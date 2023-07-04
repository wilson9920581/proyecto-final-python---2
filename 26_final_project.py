#Proyecto: crear y cargar dos matrices de 3x3, sumarlas y mostrar su suma.
# Proceso de diligenciamiento de la primera matriz
nFilas = int(input("Digite el número de filas de la primera matriz: "))
nCol = int(input("Digite el número de columnas de la primera matriz: "))

matriz = []
print("Digitando la primera matriz:")
for i in range(nFilas):
    fila = []
    for j in range(nCol):
        valor = int(input("Matriz [{}][{}]: ".format(i, j)))
        fila.append(valor)
    matriz.append(fila)

# Proceso de diligenciamiento de la segunda matriz
nFilas2 = int(input("Digite el número de filas de la segunda matriz: "))
nCol2 = int(input("Digite el número de columnas de la segunda matriz: "))

matriz2 = []
print("\nDigitando la segunda matriz:")
for i in range(nFilas2):
    fila = []
    for j in range(nCol2):
        valor = int(input("Matriz [{}][{}]: ".format(i, j)))
        fila.append(valor)
    matriz2.append(fila)

# Sumar las matrices
suma = [[0] * nCol for _ in range(nFilas)]
for i in range(nFilas):
    for j in range(nCol):
        suma[i][j] = matriz[i][j] + matriz2[i][j]

# Mostrar el resultado
print("\nLa suma de ambas matrices es:")
for fila in suma:
    for elemento in fila:
        print(elemento, end=" ")
    print()
