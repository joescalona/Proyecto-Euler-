#Serie de Fibonacci
fib=[1,2]
fibpar=[]
while True:
	if 4000000>fib[-1]:
		fib.append(fib[-1]+fib[-2])
	else:
		fib.remove(fib[-1])
		break
for i in fib:
	if i%2==0:
		fibpar.append(i) 
def suma(lista):
	suma=0
	for x in lista:
		suma=suma+x
	return suma
#print fib
#print fibpar
print suma(fibpar)


	
	
