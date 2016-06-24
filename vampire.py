name = input('Name?' )
age = input('Age?' )
age = int(age)

while age < 10000:
	if name == 'Alice':
		print('Hi, Alice.')
		break
	elif age < 12:
		print('You are not Alice, Kiddo')
		break
	elif age > 2000:
		print('Alice is not an undead, Vampire')
		break
	elif age > 100:
		print('You are not Alice, Granny.')
		break
	else:
		print('IDK your age is between 12 and 99, 101 - 1999')
		break