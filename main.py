import csv
import math

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

def calculaSumatorias(datos, orden = 3):
	sumX = 0
	sumY = 0
	n = len(datos)
	for i in range(n):
		sumY += datos[i][1]

	sumatoriasX = [0 for x in range(2*orden)]
	sumatoriasXY = [0 for x in range(orden)]

	
	for i in range(2*orden):
		for j in range(len(datos)):
			sumatoriasX[i] += math.pow(datos[j][0], i+1)
			if (i < orden):
				sumatoriasXY[i] += datos[j][1] * math.pow(datos[j][0], i+1)

	return sumatoriasX, sumatoriasXY

def calculaEcuaciones(sumatoriasX, sumatoriasXY, n, orden = 3):
	ecuaciones = [ [0 for x in range(orden + 2)] for x in range(orden + 1)]
	
	for fila in range(orden + 1):
		for col in range(orden +2):
			if(fila=0 and col=0):
				ecuaciones[fila][col] = n
			elif(j=orden+1):
				ecuaciones[fila][col] = sumatoriasXY[]
			else:
				#ecuaciones[fila][col] = 


	

option = "";
while (option != "x"):
	print()
	print("A) Ajuste Polinomial Automatico")
	print("B) Orden Polinomial Manual")
	print("X) Salir")
	print()

	option = input("Por favor seleccione una opcion: ")
	if(option == "A" or option == "a"):
		datos = readFile()
		print()
		sumatoriasX, sumatoriasXY = calculaSumatorias(datos)
		calculaEcuaciones(sumatoriasX, sumatoriasXY, len(datos))
		


	if(option =="B" or option == "b"):
		orden = int(input("Por favor indique el orden polinomial: "))
		sumatoriasX, sumatoriasXY = calculaSumatorias(datos, orden)
		calculaEcuaciones(sumatoriasX, sumatoriasXY, len(datos), orden)

