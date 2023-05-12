Operacao = float(input("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\nPara escolher a operação digite o número de acordo com a lista: "))

a = float(input("Digite o primeiro número: "))

b = float(input("Digite o segundo número: "))

if(Operacao == 1):
    print(a+b)
elif(Operacao == 2):
    print(a-b)
elif(Operacao == 3):
    print(a*b)
elif(Operacao == 4):
    print(a/b)