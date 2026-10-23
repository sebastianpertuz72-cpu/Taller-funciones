"""
Cree una función para pago semanal con horas extra. 

Es un modelo ficticio: las primeras 40 horas se pagan a la tarifa ordinaria; 

solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. 
Llame para dos personas y sume los retornos, 

sin redondearlos antes de sumar. 
Contrato: Pago semanal con horas extra: 
recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve el pago real semanal en pesos.

Fórmula o relación: Pago = horas × tarifa si horas ≤ 40; si horas > 40, pago = 40 × tarifa + (horas − 40) × tarifa × 1,5.

"""

def pago_semanal(horas, tarifa):
    if horas <= 40:
        return horas * tarifa
    else:
        return 40 * tarifa + (horas - 40) * tarifa * 1.5

horas1 = int(input("Persona 1, horas semanales: "))
tarifa1 = int(input("Persona 1, tarifa por hora: "))
horas2 = int(input("Persona 2, horas semanales: "))
tarifa2 = int(input("Persona 2, tarifa por hora: "))

pago1 = pago_semanal(horas1, tarifa1)
pago2 = pago_semanal(horas2, tarifa2)

totalpago = pago1 + pago2

print("Pagos:", pago1,"y", pago2,"pesos; total:", totalpago )

