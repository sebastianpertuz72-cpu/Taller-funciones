"""
Ejemplo: realizar unas funciones que realicen suma, resta, multiplicacion y division

Sintaxis funcion python

def nombre_funcion(parametro1[:str]), parametro2[int], . . ., parametroN[:str][-> int]:
    cuerpo funcion
    [return valor_devuelto]
"""

def  suma (a, b):
    resultado = a + b
    return resultado

def  resta (a, b):
    resultado = a - b
    return resultado


def  multiplicacion (a, b):
    resultado = a * b
    return resultado


def  modulo (a, b):
    resultado = a % b
    return resultado

def  division (a, b):
    resultado = a // b
    return resultado



valor1 = int(input("Ingrese un numero para sumar: "))
valor2 = int(input("Ingrese otro numero para sumar: "))

valor3 = int(input("Ingrese un numero para restar: "))
valor4 = int(input("Ingrese otro numero para restar: "))

valor5 = int(input("Ingrese un numero para multiplicar: "))
valor6 = int(input("Ingrese otro numero para multiplicar: "))

valor7 = int(input("Ingrese un numero para modular: "))
valor8 = int(input("Ingrese otro numero para modularar: "))

valor9 = int(input("Ingrese un numero para dividir: "))
valor10 = int(input("Ingrese otro numero para dividir: "))

resultado_suma = suma(valor1, valor2)

resultado_resta = resta(valor3, valor4)

resultado_multiplicacion = multiplicacion(valor5, valor6)

resultado_modulo = modulo(valor7, valor8)

resultado_division = division(valor9, valor10)


print("El resultado de la suma es: ", resultado_suma)

print("El resultado de la resta es: ", resultado_resta)

print("El resultado de la multiplicacion es: ", resultado_multiplicacion)

if valor8 != 0:
    print("El resultado de la modulacion es: ", resultado_modulo)

if valor10 != 0:
    print("El resultado de la division es: ", resultado_division)


