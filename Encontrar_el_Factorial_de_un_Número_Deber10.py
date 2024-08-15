def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print("Factorial de 0 es:", factorial(0))  
print("Factorial de 1 es:", factorial(1))  
print("Factorial de 5 es:", factorial(5))  
print("Factorial de 7 es:", factorial(7))  
print("Factorial de 4 es:", factorial(4))  
print("Factorial de 2 es:", factorial(2))  