def boxPrint(symbol,width, height):
	if len(symbol) != 1:
		raise Exception('Sylmbol must be single string')
	if width <= 2:
		raise Exception('Width must be greater than 2')
	if height<=2:
		raise Exception('Height must be greater than 2')
	print(symbol*width)
	for i in range(height -2):
		print(symbol + (' '*(width-2))+ symbol)
	print(symbol*width)


num = int(input('\nHow many times do you want iterated? '))

for number in range(num):
	sym = input('`WAHT SMBOL: ')
	w = int(input('WHAT WEIDTH: '))
	h = int(input('WHAT HEIGHT: '))

	try:
		boxPrint(sym,w,h)
	except Exception as err:
		print('An exception has occured: ' + str(err))