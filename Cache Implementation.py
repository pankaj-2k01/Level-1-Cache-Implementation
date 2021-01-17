#Pankaj Kumar
#Computer Organization
from math import *
def main():
	print("------------------------------------CACHE MAPPING------------------------------------------")
	S=int(input("Enter the Cache Size : "))
	CL=int(input("Enter the Cache Lines : "))
	B=int(input("Enter the Block Size : "))
	
	if(isPowerOfTwo(S) and isPowerOfTwo(CL) and isPowerOfTwo(B) and S!=0 and CL!=0 and B!=0 and B>1):
		if(S/B==CL):
			print()
			mapp=input("Enter the cache_mapping\n1.Direct Mapping\n2.Associative Mapping\n3.K-way Associative\n")
			if(mapp=="1"):
				direct_mapping(S,CL,B)
			elif(mapp=="2"):
				associative(S,CL,B)
			elif mapp=='3':
				k_way_Asso(S,CL,B)
	else:
		print("Please Enter the all of the above inputs in power of 2 and not equal to 0 and B>1")

def isPowerOfTwo(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
    return True

def check(num):
	temp=1
	i=0
	while(num>pow(2,i)):
		i+=1
	return i

def final_nooffset(num,B):
	temp=str(num)
	bits_required=check(B)
	boff=temp[-bits_required:]
	bno=temp[:-bits_required]
	#print(boff,"  ",bno)
	return boff,bno

def binaryToDecimal(binary1): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal 



def cache_print(CL,B,W):
	for i in range(len(CL)):
		print(i,CL[i],end="\t")
		for j in range(B):
			print(W[i*(B)+j],end=" ")
		print()

def direct_mapping(S,CL,B):
	print("-----------------------------------DIRECT MAPPING------------------------------------------")
	no_of_word=CL*B;
	cache_line=[]
	words=[]
	for i in range(CL):
		cache_line.append("null")
	for i in range(no_of_word):
		words.append("empty")
	y=True
	while(y):
		char=int(input("What do you want to do 1. Read 2. Write : "))
		while(char not in [1,2]):
			char=int(input("What do you want to do 1. Read 2. Write : "))
		add=input("Enter the address : ")
		print()
		while(not isBinary(add)):
			add=input("Enter the address : ")
		blooff,blno=final_nooffset(add,B)

		locator=int(blno,2)%CL
		repl_data=[cache_line[locator]]
		if(char==1):
			print("----------READ---------")
			if int(blno,2) in cache_line:
				print("cache hit")
			else:
				print("cache miss")
			for i in range(B):
				repl_data.append(words[locator*B+i])
				words[locator*B+i]='empty'
			cache_line[locator]=int(blno,2)
			if(repl_data[0]!="null"):
				print("Data is replaced with:",end="  ")
				print(repl_data)
			cache_print(cache_line,B,words)
	
		if(char==2):
			print("----------WRITE---------")
			if int(blno,2) in cache_line:
				print("cache hit")
			else:
				print("cache miss")
			repl_data=[cache_line[locator]]
			for i in range(B):
				repl_data.append(words[locator*B+i])
				words[locator*B+i]="empty"
			cache_line[locator]=int(blno,2)
			data=input("Enter the data to be written : ")
			replaced_data=words[locator*B+int(blooff,2)]
			for i in range(B):
				words[locator*B+i]="empty"
		
			words[locator*B+int(blooff,2)]=data
			if(repl_data[0]!="null"):
				print("Data is replaced with:",end="  ")
				print(repl_data)
			cache_print(cache_line,B,words)

		operation=input("want to perform more operation\nEnter 0 : ")
		if(operation=='0'):
			y=True
		else:
			print("Exit")
			y=False

def isBinary(num):
    if (len(num)<1):
        return False
    for i in str(num):
        if i not in ['1','0']:
            return False
    return True
def associative(S,CL,B):
	print("-----------------------------------ASSOCIATIVE MAPPING------------------------------------------")
	no_of_word=CL*B;
	cache_line=[]
	words=[]
	for i in range(CL):
		cache_line.append("null")
	for i in range(no_of_word):
		words.append("empty")
	y=True
	while(y):
		#print("lopp")
		char=int(input("What do you want to do 1. Read 2. Write : "))
		while(char not in [1,2]):
			char=int(input("What do you want to do 1. Read 2. Write : "))


		add=input("Enter the address : ")
		print()
		while(not isBinary(add)):
			add=input("Enter the address : ")
		blooff,blno=final_nooffset(add,B)
		blooff=int(blooff,2)
		blno=int(blno,2)
		if(char==1):
			print("----------READ---------")
			if blno in cache_line:
				print("cache hit")
			else:
				print("cache miss")
				check=True
				for i in range(len(cache_line)):
					t=blno
					if(cache_line[i]=="null"):
						cache_line[i]=blno
						t=t-blno
						check=False
						break
				if(check):
					index=cache_line[0]
					repl_data=[index]

					for i in range(B):
						pos=words[i]
						repl_data.append(pos)
						words[i]="empty"
					cache_line[0]=blno
					print("Data is replaced with:",end="  ")
					print(repl_data)
			#cache_print(cache_line,B,words)
		if(char==2):
			print("----------WRITE---------")
			data=input("Enter the data :")
			check=True
			if(blno in cache_line):
				print("cache hit")
				print()
				for i in range(len(cache_line)):
					pos=blno
					index=i*B+blooff
					if(cache_line[i]==pos):
						words[index]=data
						print("cache hit")
						break
		
			
			else:
				print("cache miss")
				for i in range(len(cache_line)):
					if(cache_line[i]=="null"):
						cache_line[i]=blno
						index=i*B+blooff
						words[index]=data
						check=False
						break
				if(check):
					repl_data=[cache_line[0]]
					for i in range(B):
						repl_data.append(words[i])
						words[i]="empty"
					cache_line[0]=blno
					words[blooff]=data

					print("Data is replaced with:",end="  ")
					print(repl_data)
			# cache_print(cache_line,B,words)
		cache_print(cache_line,B,words)
		operation=input("want to perform more operation\nEnter 0 : ")
		if(operation=='0'):
			y=True
		else:
			print("Exit")
			y=False
	
def k_way_Asso(S,CL,B):
	print("--------------------------------SET ASSOCIATIVE MAPPING------------------------------------------")
	no_of_word=CL*B;
	cache_line=[]
	words=[]
	for i in range(CL):
		cache_line.append("null")
	for i in range(no_of_word):
		words.append("empty")
	k=int(input("Enter value of k\t"))
	no_of_set=CL//k
	if(no_of_set==0):
		associative(S,CL,B)
	else:
		y=True
		while(y):
			#print("lopp")
			char=(input("What do you want to do 1. Read 2. Write : "))
			while(char not in ['1','2']):
				char=int(input("What do you want to do 1. Read 2. Write : "))


			add=input("Enter the address : ")
			while(not isBinary(add)):
				add=input("Enter the address : ")
				print()
			blooff,blno=final_nooffset(add,B)
			blooff=int(blooff,2)
			blno=int(blno,2)
			locator=blno%k
			x=locator*no_of_set
			L=cache_line[x:x+k]
			index=locator*k
			if(char=='1'):
				print("----------READ---------")
				if blno in cache_line:
					print("cache hit")
				else:
					print("cache miss")
					check=True
					for i in range(len(L)):
						if(L[i]=="null"):
							cache_line[index+i]=blno
							check=False
							break
					if(check):
						p=cache_line[index]
						repl_data=[p]
						for i in range(B):
							pos=index*B+i
							repl_data.append(words[pos])
							words[index*B+i]="empty"
						cache_line[index]=blno
						print("Data is replaced with:",end="  ")
						print(repl_data)
				#cache_print(cache_line,B,words)
			if(char=='2'):
				print("----------WRITE---------")
				data=input("Enter the data :")
				check=True
				if(blno in cache_line):
					print("cache hit")
					for i in range(len(L)):
						if(L[i]==blno):
							temp=words[(i+index)*B+blooff]
							words[(i+index)*B+blooff]=data
							check=False
							break

				else:
					print("cache hit")
					for i in range(len(L)):
						if(L[i]=="null"):
							cache_line[i+index]=blno
							words[(i+index)*B+blooff]=data
							check=False
							break
					if(check):
						pos=cache_line[index]
						repl_data=[pos]
						for i in range(B):
							t=index*B+i
							repl_data.append(words[t])
							words[t]="empty"
						cache_line[index]=blno
						words[index*B+blooff]=data

						print("Data is replaced with:",end="  ")
						print(repl_data)
				# cache_print(cache_line,B,words)
			cache_print(cache_line,B,words)
			operation=input("want to perform more operation\nEnter 0 : ")
			if(operation=='0'):
				y=True
			else:
				print("Exit")
				y=False



main()
