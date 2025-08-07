#"id": 4,
#    "titulo": "Encontrando os Números Pares",
#    "descricao": "Desenvolva uma função que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números pares."


def encontrar_pares(lista):
    # Lista vazia para guardar os números pares encontrados
    pares = []

    # Para cada número dentro da lista recebida
    for item in lista:
        # Se o número for divisível por 2
        if item % 2 == 0:
            pares.append(item)  # adiciona à lista de pares

    return pares  # devolve a nova lista com apenas os pares


numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999,
           5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Números pares:", encontrar_pares(numeros))
