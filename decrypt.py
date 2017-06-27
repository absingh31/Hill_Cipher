#!/usr/bin/python3

############################################################################################################################
# Program to generate decrypted file which is encrypted with hill cipher
# Abhishek Singh 
# Use case : python3 decrypt.py [encrypted_file name]
############################################################################################################################
import string
import sys
import numpy as np
import math
from numpy import matrix
from numpy import linalg

def decrypt_cipher(file):
	with open(file) as f:
		p_text=f.read()
		n= len(p_text)
		k = n%8
		A_inv=modMatInv(A,47)
		if k > 0:
			p_text = p_text + ' '*(8-k)
			n = n + 8-k
		output=''
		counter=0
		for bnum in range(int(n/8)):
			block = p_text[bnum*8:(bnum+1)*8].upper()
			block_vec = []
			for x in block:
				block_vec.append(alph.index(x))
			decrypt_val=A_inv*np.matrix(block_vec).T
			decrypt_val=decrypt_val.T.tolist()[0]
			decrypt_val = ''.join ( [ alph[int(x)%47] for x in decrypt_val] )
			counter=counter+1
			output=output+decrypt_val
			counter=0
	d_file = open("Decrypted_file",'w')
	d_file.write(output)


def modMatInv(A,p):
	n=len(A)
	A=matrix(A)
	adj=np.zeros(shape=(n,n))
	for i in range(0,n):
		for j in range(0,n):
			adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
	return (modInv(int(round(linalg.det(A))),p)*adj)%p

alph="0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ,.;:'?!()" +"\n"
A = np.matrix([[3,1,7,1,2,4,4,19],[2,0,11,19,-3,2,8,39],[14,45,8,6,-21,21,5,3],[1,2,3,4,5,6,7,-8],[10,20,11,21,30,40,31,41],[8,7,6,5,4,3,2,1],[35,16,46,0,8,25,1,4],[2,3,3,0,3,0,1,1]])

def modInv(a,p):
	for i in range(1,p):
		if (i*a)%p==1:
			return i

def minor(A,i,j):
	A=np.array(A)
	minor=np.zeros(shape=(len(A)-1,len(A)-1))
	p=0
	for s in range(0,len(minor)):
		if p==i:
			p=p+1
		q=0
		for t in range(0,len(minor)):
			if q==j:
				q=q+1
			minor[s][t]=A[p][q]
			q=q+1
		p=p+1
	return minor

if __name__ == '__main__':
	if(len(sys.argv)==2):
		decrypt_cipher(sys.argv[1])

	else:
		print("Wrong Input")
