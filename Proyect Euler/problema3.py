import math as m 

def factorizar(n,listar=True): 				#Defino funcion para encontrar numeros primos
	p=n
	lista1=[]								
	
	while n%2 == 0: 						#Veo si el numero n es par o no.
		lista1.append(2) 					#Como 2 es primo y factor, por lo tanto lo inserto en lista1.
		n = n/2					 			#Divido a n por 2 para seguir. 
											#Hasta este punto, n es impar. 
	for i in range(3,int(m.sqrt(n))+1,2):	#El paso es de 2 para evitar todos los numeros pares, asi ahorro tiempo y el programa es eficaz. 
		if n%i==0:							
			lista1.append(i)					
			n=n/i 
	if n>2:									#Condicion si n es un primo mayor a 2
		lista1.append(n)
	if listar==True:
		print ("Los factores primos de "+str(p)+" son "+str(lista1))
	else:
		return lista1
def maximofactor(n):						#Defino funcion para encontrar el primo mayor de los factores
	lista=factorizar(n,False)				#lista=lista de factores primos de n		
	maximo=lista[-1]						#maximo= ultimo elemento de lista
	print maximo 
print('-------------------------------------------------------------------------------------------------------------')
x=int(input('DIME UN NUMERO  '))
maximofactor(x)
print('-------------------------------------------------------------------------------------------------------------')
	
	
