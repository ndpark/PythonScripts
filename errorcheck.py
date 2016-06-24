def spam(divideBy):
	try:
		return 42/divideBy
	except ZeroDivisionError:
		print('Error: Invalid argument.')

print(spam(2))
print(spam(8))
print(spam(0))
print(spam(17))

#Try function can be used to detect an error. It will move to except if it fails. 