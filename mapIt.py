#! python3
# mapIt.py - Launches  a map in browser using address from clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:]) #Chops off the first element of the array
else:
	address = pypreclip.paste()
	
webbrowser.open('https://www.google.com/maps/place/'+address)
