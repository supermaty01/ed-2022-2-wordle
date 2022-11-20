import words
from random import choice

cantidad_letras = input()
palabra_escogida = choice(words.palabras_dict[cantidad_letras])
cantidad_intentos = 0

# Ingresar palabra
def ingresar_palabra(palabra_ingresada):
    resultados_palabra = []
    contador_amarillas = {}
    for i in range(int(cantidad_letras)):
        if palabra_ingresada[i] in palabra_escogida:
            if palabra_escogida[i] == palabra_ingresada[i]:
                resultados_palabra.append('verde')
            else:
                if palabra_ingresada[i] not in contador_amarillas:
                    contador_amarillas[palabra_ingresada[i]] = 1
                    resultados_palabra.append('amarillo')
                elif contador_amarillas[palabra_ingresada[i]] < palabra_escogida.count(palabra_ingresada[i]):
                    contador_amarillas[palabra_ingresada[i]] += 1
                    resultados_palabra.append('amarillo')
                else:
                    resultados_palabra.append('gris')
        else:
            resultados_palabra.append('gris')
    return resultados_palabra

def jugar():
    palabra_ingresada = input()
    cantidad_intentos += 1
    if len(palabra_ingresada) != int(cantidad_letras):
        raise Exception()
    if palabra_ingresada not in words.palabras_set:
        raise Exception()
    if palabra_ingresada == palabra_escogida:
        # Gano
        print('El jugador gano')
    else:
        resultado = ingresar_palabra(palabra_ingresada)
        if cantidad_intentos == 6:
            print('El jugador perdio')
        

print(ingresar_palabra())