import subprocess
from files import findFiles
import codecs

def init(args):
	path = args["root"] if "root" in args else "."
	path = path + (("/"+args["path"]) if "path" in args else "")
	global storyboardFiles, stringsFiles
	storyboardFiles = findFiles(".storyboard", path+"/Base.lproj")
	stringsFiles = findFiles(".strings", path+"/fr.lproj")

	global resourceContent
	resourceContent = {}

def close():
	for storyboard, (path, content) in resourceContent.iteritems():
		with open(path, 'w') as file:
			file.write(content)
			file.close()

def writeText(row, storyboard):
	if storyboard != None and storyboard.lower() in resourceContent:
		(path, content) = resourceContent[storyboard.lower()]
		resourceContent[storyboard.lower()] = (path, content.replace("#{"+row.key+"}", row.text))

def writeComment(row, storyboard):
	None

def writeStoryboard(row, storyboard):
	if storyboardFiles != None:
		for (rootStory, fileStory) in storyboardFiles:
			if fileStory.lower() == storyboard.lower()+".storyboard":
				storyPath = rootStory+"/"+fileStory
				for (rootStrings, fileStrings) in stringsFiles:
					if fileStrings.lower() == storyboard.lower()+".strings":
						stringsPath = rootStrings+"/"+fileStrings
						subprocess.call(["ibtool", storyPath, "--generate-strings-file", stringsPath])
						file = codecs.open(stringsPath, encoding='utf-16')
						resourceContent[storyboard.lower()] = (stringsPath, file.read())
						file.close
