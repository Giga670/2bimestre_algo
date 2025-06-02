enviados=0
transito=0
recebido=0
codigos_transito=[]
pacotes=( ("abc123","enviado"), ("def345", "em transito"), ("xyz789", "recebido"), ("jkl321", "enviado"), ("mno654", "recebido"), ("pqr987", "em transito"), ("stu741", "enviado"))
for i in range(0, len(pacotes)):
    if "enviado" in pacotes[i]:
        enviados=enviados+1
    if "em transito" in pacotes[i]:
        transito=transito+1
        codigos_transito.append(pacotes[i][0])
    if "recebido" in pacotes[i]:
        recebido=recebido+1
print(f"estão em enviados {enviados} pacotes")
print(f"estão em transito {transito} pacotes")
print(f"foram recebidos {recebido} pacotes")
print(f"os codigos que estão em transito são: {codigos_transito}")
def retorno(valor):
    for i in range(0, len(pacotes)):
        if valor in pacotes[i]:
            print(pacotes[i][1])
cod = input("insira o código: ")
retorno(cod)
ordenada=sorted(pacotes)
print(ordenada)

    