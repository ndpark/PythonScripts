def isPhoneNumber(text):
	if len(text) != 12: #Checks if the length of string is 12
		return False
	for i in range (0,3):
		if not text[i].isdecimal(): #Checks if area code is number
			return False
	if text[3] != '-': #Checks if there is a hyphen
		return False
	for i in range(4,7):
		if not text[i].isdecimal(): #Is rest numbers
			return False
	if text[7]!='-':
		return False
	for i in range(8,12): #Number check
		if not text[i].isdecimal():
			return False
	return True

'''
print('905-399-1236 is a phone number:')
print(isPhoneNumber('905-399-1236'))
print('Hello is not a phone number:')
print(isPhoneNumber('Hello')) '''

messege = 'Here is Jack\'s number: 905-388-1237, and here is Kelsey\'s, 905-233-0923.'
for i in range(len(messege)):
	chunk = messege[i:i+12] #Chunk becomes different with each iteration (Kinda like bubble sort)
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk) #Prints out chunk if a phone number is found
print('Done')