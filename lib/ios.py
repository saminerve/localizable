import os
import subprocess
from files import findFiles
import codecs

def init(args):

	path = args["root"] if "root" in args else "."
	path = path + (("/"+args["path"]) if "path" in args else "")
	global storyboardFiles, stringsFiles
	storyboardFiles = findFiles(".storyboard", path, "Base.lproj")
	stringsFiles = findFiles(".strings", path ,"fr.lproj")
	#print "Founded Paths : %s." % storyboardFiles
	global resourceContent
	resourceContent = {}

	#Add standalone Localizable.strings file
	global commonStoryboard
	commonStoryboard = "Localizable"

def close():
	for storyboard, (path, content) in resourceContent.iteritems():
		with open(path, 'w') as file:
			file.write(content)
			file.close()

def writeText(row, storyboard):
	if row.dynamic:
		storyboard = commonStoryboard

	if storyboard != None and storyboard.lower() in resourceContent:
		(path, content) = resourceContent[storyboard.lower()]
		text = replaceSpecialChars(row.text)
		if storyboard.lower() == commonStoryboard.lower():
			resourceContent[storyboard.lower()] = (path, content + "\""+row.key + "\" = \"" + text + "\";\n")
		else:
			resourceContent[storyboard.lower()] = (path, content.replace("#{"+row.key+"}", text))

def replaceSpecialChars(text):
    text = text.replace('"', '\\"')
    text = text.replace('<br/>', '\\n')
    text = text.replace('\\u', '\\U')
	text = text.replace('&amp;', '&')
    return text

def writeComment(row, storyboard):
	if commonStoryboard != None and commonStoryboard.lower() in resourceContent:
		(path, content) = resourceContent[commonStoryboard.lower()]
		resourceContent[commonStoryboard.lower()] = (path, content + "\n// "+row.section + "\n")


def writeStoryboard(row, storyboard):

	print "story", storyboard
	if storyboardFiles != None:
		for (rootStory, fileStory) in storyboardFiles:
			if fileStory.lower() == storyboard.lower()+".storyboard" or storyboard.lower() == commonStoryboard.lower():
				storyPath = rootStory+"/"+fileStory
				for (rootStrings, fileStrings) in stringsFiles:
					print storyboard.lower()+".strings"
					print fileStrings.lower()
					print "-------------------"
					if fileStrings.lower() == storyboard.lower()+".strings":
						stringsPath = rootStrings+"/"+fileStrings
						generateStringsFile(storyboard.lower(), storyPath, stringsPath)
						file = codecs.open(stringsPath, encoding='utf-16')
						resourceContent[storyboard.lower()] = (stringsPath, file.read())
						file.close
						break
				break


def generateStringsFile(storyboard, storyPath, stringsPath):
	
	if storyboard != None and storyboard.lower() == commonStoryboard.lower():
		print storyboard.lower() + " / "+commonStoryboard.lower() , "deleted and Generated"
		#print stringsPath
		os.remove(stringsPath)
		file = open(stringsPath, 'w')
		file.close()
	else:
		subprocess.call(["ibtool", storyPath, "--generate-strings-file", stringsPath])
