#from time import time


def primo(n):
	#1= si . 0=no
	primo=1
	for i in range(2,n):
		if n%i==0:
			primo = 0
			return primo
	return primo
#inicial=time()
primos=[2,]
n=3
m=int(input('Ingresa la posicion que quieres saber del numero primo = '))
while True: 
	if primo(n):
		primos.append(n)
		n=n+1
		if len(primos)==m:
			#print n
			print primos[-1]
			break
	else:
		n=n+1
print primos
#final=time()

#total=final - inicial

#print total

