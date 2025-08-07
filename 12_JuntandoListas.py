#"id": 12,
#    "titulo": "Juntando Duas Listas",
#    "descricao": "Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas."

def recebe_duas(lista1,lista2):
    lista3 = lista1 + lista2  # Concatena as duas listas
    return lista3

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

print("A lista concatenada fica:", recebe_duas(natureza, tecnologia))