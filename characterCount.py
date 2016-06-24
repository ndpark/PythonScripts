import pprint #Imports pretty printing

messege = 'It was a bright cold day in April, and the clocks were stiriking thirteen.'
count = {}

for character in messege:
	count.setdefault(character,0) #Counts how many times a character occurs in a string.
	count[character] = count[character]+1
	
pprint.pprint(count) #pprint will replace print function and make it prettyn

