##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
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
	result[element[0]] = result[element[0]] + int(element[1])

for key in sorted(result.keys()):  
     print(key + ',' + str(result[key]))