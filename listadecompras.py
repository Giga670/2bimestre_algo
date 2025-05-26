reniciar=input("deseja fazer uma lista de compras? digite sim para isso ")
while reniciar=="sim":
    lista=[]
    opcao=input("deseja adicionar algun item na lista? ")
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
    opcao3=input("deseja remover um item da lista acima? ")
    if opcao3=="sim":
        while opcao3=="sim":
            lista.remove(input("digite o nome do item que quer remover: "))
            opcao3=input("digite não para parar ou sim para continuar: ")
    if len(lista)>0:
        print(f"essa é sua lista final {lista}")
    else:
        print("sua lista ficou vazia")
    reniciar=input("deseja fazer outra lista? digite sim para isso ")
print("obrigado por usar o fazedor de listas")