from files import find
def init(args):

	path = args["root"] if "root" in args else "."
	(rootdir, file) = find("strings.xml", path)

	global root
	root = rootdir

	global resourceFiles
	resourceFiles = {}

def close():
	for storyboard, file in resourceFiles.iteritems():
		file.write("\n</resources>")
		file.close()

def writeComment(row, storyboard):
	if storyboard != None:
		file = resourceFiles[storyboard.lower()]
		if file != None:
			file.write("\n\t<!--  " + row.section + " -->\n")

def writeText(row, storyboard):
	if storyboard != None:
		file = resourceFiles[storyboard.lower()]
		if file != None:
			content = row.text.encode('utf-8').replace("<br/>","\\n").replace("'", "\\'").replace("&","&amp;").replace("\"", "\\\"").replace("%", "%%")

			file.write("\t<string name=\""+row.key.strip()+"\">"+content+"</string>\n")

def writeStoryboard(row, storyboard):
	if root != None:
		file = open(root+"/strings-gen-"+storyboard.lower()+".xml", "wb+")
		resourceFiles[storyboard.lower()] = file
		file.write("<resources>\n\t<!-- Generated resource file for "+storyboard+" -->\n")
