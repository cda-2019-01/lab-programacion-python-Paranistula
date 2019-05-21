##
## Imprima la suma de la segunda columna.
##
file = open('data.csv', 'r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
data = []
for arr in file:
    for elemt in arr
    
suma_col = 0
for i in file:
    suma_col = suma_col + int(i[1])
print(suma_col)