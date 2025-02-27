# Versão sem List Comprehension
quadrados_sem = []
for num in range(1, 11):
    quadrados_sem.append(num ** 2)

# Versão com List Comprehension
quadrados_com = [num ** 2 for num in range(1, 11)]

print("Quadrados sem List Comprehension:", quadrados_sem)
print("Quadrados com List Comprehension:", quadrados_com)

# Exemplo 2: Filtrar apenas os números pares de uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Versão sem List Comprehension
pares_sem = []
for num in numeros:
    if num % 2 == 0:
        pares_sem.append(num)

# Versão com List Comprehension
pares_com = [num for num in numeros if num % 2 == 0]

print("Pares sem List Comprehension:", pares_sem)
print("Pares com List Comprehension:", pares_com)
