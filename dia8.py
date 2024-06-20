# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de 
# longitud variable (entre 8 y 16 caracteres) 
# que incluya letras mayúsculas, minúsculas, números y símbolos .

import secrets
import string

#definir alfabeto

numeros = string.digits
letras_mayusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase

caracteres_especiales = string.punctuation

alfabeto = (numeros + letras_minusculas + letras_mayusculas + caracteres_especiales)

#fijar la longitud de la contraseña
longitud_max = 16
longitud_min = 8


contrasenha = ''

contrasenha_usuario = int(input('Ingrese la cantidad de digitos para la contrasenha '))
if contrasenha_usuario < longitud_min or contrasenha_usuario > longitud_max:
    print ('Ingrese un numero entre 8 y 16')

    
else:
        contrasenha = ''.join(secrets.choice(alfabeto) for i in range (contrasenha_usuario))
        print ('contrasenha generada: ' , contrasenha)