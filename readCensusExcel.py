#! python3
#! readCensusExcel.py 

import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

#Makes a dictionary for the data calculated by the program
countyData = {}
"""
The rows:
A - tract number
B - state abbreviation
C - County name
D - Population
"""

#Iterates through the rows of the sheet
for row in range(2,sheet.max_row + 1):
	state = sheet['B'+str(row)].value
	county = sheet['C'+str(row)].value
	pop = sheet['D'+str(row)].value

	#Sets a value for state if it doesn't already exist
	countyData.setdefault(state,{})

	#Sets a value for the county and the following charactersitics 
	countyData[state].setdefault(county,{'tracts':0,'pop':0})

	#Each row represents one census tract therefore with each row, increment by one
	countyData[state][county]['tracts'] +=1

	#Increase the population
	countyData[state][county]['pop'] += int(pop)
		
print('Writign results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
