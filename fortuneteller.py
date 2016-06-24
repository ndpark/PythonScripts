import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber == 2:
		return 'It is decidedly so'
	elif answerNumber == 3:
		return 'Yes'
	elif answerNumber == 4:
		return 'Eh'
	elif answerNumber == 5:
		return 'Ask again later'
	elif answerNumber == 6:
		return 'Concentrate and ask again'
	elif answerNumber == 7:
		return 'No'
	elif answerNumber == 8:
		return 'Nope'
	elif answerNumber == 9:
		return 'Never'
		
r = random.randint(1,9)
fortune = getAnswer(r)
print('Your fortune is: ' + fortune)

#None has no return type