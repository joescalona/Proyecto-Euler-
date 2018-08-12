list1=[]

for i in range(1,1000):
	if (i%3==0) or (i%5==0):
		list1.append(i)
#print(list1)

def suma(lista):
	suma=0
	for i in lista:
		suma=suma+i
	return suma

print(suma(list1))


