#"id": 12,
#    "titulo": "Juntando Duas Listas",
#    "descricao": "Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas."

def recebe_duas(lista1,lista2):
    lista3 = lista1 + lista2  # Concatena as duas listas
    return lista3

listaexemplo1 = ["test1", "test2"]
listaexemplo2 = ["test3", "test4"]

print("A lista concatenada fica:", recebe_duas(listaexemplo1, listaexemplo2))