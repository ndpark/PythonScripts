import sys

while True:
	print('Type \'Exit\' to exit.')
	response = input()
	if response == 'exit':
		sys.exit()
	print ('You typed' + response + '.')