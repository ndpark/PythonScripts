#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
#Usage: py.exe mcb.pyw save <keyword> will save clpboard to keyboard
#		py.exe mcb.pyw <keyword> will load keyword to clipboard
#		py.exe mcb.pyw list will load all keywords to clipboard

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb') #The shelve file will be called MCB- multiple clipboard

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
	#Keywords and load content
	if sys.argv[1].lower() == 'list': #If there's one commanding argument, check if it's list
		pyperclip.copy(str(list(mcbShelf.keys()))) #Copies content onto clipboard if it's "list"
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		
mcbShelf.close()
