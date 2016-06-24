#! python3
# backupToZip.py - Copies entire folder and its content into a zip file, increments filename

import zipfile, os


def backupToZip(folder):
	folder = os.path.abspath(folder) #Folder must be absolute
	
	#Figures out what the filename should be
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_'+ str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number +1
		
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in%s...' % (foldername))
		backupZip.write(foldername)
		for filename in filenames:
			newBase/ os.path.basename(folder)+'_'
			if filename.startswith(newBase) and filename.endswith('.zip')
				continue 
			backupToZip.write(os.path.join(foldername,filename))
	backupZip.close()
	print('Done')

	
fileDir = input('Please insert filename')
backupToZip(fileDir)