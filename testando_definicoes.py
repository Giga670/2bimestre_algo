#testando definições
#listas:
compras = ["pao","cafe","leite"]
print(compras)

#pode ser removido pelo nome ou pelo indice
#compras.remove("cafe")
compras.remove(compras[0])
print(compras)

#append acreçenta um item ao final da lista, só pode adicionar um por vez
compras.append("açucar")
print(compras)

#é preciso criar uma lista nova para receber os elementos ordenados
compras_ordenadas=sorted(compras)
print(compras_ordenadas)

#o nome item é um identificador dos itens dentro da lista, podendo receber qualquer nome
for item in compras:
    print(f"-{item}")
