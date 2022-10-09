#el usuario va a ingresar un numero y el programa le va a decir si ese numero es menor, mator  igual a un numero generado aleatoriamente 
#import permite importar modulos o archivos que  contienen funciones utiles
#random nos permire generar numeris aleatorios
import random

def adivina_el_numero(x):  # x va a ser el limite superior del intervalo de numeros a adivinar

    print("==============================")
    print("Bienvenida(o) al juego!")
    print("==============================")
    print("La meta es adivinar un numero generado por la computadora")
#numero entero aleatorio
# random.randint()  admite dos parametros (a, b)/ retorna un numero aleatorio entre a y b inclusive
    numero_aleatorio = random.randint(1, x)

    prediccion = 0 

    while prediccion != numero_aleatorio :  #while para repetir lo mismo un numero indeterminado de veces
        prediccion = int(input(f"adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("El numero es muy pequeño, vuelve a intentar")
        elif prediccion > numero_aleatorio: 
            print("El numero es muy grande, vuelve a intentar")     

    print(f"Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente.")


adivina_el_numero(10)

