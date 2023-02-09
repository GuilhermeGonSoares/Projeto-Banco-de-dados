from termcolor import colored, cprint

from controllers.ConsultaController import ConsultaController
from controllers.EspecializacaoController import EspecializacaoController
from controllers.MedicoController import MedicoController


class AtendimentoPacienteView:

    def __init__(self, pacienteController, especializacaoController: EspecializacaoController, medicoController: MedicoController, consultaController: ConsultaController):
        self.pacienteController = pacienteController
        self.especializacaoController = especializacaoController
        self.medicoController = medicoController
        self.consultaController = consultaController
        self.atendimento_ao_cliente()
     

    def opcoes_atendimento_paciente(self):
        print()
        cprint("************************", "green")
        print(colored("Digite os números correspondentes no menu para realizar as operações", "green", attrs=["bold"]))
        print("1- Consulta")
        print("2- Ver os seus dados")
        print("3- Atualizar seus dados")
        print("4- Deletar cadastro")
        print("5- Voltar")
        cprint("************************", "green")


    def atendimento_ao_cliente(self):
        continuar = True
        while continuar:
            print()
            cprint("************************", "green")
            print(colored("Digite os números correspondentes no menu para realizar as operações", "green", attrs=["bold"]))
            print("1- Acessar paciente")
            print("2- Cadastrar paciente")
            print("3- Todos pacientes")
            print("4- Voltar")
            cprint("************************", "green")

            op = int(input())

            if op == 1:
                gerenciar = True
                cpf = input("Digite o seu CPF(válido) para realizar a consulta por favor: ")
                while gerenciar:
                    gerenciar = self.gerenciar_paciente(cpf)
            elif op == 2:
                cadastro_valido = False
                while not cadastro_valido:
                    cadastro_valido = self.cadastrar_paciente()
            elif op == 3:
                pacientes = self.pacienteController.listarPacientes()
                for paciente in pacientes:
                    cprint(self.formatar_dados_paciente(paciente), "yellow")

            else:
                continuar = False
     
    def gerenciar_paciente(self, cpf):
        paciente = self.pacienteController.findPaciente(cpf)    
    
        if not paciente:
            cprint("CPF inválido ou não cadastrado", "red")
            return False

        
        cprint(f"Bem-vindo {paciente[1]}! Estamos a sua disposiçao", "blue")
        self.opcoes_atendimento_paciente()
        paciente_opcoes = int(input())
        
        if paciente_opcoes == 1:
            dados = self.consulta(cpf)
            consulta = self.consultaController.criarConsulta(dados)
            print(consulta)
            return True

        if paciente_opcoes == 2:
            cprint(self.formatar_dados_paciente(paciente), "yellow")
            return True
        if paciente_opcoes == 3:
            dados = self.novos_dados()
            paciente = self.pacienteController.atualizarPaciente(cpf, dados)
            cprint(self.formatar_dados_paciente(paciente), "yellow")
            cprint(f"PACIENTE {paciente[0]} ATUALIZADO COM SUCESSO!", "blue")
            return True
        if paciente_opcoes == 4:
            print()
            cprint("************************", "green")
            print("Certeza que deseja excluir o seu cadastro? ")
            print("1- Sim")
            print("2- Não")
            cprint("************************", "green")

            quer_deletar = int(input())
            if quer_deletar != 1:
                return True
            paciente = self.pacienteController.deletarPaciente(cpf)
            cprint(f"Pacience CPF: {paciente[0]} deletado com sucesso", "yellow")
            return False
        if paciente_opcoes == 5:
            return False


    def cadastrar_paciente(self):
        
        cpf_valido = False
        msg_cpf = "CPF:"
        while not cpf_valido:
            novo_cpf = input(f"{msg_cpf} ")
            if len(novo_cpf) != 11:
                msg_cpf = "CPF inválido! CPF precisa ter 11 dígitos"
                cpf_valido = False
            else:
                cpf_valido = True

        dados = self.novos_dados()

        dados.insert(0, novo_cpf)
        paciente = self.pacienteController.criarPaciente(dados)
        if not paciente:
            return False
        cprint("Paciente cadastrado com sucesso", "green")
        cprint(self.formatar_dados_paciente(paciente), "yellow")
        return True

    def formatar_dados_paciente(self,paciente):
        return f'''
        CPF: {paciente[0]}
        NOME COMPLETO: {paciente[1]}
        ENDERECO: {paciente[2]}
        TELEFONE: {paciente[3]}
        '''
    def novos_dados(self):
        cprint("Forneça os valores:", "green")
        
        telefone_valido = False
    
        
        novo_nome = input("NOME: ")
        novo_endereco = input("ENDERECO: ")

        msg_telefone= "TELEFONE:"
        while not telefone_valido:
            novo_telefone = input(f"{msg_telefone} ")
            if len(novo_telefone) > 20:
                msg_cpf = "TELEFONE inválido! TELEFONE precisa ter menos de 20 dígitos."
                telefone_valido = False
            else:
                telefone_valido = True
        return [novo_nome, novo_endereco, novo_telefone]

    def consulta(self,cpf):
        cprint("************************", "green")
        print("Escolha a especialização que deseja consultar:")
        especializacoes = self.especializacaoController.listarEspecializacoes()
        
        for esp in especializacoes:
            tipo_esp = colored(esp[0], "blue")
            print(f"{esp[1]}- {tipo_esp}")
        codigo_especializacao = int(input("Qual o código da especializacao: "))
        medicos_disponiveis = self.medicoController.listarMedicosPelaEspecializacao(codigo_especializacao)
        print(medicos_disponiveis)
        for medico in medicos_disponiveis:
            print(f"CRM: {medico[0]} - Nome: {medico[1]} - Telefone: {medico[2]} - Endereço: {medico[3]} - Especialização: {medico[4]}")
        
        crm_medico = input("Qual o CRM do médico escolhido: ")
        valor = float(input("Digite o valor da consulta: "))
        plano_saude = input("É plano de saúde? s/n")
        eh_plano_saude = 1 if plano_saude == 's' else 0

        return [cpf, crm_medico, valor, eh_plano_saude]
