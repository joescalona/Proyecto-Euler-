def primo(n):
	#1= si . 0=no
	primo=1
	for i in range(2,n):
		if n%i==0:
			primo = 0
			return primo
	return primo
primos=[2,]
n=3
print('************************* SUMA NUMEROS PRIMOS *************************')
m=int(input('INGRESA EL TOPE = '))
while primos[-1]<m:
	if primo(n):
		primos.append(n)
		n=n+1
	else:
		n=n+1
primos.pop(-1)
sum=0
for i in primos:
	sum=sum+i

#print primos

print sum

