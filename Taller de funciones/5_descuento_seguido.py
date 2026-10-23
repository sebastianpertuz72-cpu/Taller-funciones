"""
Cree las funciones necesarias para descuento seguido de impuesto ficticio. 
El descuento se calcula sobre la base. 
El impuesto se calcula sobre el subtotal ya descontado, no sobre la base original. 
Son reglas ficticias, no normas tributarias. 
El escenario pasa el retorno del descuento a la función de impuesto y muestra subtotal y total. 
Contratos en orden de parámetros: 
Subtotal descontado: recibe base real no negativa en pesos, descuento real de 0 a 100 por ciento y devuelve real no negativo en pesos. 
Total con impuesto: recibe subtotal real no negativo en pesos, impuesto real no negativo por ciento y devuelve real no negativo en pesos.

Fórmula o relación: Subtotal = base × (1 − descuento / 100); total = subtotal × (1 + impuesto / 100).

Cada porcentaje se divide por 100.

"""


def subtotal_descontado(base, descuento):
    return base * (1 - descuento / 100)


def total_con_impuesto(subtotal, impuesto):
    return subtotal * (1 + impuesto / 100)


base = int(input("Ingrese la base en pesos: "))
descuento = int(input("Ingrese el descuento en %: "))
impuesto = int(input("Ingrese el impuesto en %: "))

subtotal = subtotal_descontado(base, descuento)
total = total_con_impuesto(subtotal, impuesto)

print("Subtotal:", subtotal , "; total:", total, "pesos")
