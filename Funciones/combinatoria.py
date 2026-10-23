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
    if k < 0 or n < 0 or (n-k) < 0:
        return None
    else:
        combi = factorial(n) / (factorial(k) * factorial(n-k))
        return combi

valor_n = int(input("Valor de n? "))
valor_k = int(input("Valor de k? "))

print("C(", valor_n, ",", valor_k, ")= ", combinatoria(valor_n,valor_k))