numero_1 = int(input('Ingerese un numero: '))
numero_2 = int(input('Ingerese otro numero: '))
numero_3 = int(input('Ingerese otro numero: '))

def ordenar_numeros():
    numeros = [numero_1, numero_2, numero_3]
    numeros.sort()
    return (numeros)

numeros_ordenados = ordenar_numeros()
print (f"Los numeros en orden ascendentes son: {numeros_ordenados}")
