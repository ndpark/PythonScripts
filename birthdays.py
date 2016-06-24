birthdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}

while True: #Will always run
	print('Enter a name: (blank to quit)') #Say this
	name = input()
	if name == '': #If name is blank, then the program will quit
		break
	
	if name in birthdays:
		print(birthdays[name] +' is the birthday of '+ name) #If the name already exists, this will be prompted
	else:
		print('I do not have a birthday info for ' + name)
		print('What is their birthday?')
		bday=input()
		birthdays[name] = bday
		print('Databse updated.')