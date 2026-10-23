def sumar(num1: int, num2: int) -> int:
    resultado = num1 + num2
    return resultado

def restar(num1: int, num2: int) -> int:
    resultado = num1 - num2
    return resultado

def multiplicar(num1: int, num2: int) -> int:
    resultado = num1 * num2
    return resultado

def dividir(num1: int, num2: int) -> int:
    resultado = num1 // num2
    return resultado

def modulo(num1: int, num2: int) -> int:
    resultado = num1 % num2
    return resultado

def factorial(num):
    if num < 0:
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for n in range(2, num+1):
            fact *= n # es lo mismo fact = fact * n
        return fact

def combinatoria(n, k):
    if n < 0 or k < 0 or (n-k) < 0:
        return None
    else:
        combi = factorial(n) / (factorial(k) * factorial(n-k))
        return combi

def menu():
    print(
"""
*** MENU ***
1. Sume dos numeros
2. Reste dos numeros
3. Multiplique dos numeros
4. Divida dos numeros
5. Calcule el modulo dos numeros
6. Calcule le factorial de un numero
7. Calcule la combinatoria
8. Salir
""")

def leerOpcion():
    opcion = input(">>>Opcion? ")
    while opcion < "1" or opcion > "8":
        print("--> Error. Opción no válida.")
        input("Presione enter para continuar ....")
        print("\n\n\n\n\n")
        menu()
        opcion = input(">>>Opcion? ")

    return int(opcion)

def opcion_sumar():
    print("\n\n\n 1. SUMAR DOS NUMEROS")

    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))

    print("El resultado de la suma es: ", sumar(num1, num2))

def opcion_restar():
    print("\n\n\n 2. RESTAR DOS NUMEROS")

    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))

    print("El resultado de la resta es: ", restar(num1, num2))

def opcion_multiplicar():
    print("\n\n\n 3. MULTIPLICAR DOS NUMEROS")

    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))

    print("El resultado de la multiplicacion es: ", multiplicar(num1, num2))

def opcion_dividir():
    print("\n\n\n 4. DIVIDIR DOS NUMEROS")

    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))

    print("El resultado de la suma es: ", dividir(num1, num2))

def opcion_modulo():
    print("\n\n\n 5. CALCULAR EL MODULO DE DOS NUMEROS")

    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))
    
    print(num1, "%", num2,"=", modulo(num1, num2))

def opcion_factorial():
    print("\n\n\n 6. CALCULAR EL FACTORIAL")

    num1 = int(input("Ingrese un numero "))
    
    print(num1, "!=", factorial(num1))

def opcion_combinatoria():
    print("\n\n\n 7. CALCULAR COMBINATORIA")

    num1 = int(input("n? "))
    num2 = int(input("k? "))
    
    print("C(", num1, ",", num2, ")=", combinatoria(num1, num2))



### Programa principal
while True:
    menu()
    opcion = leerOpcion()
    match opcion:
        case 1:
            opcion_sumar()
        case 2:
            opcion_restar()
        case 3:
            opcion_multiplicar()
        case 4:
            opcion_dividir()
        case 5:
            opcion_modulo()
        case 6:
            opcion_factorial()
        case 7:
            opcion_combinatoria()
        case 8:
            print("Gracias por usar la calculadora...")
            break

    input("Presione Enter para continuar...")