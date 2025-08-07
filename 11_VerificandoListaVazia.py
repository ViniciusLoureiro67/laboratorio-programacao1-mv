#"id": 11,
#    "titulo": "Verificando se a Lista está Vazia",
#    "descricao": "Escreva uma função que receba uma lista e retorne 'True' se ela estiver vazia e 'False' caso contrário."

def esta_vazia(lista):
    return len(lista) == 0
# Verifica se a lista está vazia


lista1 = []
lista2 = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Lista 1 está vazia?", esta_vazia(lista1))  # True
print("Lista 2 está vazia?", esta_vazia(lista2))  # False
