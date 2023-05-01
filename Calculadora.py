operacao = input("Escolha uma operção matemática: ")
num1 = int(input("Agora digite um valor: "))
num2 = int(input("Agora digite um valor: "))

soma = num1+num2
menos = num1-num2
divisao = num1/num2
multiplicacao = num1*num2

if operacao == "soma":
    print(soma)
elif operacao == "menos":
    print(menos)
elif operacao == "divisao":
    print(divisao)
else:
    print(multiplicacao)
