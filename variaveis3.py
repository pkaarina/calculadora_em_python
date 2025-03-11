import sys


numero_um = input('digite o numero um: ')
try:
    numero_um_convertido = float(numero_um)
except ValueError:
    print("Erro: a string não pode ser convertida em número")
    sys.exit()

numero_dois = input('digite o numero dois: ')
try:
    numero_dois_convertido = float(numero_dois)
except ValueError:
    print("Erro: a string não pode ser convertida em número")
    sys.exit()

operacao=input("digite:\n\t+ para somar\n\t* para multiplicar\n\t- para subtrair\n\te / para dividir\n")


if operacao == "+":
    print ("a operação escolhida foi: soma")
    print ("o resultado da soma é: ",numero_um_convertido+numero_dois_convertido)
elif operacao == "*":
    print ("a operação escolhida foi: multiplição")
    print ("o resultado da multiplicação é: ",numero_um_convertido*numero_dois_convertido)
elif operacao == "-":
    print ("a operação escolhida foi: subtração")
    print ("o resultado da subtração é:",numero_um_convertido-numero_dois_convertido)
elif operacao == "/":
    if numero_dois_convertido == 0:
        print ("Erro: Não é possível dividir por 0.")
        sys.exit()
    print ("a operação escolhida foi: divisão")
    print ("o resultado da divisão é:", numero_um_convertido/numero_dois_convertido)
else: 
    print ("operação inválida, digitar -, +, * ou /")

print ("\nobrigada por utilizar nossos serviços :)\n")