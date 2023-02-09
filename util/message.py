
from termcolor import colored, cprint

mensagem = '''
Bem-vindo ao Sistema Hospitalar! 🏥
Esperamos que você tenha uma boa experiência.
Se precisar de ajuda, por favor, não hesite em perguntar.'''

msg = colored(mensagem, "red", attrs=["bold", "underline"])

def msg_bd_connection(msg):
    cprint(msg, "yellow")

def msg_bd_error(msg):
    msg = colored(msg, "red", attrs=["bold", "reverse"])
    print(msg)

def boas_vindas():
    cprint(msg)

def menu(msg):
    msg = colored(msg, "green", attrs=["bold"])
    print(msg)

def atendimento():
    print()
    cprint("************************", "green")
    menu("Digite os números correspondentes no menu para realizar as operações")
    print("1- Paciente")
    print("2- Médico")
    print("3- Consulta")
    print("0- Sair")
    cprint("************************", "green")




def atendimento_paciente():
    print("1- Marcar consulta")
    print("2- Ver os seus dados")
    print("3- Atualizar seus dados")
    print("4- Deletar cadastro")
    print("5- Voltar")