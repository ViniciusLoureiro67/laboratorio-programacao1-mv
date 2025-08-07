#"id": 10,
#    "titulo": "Removendo Duplicatas",
#    "descricao": "Elabore uma função que receba uma lista com valores possivelmente duplicados e retorne uma nova lista contendo apenas os valores únicos, sem repetições."

def remover_duplidos(lista):
    # Transforma a lista em um set (remove duplicados), depois volta pra lista
    unicos = list(set(lista))
    return unicos

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

print("Lista sem duplicatas:", remover_duplidos(numeros))