# Program to generate crypto project
# Abhishek Singh 
# the current directory should  have
# File named Normal.txt which will be encrypted
#######################################################

def matmult(A,v): # multiply a marix A by a vector v
    n =len(v)
    Av=[]
    for i in range(len(A)):
        s = 0
        for j in range(n):
            s += A[i][j]*v[j]
        Av.append(s)    
    return Av

#######################################################
# the symbol list

alph="0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ,.;:'?!()" +"\n"

#######################################################

# the encryption matrix

A = [
        [3,1,7,1,2,4,4,19],[2,0,11,19,-3,2,8,39],[14,45,8,6,-21,21,5,3],[1,2,3,4,5,6,7,-8],[10,20,11,21,30,40,31,41],[8,7,6,5,4,3,2,1],[35,16,46,0,8,25,1,4],[2,3,3,0,3,0,1,1]]
#######################################################


book = open("To_encrypt.txt","r").readlines()   # Input text file for encryption 

cfile = open( "Encrypted_File", 'w')# cipher file for that will be generated
ptext = ''.join(book[:-1]) # Take input from file
n = len(ptext)
k = n%8#prepare for padding for blocks size 8. Encryption matrix is 8x8
if k > 0:
	ptext = ptext +  ' '*(8-k)
	n = n + 8-k   
    # padding done   
for bnum in range(int(n/8)):#proces block by block, bnum is block number
	block = ptext[bnum*8:(bnum+1)*8].upper()
	block_vec = []
	for x in block:
		if x in alph:
			block_vec.append(alph.index(x))
		else:    
			block_vec.append(36)
	eblock = matmult(A, block_vec)
	eblock  =  ''.join ( [ alph[x%47] for x in eblock] )
	cfile.write(eblock) #encrypted block written to cipher file
cfile.close()
print("Encrypted file written")

