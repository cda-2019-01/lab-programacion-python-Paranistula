##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

# Guarda cada linea del archivo como elemento de una lista
file = open('data.csv', 'r').readlines()

# Quitamos el ultimo caracter de cada elemento
file = [row[0:-1] for row in file]

# Separa los caracteres por tabulacion
file = [row.split('\t') for row in file]
data = file
# print data

result = {}

for element in data:
	result[element[0]] = 0

for element in data:
	result[element[0]] = result[element[0]] + 1

for key in sorted(result.keys()):  
     print(key + ',' + str(result[key]))