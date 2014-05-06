import csv
import math
from fractions import Fraction

def leerArchivo(filename = "datos.txt"):
	with open(filename,'r') as file:
		try:
			reader = csv.reader(file)
			n = int(next(reader)[0])
			datos = [[0 for x in range(2)] for x in range(n)]
			x = y = 0
			print("Datos:")
			print("{:5} {:5}".format("X","Y"))
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
	sumatoriasXY.insert(0,sumY)
	return sumatoriasX, sumatoriasXY

def calculaOrden(datos):
	orden = 0
	numVal = len(datos) #numero de valores de deltaY
	valoresY = []
	for i in range(len(datos)):
		valoresY.append(datos[i][1])

	while numVal > 0:
		flag = True
		for i in range(len(valoresY)-1):
			valoresY[i] = valoresY[i+1] - valoresY[i]
		valoresY.pop(len(valoresY)-1)
		for i in range(len(valoresY)-1):
			if valoresY[i] != valoresY[i+1]:
				flag = False
		numVal -= 1
		orden += 1
		if flag:
			return orden
	return orden
	


def calculaEcuaciones(sumatoriasX, sumatoriasXY, n, orden = 3):
	ecuaciones = [ [0 for x in range(orden + 2)] for x in range(orden + 1)]
	num_ecuacion = 0
	num_termino = 0
	for x in range(len(ecuaciones)):
		for y in range(len(ecuaciones[0])-1):
			ecuaciones[x][y] = Fraction(sumatoriasX[x+y-1])
	posXY = len(ecuaciones[0]) - 1
	for x in range(len(ecuaciones)):
		ecuaciones[x][posXY] = Fraction(sumatoriasXY[x])

	ecuaciones[0][0] = Fraction(n)
	return ecuaciones

def printEcuacion(valores):
	ec = "\nEcuacion:\n"
	for x in range(len(valores)):
		if int(valores[x]) != 0 and x == 1:
			ec += " + "
			if int(valores[x]) == 1:
				ec += "X"
			else:
				ec += str(valores[x]) + "X"

		elif int(valores[x]) != 0 and x != 0:
			ec += " + "
			if int(valores[x]) == 1:
				ec += "X^" + str(x)
			else:
				ec += str(valores[x]) + "X^" + str(x)
		elif x == 0:
			ec += str(valores[x])
	print(ec)

'''
	GAUSS-JORDAN
'''

def changeRow(matrix, rowA, rowB):
	tmp = matrix[rowA]
	matrix[rowA] = matrix[rowB]
	matrix[rowB] = tmp
	printMatrix(matrix, "R{} <--> R{}".format(rowA, rowB))

def sumRow(matrix, rowA, rowB, multiplier=1):
	if multiplier == 0:
		#sys.exit("Error: Invalid operation, can't multiply by 0...")
		return
	for x in range(len(matrix[rowA])):
		matrix[rowA][x] += multiplier*matrix[rowB][x]
	printMatrix(matrix, "R{0} <-- R{0} + ({2})R{1}".format(rowA, rowB, multiplier))

def multiplyRow(matrix, row, val):
	if val == 0:
		#sys.exit("Error: Invalid operation, can't multiply by 0...")
		return
	for x in range(len(matrix[row])):
		matrix[row][x] *= val
	printMatrix(matrix, "R{0} <-- ({1})R{0}".format(row, val))

#TERMINAN OPERACIONES BASICAS

def gaussJordan(matrix, fila):#No es necesario saber el tamaño de la columna
	selectPivot(matrix)
	for i in range(fila):
		createPivot(matrix, i)
		for row in range(fila):
			if row != i:
				sumRow(matrix, row, i, -1*Fraction(matrix[row][i]))
				if matrix[row][i] >= 0:
					pass#sumRow(matrix, row, i, -1*Fraction(matrix[row][i]))
				else:
					pass#sumRow(matrix, row, i, Fraction(matrix[row][i]))
	valores = []
	pos = len(matrix[0]) - 1
	for x in range(len(matrix)):
		valores.append(matrix[x][pos])
	return valores

def selectPivot(matrix):
	rowNum = 0
	for row in matrix:
		if row[0] != 0:
			if rowNum != 0:
				changeRow(matrix, 0,rowNum)
			return
		rowNum += 1
	sys.exit("Error: There's no pivot...")

def createPivot(matrix, i):
	multiplyRow(matrix, i, Fraction(matrix[i][i].denominator)/Fraction(matrix[i][i].numerator))


def printMatrix(matrix, msg="Matrix:"):
	pass
	'''
	print("\n" + msg + "\n")
	rowLen = len(matrix[0])
	for row in matrix:
		for x in range(rowLen):
			print("{:6}".format(row[x]), end=" ")
		print()
	print("\n" + "======="*rowLen)
	'''


'''
	TERMINA GAUSS-JORDAN
'''

option = "";
while (option != "x"):
	print()
	print("A) Ajuste Polinomial Automatico")
	print("B) Orden Polinomial Manual")
	print("X) Salir")
	print()

	option = input("Por favor seleccione una opcion: ")
	if(option == "A" or option == "a"):
		datos = leerArchivo()
		orden = calculaOrden(datos)
		print("\nEl orden utilizado es: ", orden)
		sumatoriasX, sumatoriasXY = calculaSumatorias(datos, orden)
		ecuaciones = calculaEcuaciones(sumatoriasX, sumatoriasXY, len(datos), orden)
		valores = gaussJordan(ecuaciones, orden+1)
		printEcuacion(valores)
		

	if(option =="B" or option == "b"):
		datos = leerArchivo()
		orden = int(input("Por favor indique el orden polinomial: "))
		ordenAuto = calculaOrden(datos)
		if (orden <= ordenAuto):
			sumatoriasX, sumatoriasXY = calculaSumatorias(datos, orden)
			ecuaciones = calculaEcuaciones(sumatoriasX, sumatoriasXY, len(datos), orden)
			valores = gaussJordan(ecuaciones, orden+1)
			printEcuacion(valores)
		else:
			print("El orden seleccionado supera al limite posible, se ha utilizado el orden: ", ordenAuto)
			sumatoriasX, sumatoriasXY = calculaSumatorias(datos, ordenAuto)
			ecuaciones = calculaEcuaciones(sumatoriasX, sumatoriasXY, len(datos), ordenAuto)
			valores = gaussJordan(ecuaciones, ordenAuto+1)
			printEcuacion(valores)

