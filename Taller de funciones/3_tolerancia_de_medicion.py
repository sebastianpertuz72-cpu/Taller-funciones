"""
Cree las funciones necesarias para tolerancia de una medición. 
Debe reutilizar una función de valor absoluto que recibe un real y devuelve su distancia al cero. 
Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. 
El escenario consulta dos mediciones por separado. 
Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no negativo. 
Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
Fórmula o relación: Error = valor absoluto de (medición − objetivo); aceptable cuando error ≤
tolerancia.

"""
def valor_total(valor):
    if valor < 0:
        return -valor
    else:
        return valor

def aceptacion(medicion, objetivo, tolerancia):
    error = valor_total(medicion - objetivo)
    return error <= tolerancia

objetivo = float(input("Ingrese el objetivo: "))
tolerancia = float(input("Ingrese la tolerancia: "))

medicion1 = float(input("Ingrese la primera medicion: "))
medicion2 = float(input("Ingrese la segunda medicion: "))

aceptacion1 = aceptacion(medicion1, objetivo, tolerancia)
aceptacion2 = aceptacion(medicion2, objetivo, tolerancia)


if aceptacion1:
    primera = "verdadero"
else:
    primera = "falso"

if aceptacion2:
    segunda = "verdadero"
else:
    segunda = "falso"

print("Aceptables:", primera , ";", segunda)




