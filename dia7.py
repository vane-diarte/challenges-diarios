import random
opciones = ['piedra', 'papel', 'tijera']

def juego (jugador, computadora):
    

    if jugador == computadora:
        return 'Empate'
    
    if jugador == 'piedra':
        if computadora == 'papel':
            return 'Computadora gana'
        else:
            return 'Jugador gana'
        
    if jugador == 'papel':
        if computadora == 'tijera':
            return 'Computadora gana'
        else:
            return 'Jugador gana'
        
    if jugador == 'tijera':
        if computadora == 'piedra':
            return 'Computadora gana'
        else:
            return 'Jugador gana'
        
def jugar():
    print ('Juega piedra, papel o tijera')
    jugador = input ('Ingrese "piedra", "papel" o "tijera" para jugar: ').lower()
    computadora = random.choice(opciones)

    resultado = juego(jugador, computadora)
    print (f'Jugador elige: {jugador}')
    print (f'Computadora elige: {computadora}')
    return resultado

resultado_del_juego = jugar()
print (resultado_del_juego)





        
    

        
    