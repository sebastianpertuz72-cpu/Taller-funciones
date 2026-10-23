"""
Cree una función para precio unitario comparable.

 Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. 

Llame para dos paquetes y use los retornos para indicar el más económico por gramo; 
si coinciden indique igualdad. 

Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.


Fórmula o relación: Precio por gramo = precio total / cantidad de gramos.

"""

def  division (a, b):
    if (a or b) < 0:
        return None
    else:
        resultado = a // b
        return resultado

gram1 = int(input("Ingrese la cantidad de gramos del primer paquete"))
precio1 = int(input("Ingrese el valor del primer paquete"))

precioxgramo1 = division(precio1,gram1)

gram2 = int(input("Ingrese la cantidad de gramos del segundo paquete"))
precio2 = int(input("Ingrese el valor del segundo paquete"))

precioxgramo2 = division(precio2,gram2)

if precioxgramo1 == precioxgramo2:
    print("Ambos tienen el mismo precio por gramo, por ende queda elegir dependiendo de gustos.", precioxgramo1, precioxgramo2)

elif precioxgramo1 == None:
    print("Precio por gramo:",precioxgramo1, "pesos; conviene mas el primer paquete" )

elif precioxgramo2 == None:
    print("Precio por gramo:",precioxgramo2,"pesos; conviene mas el primer paquete" )

elif precioxgramo1 < precioxgramo2:
    print("Precio por gramo:",precioxgramo1, "y", precioxgramo2, "pesos; conviene mas el primer paquete" )

else:
    print("Precio por gramo:",precioxgramo1, "y", precioxgramo2, "pesos; conviene mas el segundo paquete")