#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import yaml
import os

from lib import xlsutil
from lib import platform
from classes import LocalizableEngine, LocalizableRow

reload(sys)  
sys.setdefaultencoding('utf8')

if len(sys.argv) < 2:
    sys.exit('Usage: %s file.yaml' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: File %s was not found!' % sys.argv[1])

parameters =  yaml.load(open(sys.argv[1]))


def launchLocalizationEngine(sheet, args):
	engine = LocalizableEngine(args)

	platform.init(engine)

	for rownum in range(sheet.nrows):
		localizableRow = LocalizableRow(sheet.row_values(rownum))
		engine.setRow(localizableRow)
		platform.write(localizableRow, engine.storyboard)

	platform.close()

if __name__ == "__main__":

    file = parameters["datasource"]
    localizable_sheet = xlsutil.open_localizable(file)
    launchLocalizationEngine(localizable_sheet, parameters)