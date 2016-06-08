opcs="si"
listaestudiantes=[]
listanotas=[]
while opcs=="si":
	opc=int(input("1. Crear estudiante \n2. Ingresar notas \n3. Reporte de notas \n4. Salir \n: "))
	if opc==1:
		estudiante=input("Ingresar nombre de estudiante: ")
		listaestudiantes.append(estudiante)
	elif opc==2:
		print("Escoja el estudiante a quien desea ingresar notas: ")
		print(listaestudiantes)
		opcss=input(":")
		
		nota=int(input("Ingrese Nota: "))

	elif opc==3:
		for x in open("archivodenotas.txt", "r"):
			print(x)
	archivo=open("archivodenotas.txt", "w")
	for nota in listanotas:
		archivo.write.write(estudiante)
		archivo.write.write(str(nota))
		archivo.write.write("\n")
archivo.close()
