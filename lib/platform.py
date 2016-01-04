from classes import RowType 
import android
import ios



def init(engine):
	global platformsArgs
	platformsArgs = engine.args

	if "android" in platformsArgs:
		android.init(platformsArgs["android"])

	if "ios" in platformsArgs:
		ios.init(platformsArgs["ios"])

def write(row, storyboard):
	if len(row.key) > 0:
		if row.getRowType() == RowType.text:
			writeText(row, storyboard)
		elif row.getRowType() == RowType.comment:
			writeComment(row, storyboard)
		elif row.getRowType() == RowType.storyboard:
			writeStoryboard(row, storyboard)

def writeComment(row, storyboard):
	if "android" in platformsArgs:
		android.writeComment(row, storyboard)
	if "ios" in platformsArgs:
		ios.writeComment(row, storyboard)

def writeText(row, storyboard):
	if "android" in platformsArgs:
		android.writeText(row, storyboard)
	if "ios" in platformsArgs:
		ios.writeText(row, storyboard)

def writeStoryboard(row, storyboard):
	if "android" in platformsArgs:
		android.writeStoryboard(row, storyboard)
	if "ios" in platformsArgs:
		ios.writeStoryboard(row, storyboard)

def close():
	if "android" in platformsArgs:
		android.close()
	if "ios" in platformsArgs:
		ios.close()