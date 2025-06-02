#tuplas são imutaveis e só podem ser alterado no código fonte ou utilizando indexação e slicing

#indexação e slicing são feranmentas fundamentais para acesar e manipular partes espesificas da tupla

numero= (5,8,12,8,7,8,3)
#definindo tupla
#para ser uma tupla precisa estar entre parentenses
print(f"tupla original: {numero}")
print(len(numero))
print(f" mostrando pelo indice {numero[2]}")
print(f" slicing do 2 ao 5 {numero[2:5]}")
print(f"quantas vezes o mumero oito repete {numero.count(8)}")
print(f"posição da primeira ocorrencia do numero 7: {numero.index(7)}")
minimo_tupla=min(numero)
print(f"mostra o menor numero:{minimo_tupla}")
maximo_tupla=max(numero)
print(f"mostra o maior numero {maximo_tupla}")
soma_tupla=sum(numero)
print(f"mostra a soma da tupla: {soma_tupla}")
print(f"o numero 4 esta na tupla? {4 in numero}")
numero2=(15,20)
tupla_concatenada=numero+numero2
print(f"a concatenação das tuplas 1 e 2 resulta na nova tupla: {tupla_concatenada}")
tupla_duplicada=numero*2
print(tupla_duplicada)