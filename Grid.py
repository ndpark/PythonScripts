grid = [['.', '.', '.', '.', '.', '.'],        
		['.', 'O', 'O', '.', '.', '.'],       
		['O', 'O', 'O', 'O', '.', '.'],        
		['O', 'O', 'O', 'O', 'O', '.'],        
		['.', 'O', 'O', 'O', 'O', 'O'],        
		['O', 'O', 'O', 'O', 'O', '.'],        
		['O', 'O', 'O', 'O', '.', '.'],        
		['.', 'O', 'O', '.', '.', '.'],        
		['.', '.', '.', '.', '.', '.']]
string = ''
def rotatePic(putGridHere,string):
	for i in range(0,len(putGridHere[0])): #goes down rows
		string = ''
		for j in range(0,(len(putGridHere))): #goes thorough columns
			string += putGridHere[j][i] # Add the contents to the string
		print(string) # Prints row after it's done

rotatePic(grid,string)
