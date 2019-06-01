##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
# Guarda cada linea del archivo como elemento de una lista
file = open('data.csv', 'r').readlines()

# Quitamos el ultimo caracter de cada elemento
file = [row[0:-1] for row in file]

# Separa los caracteres por tabulacion
file = [row.split('\t') for row in file]
data = file

result = {}

for element in data:
	result[element[0]] = []

for element in data:
	result[element[0]].append(int(element[1]))

# print result

for key in sorted(result.keys()):  
     print(key + ',' + str(max(result[key])) + ',' + str(min(result[key])))