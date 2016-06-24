#range(len(list)) can be used to iterate through lists
dogs = []
while True:
	name = input('Dog name for dog # ' + str(len(dogs)+1) + '\nType in empty space to exit\n>>')
	dogs = dogs + [name] #Making a new list called name, and then adding it to dogs list
	if name == ' ':
		break
print ('The dog names are:')
for name in dogs:
	print('The name is ' + name)
	
	
"""for i in range(len(list))
	print ('blah' + str(i) + 'blah' + list[i])
	If you think about it it makes sense because 
	
'in' and 'not in' can be written to check if something is in an array , similar to search
 
something.index() can search which value that is passed 
example: spam = ['hello','google','dog','cat']
spam.index('hello')
0
etc

spam.insert(1,'dog') will insert the index into the array
sort() works --(reverse==True) to make it go reverse. Must all be the same type.
remove() removes an element

list is mutable; string is not.

tuples are same as lists except immutble