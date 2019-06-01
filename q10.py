##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
# Guarda cada linea del archivo como elemento de una lista
file = open('data.csv', 'r').readlines()

# Quitamos el ultimo caracter de cada elemento
file = [row[0:-1] for row in file]

# Separa los caracteres por tabulacion
file = [row.split('\t') for row in file]

data = []
i = 0
for elemt in file:
	data.append([])
	for e in elemt:
		a = e.split(',')
		if(len(a) == 1):
			data[i].append(a[0])
		else:
			data[i].append(a)
	i += 1

result = {}

for element in data:
	for el in element[4]:
		aux = el.split(':')
		result[aux[0]] = 0

for element in data:
	for el in element[4]:
		aux = el.split(':')
		result[aux[0]] += 1

for e in sorted(result):
	print(e + ',' + str(result[e]))