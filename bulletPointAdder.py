#! python3
# bulletPointAdder.py - adds wikipedia bullet points to the start of each text

import pyperclip
text = pyperclip.paste()

#Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '*' + lines[i]

text= '\n'.join(lines) #Turns strings into seperate lists

pyperclip.copy(text)
print(text)


