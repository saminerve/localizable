from enum import Enum

class RowType(Enum):
	text = 1
	comment = 2
	storyboard = 3
	
class LocalizableRow:
	"""Row of localizable file"""
	def __init__(self, sheet_row):
		self.key = sheet_row[0]
		self.page = sheet_row[1]
		self.section = sheet_row[2]
		self.label = sheet_row[3]
		self.text = sheet_row[4]

	def getRowType(self):
		if self.key != "#":
			return RowType.text
		elif self.page.lower() == "storyboard":
			return RowType.storyboard
		else:
			return RowType.comment

class LocalizableEngine:
	"""Keep state of localization engine"""
	def __init__(self, args):
		self.storyboard = None
		self.args = args

	def setRow(self, localizableRow):
		if localizableRow.getRowType() == RowType.storyboard:
			self.storyboard = localizableRow.section
