import csv

def readFile(filename = "datos.txt"):
	#print()
	with open(filename,'r') as file:
		try:
			reader = csv.reader(file)
			n = int(next(reader)[0])
			datos = [[0 for x in range(2)] for x in range(n)]
			x = y = 0
			#print("{:10} {:10}".format("X","Y"))
			for row in reader:
				for val in row:
					datos[x][y] = float(val)
					print("{:5}".format(val), end=" ")
					y += 1
				print("")
				x += 1
				y = 0

		except csv.Error as e:
			sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
	return datos

readFile()
'''
option = "";
while (option != "x"):
	print()
	print("A) Interpolacion Exacta")
	print("B) Interpolacion Aproximada")
	print("X) Salir")
	print()

	option = input("Por favor seleccione una opcion: ")
	if(option == "A" or option == "a"):
		datos = readFile()
		print()
		valor = float(input("Por favor indique el valor a interpolar: "))
		Lagrange(datos, valor)
'''
