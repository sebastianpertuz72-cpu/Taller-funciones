"""
Ejemplo: realizar una funcion que sume dos numeros

Sintaxis funcion python

def nombre_funcion(parametro1[:str]), parametro2[int], . . ., parametroN[:str][-> int]:
    cuerpo funcion
    [return valor_devuelto]
"""

def  suma (a, b):
    resultado = a + b
    return resultado

valor1 = int(input("Ingrese un numero: "))
valor2 = int(input("Ingrese un numero: "))

resultado_suma = suma(valor1, valor2)
print("El resultado de la suma es: ", resultado_suma)


