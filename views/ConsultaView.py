from termcolor import colored, cprint

from controllers.ConsultaController import ConsultaController
from util.message import menu
from views.AtendimentoPacienteView import AtendimentoPacienteView


def consultaView(consultaController: ConsultaController):        
    print()
    cprint("************************", "green")
    menu("Digite os números correspondentes no menu para realizar as operações")
    print("1- Listar as consultas")
    print("2- Criar consulta")
    print("3- Atualizar consulta")
    print("4- Deletar consulta")
    print("0- Sair")
    cprint("************************", "green")
    opcao = int(input())

    match opcao:
        case 1:
            listar_consultas(consultaController)
        case 2:
            ...

        case _:
            return

    
def listar_consultas(consultaController: ConsultaController):
    consultas = consultaController.listarConsultas()
    for consulta in consultas:
        cprint(f"CPF do paciente: {consulta[0]} - Nome do paciente: {consulta[1]} - CRM do médico: {consulta[2]} - Nome do medico: {consulta[3]} - Especializacao: {consulta[4]}", "blue")
    
def criar_consulta():
    atendimento = AtendimentoPacienteView()



# def consulta(cpf):
#     cprint("************************", "green")
#     print("Escolha a especialização que deseja consultar:")
#     especializacoes = especializacaoController.listarEspecializacoes()
    
#     for esp in especializacoes:
#         tipo_esp = colored(esp[0], "blue")
#         print(f"{esp[1]}- {tipo_esp}")
#     codigo_especializacao = int(input("Qual o código da especializacao: "))
#     medicos_disponiveis = medicoController.listarMedicosPelaEspecializacao(codigo_especializacao)
#     print(medicos_disponiveis)
#     for medico in medicos_disponiveis:
#         print(f"CRM: {medico[0]} - Nome: {medico[1]} - Telefone: {medico[2]} - Endereço: {medico[3]} - Especialização: {medico[4]}")
    
#     crm_medico = input("Qual o CRM do médico escolhido: ")
#     valor = float(input("Digite o valor da consulta: "))
#     plano_saude = input("É plano de saúde? s/n")
#     eh_plano_saude = 1 if plano_saude == 's' else 0

#     return [cpf, crm_medico, valor, eh_plano_saude]