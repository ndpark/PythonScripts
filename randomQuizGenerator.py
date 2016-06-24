#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, w/ answer keys

import random

#States are the keys, the capitals are their values
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


 #Generating quizzes
for quizNum in range(1):
	quizFile = open('capitalsquiz%s.txt' % (quizNum +1), 'w') #%s is like python2 - it will be replaced with number
	answerKeyFile = open('capitalsquiz_answes%s.txt' % (quizNum+1),'w') #'w' opens in write mode
	
	#Writing out the headers
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' '*20)+ 'State Capitals Quiz (Form %s)' % (quizNum+1))
	quizFile.write('\n\n')
	
	#Shuffles states
	states = list(capitals.keys()) #Lists only the keys
	random.shuffle(states) #Randomly shuffles the states around
	
	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]] #Takes it from the capitals dictionary
		wrongAnswers = list(capitals.values()) #Copies the values of capitals dictionary
		del wrongAnswers[wrongAnswers.index(correctAnswer)] #Deletes the correct answer
		wrongAnswers = random.sample(wrongAnswers,3) #random.sample selects wrongAnswers for reference, and get 3 from the dictionary
		answerOptions= wrongAnswers + [correctAnswer] #wrong and right answers are mixed
		random.shuffle(answerOptions) #Shuffle the answers
		
		quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1, states[questionNum]))
		for i in range(4):
			quizFile.write('	%s.%s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
		
		answerKeyFile.write('%s.%s\n'% (questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
	
	quizFile.close()
	answerKeyFile.close()