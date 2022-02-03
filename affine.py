import FileControl as fc
#let number of elements in letters be x in mod*x
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Key values are used in the encryption and decryption equations
k1 = 5
k2 = 8

#Map letter input to coresponding value.
def mapper(x):  
	#convert each letter to lower case.
	y = str(x.lower()) 
	return letters.index(y)

#Reverse Mapping to assign digit to cypher letter. NOT USED! ###
def revMapper(x):
	return letters[x]

#Pass each element through the encription f(x)= (a X + b)mod26.
def encript(x):
	result = (k1 * mapper(x) + k2)% len(letters)
	x=result
	#print(x)
	return x

#Find the GCD of inverse key mod 26
def GCD_INV_MOD(x):
	for i in range(len(letters)):
		if x * i % len(letters) == 1:
			return i

#decrption equation
def decript(x):
	result = GCD_INV_MOD(k1)*(x-k2)

	return result

# Test decripter
def decripter(x):
	result = GCD_INV_MOD(k1) * (mapper(x) - k2)

	return result






#MAIN SECTION...DRIVER CODE
list = fc.getCharacters(fc.readPlainText("encriptme.txt"))


#runs the encription and revers maps the numeric values to cipher text

for i in range(len(list)):
	for j in range(len(list[i])):
		list[i][j] = revMapper(encript(list[i][j]))

cipher = fc.reduceList(list)
fc.outputCypherText(fc.buildCipherTxt("",cipher), "AffineCypherText.txt",)




#runs file output function 
#fc.output(lana)

print("+----list----+\n")
print(list)
test = decripter(list)
test = " ".join(fc.reduceList(test))
print(test)


