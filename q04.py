##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
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
	result[(element[2].split('-')[1])] = 0

for element in data:
	result[(element[2].split('-')[1])] = result[(element[2].split('-')[1])] + 1

for key in sorted(result.keys()):  
     print(key + ',' + str(result[key]))