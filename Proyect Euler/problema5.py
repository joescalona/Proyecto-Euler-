from time import time

tiempo_inicial=time()


#Ver si un numero es divisible por 1 hasta 20
def divisible1hasta20(num):
	for i in range(1,21):
		if num%i != 0:
			return False
	return True

#comenzando por 2520, ver si es divisible por 1 hasta 20
num=2520
while True:
	if divisible1hasta20(num):
		break #Si la funcion encuentra un numero, parar
	num+= 20 #Sino, incrementar numero


print(num)
tiempo_final=time()
tiempo_ejecucion=tiempo_final - tiempo_inicial
print tiempo_ejecucion
