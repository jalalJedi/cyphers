import pandas as pd
import numpy as np
import FileControl as fc
import math as ma
from collections import OrderedDict

key = "Kinggss"

pTxt = "Thaught is not the action and not the hope but it is the action within as for any other it is none but the method"
pTxtFile = "encriptme.txt"
CTxt = ""

# Strips Key from any duplicate letters
def stripKey(key):
	key = "".join(OrderedDict.fromkeys(key))
	return key

# returns numbered rank of key characters
def ranKey(key):
	key = key.lower()
	numericKey = []

	for i in key:
		numericKey.append(fc.letters.index(i))
		

	rank_lst = [sorted(numericKey).index(values)+1 for values in numericKey]
	#print(rank_lst)
	return rank_lst

# Create and fill grid with characters.
# Returns pandas dataframe.
def CreatGrid(pTxt,key):
	key = stripKey(key)
	
	#break down text into list of characters.
	CharacterList =  [char for char in pTxt]
	
	# define grid dimensions.
	width = len(key)
	
	# Math.ceil() used to round the number of rows in case the result is float. 
	length = ma.ceil(len(CharacterList)/width) 
		
	# set dataframe "grid" with predifinde shape (rows,collumns).
	grid = pd.DataFrame(index = np.arange(1,length+1), columns = np.arange(1,width+1))

	# Fill Text to Grid
	counter = 0
	for i in range(1,length+1):
		for j in range(1,width+1):
			if counter < len(CharacterList):
				grid.at[i,j] = CharacterList[counter]
				counter+=1
			else:
				grid.at[i,j] = 'X'

	return grid

# encryption funtion shifts columns based in key rank
# outputs a cypher grid in a pandas dataframe
def encrypt(grid,rankey):
	grid = grid[rankey]
	
	return grid

#converts dataframe series "columns" to nested list
def creatList(rankey, cypherGrid):
	gridlist=[]
	
	for i in rankey:
		#gridlist = 
		gridlist.append(cypherGrid[i].tolist())
	
	return gridlist

def decrypt(grid):
	
	return 0

############# encryptionDRIVER. ##################
pTxt = fc.readPlainText(pTxtFile)
pTxt = fc.buildCipherTxt(" ",pTxt) 
# print("+----pTxt----+\n")
# print(pTxt)

grid = CreatGrid(pTxt,key)
print("+----grid----+\n")
print(grid)

rankey = ranKey(stripKey(key))
# print("+----rankey----+\n")
# print(rankey)

cypherGrid = encrypt(grid,rankey)
# print("+----cypherGrid----+\n")
# print(cypherGrid)

list1 = creatList(rankey, cypherGrid)
print("+----list----+\n")
print(list1)

list2 = fc.reduceList(list1)
print("+----reduced list!----+\n")
print(list2)

ctxt = fc.buildCipherTxt("-",list2)
print("+----ctxt----+\n")
print(ctxt)

fc.outputCypherText(ctxt,"BCTCcypherText.txt")



############# TEST DRIVER. #############
# print(grid)
# print(rankey)
# print(cypherGrid)
# print(ctxt)