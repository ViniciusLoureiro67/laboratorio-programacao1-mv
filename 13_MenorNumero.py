#     "id": 13,
#    "titulo": "Retornando o Menor Número",
#    "descricao": "Desenvolva uma função que receba uma lista de números e retorne o menor número encontrado nela."


def encontrar_menor(lista):
    menor = lista[0]  # Começamos assumindo que o primeiro número é o menor
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Maior número:", encontrar_menor(numeros))