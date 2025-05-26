lista=[]
opcao="sim"
while opcao=="sim":
    listat=input("digite um item: ")
    lista.append(listat)
    opcao=input("digite não para parar ou sim para continuar: ")
opcao2=input("deseja adicionar um item? ")
if opcao2=="sim":
    while opcao2=="sim":
        listat=input("digite um item: ")
        lista.append(listat)
        opcao2=input("digite não para parar ou sim para continuar: ")
print(lista)
opcao3=input("deseja remover um item da lista acima")
if opcao3=="sim":
    lista.remove(input("digite o nome do item que quer remover"))
print(f"essa é sua lista final {lista}")