cadena = input('Ingrese una frase: ')

lista = []

for i in cadena:
    vocales = ('a', 'e', 'i', 'o', 'u')
    if i in vocales:
       lista.append (i)
print (lista)
cantidad_de_vocales = len(lista)
print (cantidad_de_vocales)

