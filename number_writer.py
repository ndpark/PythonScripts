#! python3
# number_writer.py

import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json' #Choose a filename
with open(filename,'w') as f_obj: #Open the file in write mode
	json.dump(numbers,f_obj) #Store numbers as numbers.json