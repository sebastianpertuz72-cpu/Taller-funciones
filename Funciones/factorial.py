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

n = int(input("Ingrese un numero mayor o igual a 0: "))
while n < 0:
    print("--> Error. El numero debe ser mayor que o igual que 0 \n")
    n = int(input("Ingrese un numero mayor o igual a 0"))

print(n, "!=", factorial(n))