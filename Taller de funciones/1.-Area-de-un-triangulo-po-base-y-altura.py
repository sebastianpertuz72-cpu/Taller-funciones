"""
Cree una función para área de un triángulo por base y altura. 
La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. 
Contrato: Área de un triángulo por base y altura:
recibe base y altura, reales positivos expresados en centímetros y devuelve el área real en centímetros cuadrados.

Fórmula o relación: Área = base × altura / 2. La división entre 2 obtiene la mitad del rectángulo de
igual base y altura.


"""

def area_de_un_triangulo(base, altura):
    if base < 0 or altura < 0:
        return None
    else:
        return base * altura // 2

def  suma (a, b):
    resultado = a + b
    return resultado

base1 = int(input("Digite la base: "))
altura1 = int(input("Digite la altura: "))

area1 = area_de_un_triangulo(base1, altura1)

base2 = int(input("Digite la base: "))
altura2 = int(input("Digite la altura: "))

area2 = area_de_un_triangulo(base2, altura2)

areatot = suma(area1, area2)

print("Areas: ", area1, "y", area2, "cm²; suma:", areatot,"cm²")
