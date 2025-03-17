import sys
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.LIGHTBLUE_EX}
#   ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗  
#  ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗ 
#  ██║     ███████║██║     ██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║ 
#  ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║ 
#  ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║ 
#   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ 
{Style.RESET_ALL}
{Fore.LIGHTBLUE_EX}Calculadora em Python - by Karina Ferreira {Style.RESET_ALL}
"""
    print(banner)

print_banner()

numero_um = input(f'{Fore.LIGHTMAGENTA_EX}digite o numero um: ')
try:
    numero_um_convertido = float(numero_um)
except ValueError:
    print(f"{Fore.LIGHTRED_EX}Erro: a string não pode ser convertida em número")
    sys.exit()

numero_dois = input(f'{Fore.LIGHTMAGENTA_EX}digite o numero dois: ')
try:
    numero_dois_convertido = float(numero_dois)
except ValueError:
    print(f"{Fore.LIGHTRED_EX}Erro: a string não pode ser convertida em número")
    sys.exit()

operacao=input(f"{Fore.LIGHTMAGENTA_EX}digite:\n\t+ para somar\n\t* para multiplicar\n\t- para subtrair\n\te / para dividir\n")


if operacao == "+":
    print (f"{Fore.LIGHTRED_EX}a operação escolhida foi: soma")
    print (f"{Fore.LIGHTRED_EX}o resultado da soma é: {numero_um_convertido+numero_dois_convertido}")
elif operacao == "*":
    print (f"{Fore.LIGHTRED_EX}a operação escolhida foi: multiplição")
    print (f"{Fore.LIGHTRED_EX}o resultado da multiplicação é: {numero_um_convertido*numero_dois_convertido}")
elif operacao == "-":
    print (f"{Fore.LIGHTRED_EX}a operação escolhida foi: subtração")
    print (f"{Fore.LIGHTRED_EX}o resultado da subtração é: {numero_um_convertido-numero_dois_convertido}")
elif operacao == "/":
    if numero_dois_convertido == 0:
        print (f"{Fore.LIGHTRED_EX}Erro: Não é possível dividir por 0.")
        sys.exit()
    print (f"{Fore.LIGHTRED_EX}a operação escolhida foi: divisão")
    print (f"{Fore.LIGHTRED_EX}o resultado da divisão é: {numero_um_convertido/numero_dois_convertido}")
else: 
    print (f"{Fore.LIGHTRED_EX}operação inválida, digitar -, +, * ou /")

print (f"{Fore.LIGHTRED_EX}\nobrigada por utilizar nossos serviços :)\n")