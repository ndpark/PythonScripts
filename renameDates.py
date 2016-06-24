#! python3
# renameDates.py - Renames filenames with MM-DD-YYYY to DD-MM-YYYY

import shutil,os,re

datePattern = re.compile("""^(.*?)
	((0|1)?\d)-		#Month
	((0|1|2|3)?\d)- #Day
	((19|20)\d\d)	#Year
	(.*?)$			#Filename
	""",re.VERBOSE)
	
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)
	
	if mo== None:
		continue
	beforePart = mo.group(1) #If the filename matches the regex, this will occur
	month = mo.group(2)
	day - mo.group(4)
	year = mo.group(6)
	whatever = mo.group(8)

euroFilename = beforePart+day+'-'+month+'-'+year+whatever

absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir,amerFilename)
euroFilename = os.path.join(absWorkingDir,euroFilename)

print('Renaming "%s" to "%s"...' % (amerFilename,euroFilename))
shutil.move(amerFilename,euroFilename) #Will rename the files
