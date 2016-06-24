def addComma(list):
	list.insert(-1,'and') #inserts 'and' to last spot in the list
	string = list[0]#makes a string - apples is now a string
	for i in range(len(list)-2): #while i is 2 less than the length,
		string = string + ', ' + list[i+1] #string is: apple, bananas, tofu, and
	string = string + ' ' + list[-1] #string is now: apple, bannas, tofu, and cats
	print(string)
		
spam = ['apples','bananas','tofu','cats']
addComma(spam)