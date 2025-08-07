# "id": 3
# "titulo": "Encontrando o Segundo Maior Número"
# "descricao": "Crie uma função que retorne o segundo maior número de uma lista. Considere que a lista pode ter números duplicados."

def segundo_maior(lista):
    # Remove duplicados usando set, depois colocamos como lista novamente
    numeros_unicos = list(set(lista))

    # Verifica se tem pelo menos dois números diferentes, pois se não tem pelo menos 2 números, como saberemos o segundo maior?
    if len(numeros_unicos) < 2:
        return None  

    # Ordena a lista do maior para o menor 
    numeros_unicos.sort(reverse=True)

    # Retorna o segundo item (posição 1)
    return numeros_unicos[1]


numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

print("Segundo maior número:", segundo_maior(numeros))
