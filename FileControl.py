# reading file and spliting words into list.
def readPlainText(fname):
    planeText = open(fname, "r")
    listOfWords = planeText.read().split()
    return listOfWords
#further breakdown of words to lists of characters.
def getCharacters(listOfWords):
    listOfCharacters = list(map(list, listOfWords))
        #print(listOfCharacters)
    return listOfCharacters

#put together text from 
def buildCipherTxt(x,list):
    txt = x.join(list).upper()
    return txt

#out put to Cypher text to file
def outputCypherText(x,fname):
    new = open(fname, "w")
    
    for i in x:
        new.write(i)
    
    new.close()

#Reduce nested List to list of words
def reduceList(x):
    l=[]
    for i in range(len(x)):
        l.append("".join(x[i]))   
    
    return l


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
