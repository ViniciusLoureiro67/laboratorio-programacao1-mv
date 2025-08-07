# "id": 14,
# "titulo": "Calculando a Média"
# "descricao": "Crie uma função que receba uma lista de números e retorne a média aritmética desses valores."

def calcular_media(lista):  
    if len(lista) == 0:     # Se a lista estiver vazia, evitamos divisão por zero
        return 0            # Retornamos 0
    
    soma = sum(lista)       # soma todos os valores da lista com a função 'sum'
    quantidade = len(lista) # usa 'len' para contar quantos itens tem na lista
    media = soma / quantidade  # divide a soma pela quantidade
    return media            # retornamos o valor final da média

# Exemplo de uso:
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

print("Média:", calcular_media(numeros))
