#PROGRAMA QUE DICE SI UN NUMERO ES PALINDROMO O NO 

x=int(input('Ingrese un numero y te diremos si es palindromo o no = '))
x1=str(x)
y1=x1[::-1]

if x1==y1:
	print(str(x)+" es palindromo")
else:
	print("no lo es")
