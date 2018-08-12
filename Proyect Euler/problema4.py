def palindromo(n):						#dice si es palindromo o no
	der=str(n)							#der= numero leido correctamente
	alre=der[::-1]						#alre= numero leido alreves 
	if der==alre:						#Si n es palindromo, lo devolvera
		return n 

list1=range(1000,900,-1)				#va del 1000 hasta el 899
list2=range(1000,900,-1)
list3=[]
print('LOS MAYORES PALINDROMOS EN ESTE RANGO SON ')
for i in list1:							#multiplica cada elemento de list1 con cada elemento de list2
	for j in list2:
		if str(palindromo(i*j))==str(i*j):
			print (str(i)+'*'+str(j)+'='+str(i*j))
			list3.append(i*j)
print('EL MAYOR DE ELLOS ES '+str(list3[0]))




		

		
