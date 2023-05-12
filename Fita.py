total = float(input("Digite um número: "))
while True:
    operacao = (input("Digite uma das quatro operações da matemática ou '=' para finalizar: "))
    if(operacao == '='):
        break
    elif(operacao == '+'):
        numero = float(input("Digite um número: "))
        total += numero
    elif(operacao == '-'):
        numero = float(input("Digite um número: "))
        total -= numero
    elif(operacao == 'x'):
        numero = float(input("Digite um número: "))
        total *= numero
    elif(operacao == '/'):
        numero = float(input("Digite um número: "))
        total /= numero
print(f"Resultado: {total}")