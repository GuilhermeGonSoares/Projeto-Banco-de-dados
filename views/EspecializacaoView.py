from termcolor import cprint

from controllers.EspecializacaoController import EspecializacaoController
from controllers.MedicoController import MedicoController
from util.limparTerminal import limparTerminal


class MedicoView:

    def __init__(self, medicoController: MedicoController, especializacaoController: EspecializacaoController):
        self.medicoController = medicoController
        self.especializacaoController = especializacaoController
        self.atendimento_ao_medico()
     

    def opcoes_atendimento_medico(self):
        cprint("************************", "green")
        print("1- Ver os seus dados")
        print("2- Atualizar seus dados")
        print("3- Deletar cadastro")
        print("4- Voltar")
        cprint("************************", "green")


    def atendimento_ao_medico(self):
        continuar = True
        while continuar:
            cprint("************************", "green")
            print("1- Acessar médico cadastrado")
            print("2- Cadastrar médico")
            print("3- Todos médicos")
            print("4- Voltar")
            cprint("************************", "green")

            op = int(input())
            match op:
                case 1:
                    gerenciar = True
                    crm = input("Digite o seu CRM(válido) para realizar a consulta por favor: ")
                    while gerenciar:
                        gerenciar = self.gerenciar_medico(crm)
                case 2:
                    cadastro_valido = False
                    while not cadastro_valido:
                        cadastro_valido = self.cadastrar_paciente()
                case 3:
                    pacientes = self.pacienteController.listarPacientes()
                    for paciente in pacientes:
                        cprint(self.formatar_dados_medico(paciente), "yellow")
                case _:
                    continuar = False

     
    def gerenciar_medico(self, crm):
        medico = self.medicoController.findMedico(crm)    
    
        if not medico:
            cprint("CRM inválido ou não cadastrado", "red")
            return False

        
        cprint(f"Bem-vindo {medico[1]}! Estamos a sua disposiçao", "blue")
        self.opcoes_atendimento_medico()
        medico_opcoes = int(input())

        match medico_opcoes:
            case 1:
                cprint(self.formatar_dados_medico(medico), "yellow")
                return True
            case 2:
                dados = self.novos_dados()
                medico = self.medicoController.atualizarMedico(crm, dados)
                cprint(self.formatar_dados_medico(medico), "yellow")
                cprint(f"MEDICO {medico[0]} ATUALIZADO COM SUCESSO!", "blue")
                return True
            case 3:
                cprint("************************", "green")
                print("Certeza que deseja excluir o seu cadastro? ")
                print("1- Sim")
                print("2- Não")
                cprint("************************", "green")

                quer_deletar = int(input())
                if quer_deletar != 1:
                    return True
                medico = self.medicoController.deletarMedico(crm)
                cprint(f"MEDICO do CRM: {medico[0]} deletado com sucesso", "yellow")
                return False
            
            case _:
                return False



    def cadastrar_paciente(self):
        crm_valido = False
        msg_crm = "crm:"
        while not crm_valido:
            novo_crm = input(f"{msg_crm} ")
            if len(novo_crm) != 11:
                msg_crm = "crm inválido! crm precisa ter 11 dígitos"
                crm_valido = False
            else:
                crm_valido = True

        dados = self.novos_dados()

        dados.insert(0, novo_crm)
        paciente = self.pacienteController.criarPaciente(dados)
        if not paciente:
            return False
        cprint("Paciente cadastrado com sucesso", "green")
        cprint(self.formatar_dados_medico(paciente), "yellow")
        return True

    def formatar_dados_especializacao(self,especializacao):
        return f'''
        Código: {especializacao[0]}
        Tipo da especializacao: {especializacao[1]}
        '''
    def novos_dados(self):
        cprint("Forneça os valores:", "green")
        
        esp_valida, telefone_valido = False, False
    
        
        novo_nome = input("NOME: ")
        novo_endereco = input("ENDERECO: ")

        msg_telefone= "TELEFONE:"
        while not telefone_valido:
            novo_telefone = input(f"{msg_telefone} ")
            if len(novo_telefone) > 20:
                msg_crm = "TELEFONE inválido! TELEFONE precisa ter menos de 20 dígitos."
                telefone_valido = False
            else:
                telefone_valido = True
        
        msg_esp = "Codigo da especialização:"
        while not esp_valida:
            novo_esp = int(input(f"{msg_esp}"))
            esp = self.especializacaoController.findEspecializacao(novo_esp)
            if not esp:
                msg_esp = "Código especialização inválido! Selecione uma dessas especializações ou crie uma nova especialização:"
                especializacoes = self.especializacaoController.listarEspecializacoes()
                
        
        return [novo_nome, novo_endereco, novo_telefone]

    def marcar_consulta(self,crm):
        cprint("************************", "green")
        print("Escolha a especialização que deseja consultar:")
        