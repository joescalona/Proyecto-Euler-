#FUNCION SUMA DE LOS NUM NUMEROS Y ELEVAR RESULTADO AL CUADRADO

def sumtotalcuadrado(num):
	x=(num*(num+1))/2 
	return x**2

#DEFINO LISTA DONDE IRA CADA ELEMENTO AL CUADRADO

list1=[]
for i in range(1,101):
	list1.append(i**2)

#SUMO CADA ELEMENTO DE LA LISTA ANTERIOR

sum=0

for j in list1:
	sum=sum+j

#X= SUMA DE LOS 100 PRIMEROS NUMEROS NATURALES AL CUADRADO

x=sumtotalcuadrado(100)

#Y=RESULTADO TOTAL
y= x - sum
print y
 