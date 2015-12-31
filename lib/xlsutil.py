import xlrd

def open_localizable(path):
	"""
	Open, read and returnf first sheet in Excel file
	"""

	book = xlrd.open_workbook(path)
	first_sheet = book.sheet_by_index(0)

	print first_sheet.row_values(0)

	return first_sheet
