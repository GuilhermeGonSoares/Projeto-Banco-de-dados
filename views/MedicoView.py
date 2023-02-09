from termcolor import colored, cprint

from controllers.EspecializacaoController import EspecializacaoController
from controllers.MedicoController import MedicoController
from util.limparTerminal import limparTerminal


class MedicoView:

    def __init__(self, medicoController: MedicoController, especializacaoController: EspecializacaoController):
        self.medicoController = medicoController
        self.especializacaoController = especializacaoController
        self.atendimento_ao_medico()
     

    def opcoes_atendimento_medico(self):
        print()
        cprint("************************", "green")
        print(colored("Digite os números correspondentes no menu para realizar as operações", "green", attrs=["bold"]))
        print("1- Ver os seus dados")
        print("2- Atualizar seus dados")
        print("3- Deletar cadastro")
        print("4- Especialização")
        print("5- Voltar")
        cprint("************************", "green")


    def atendimento_ao_medico(self):
        continuar = True
        while continuar:
            print()
            cprint("************************", "green")
            print(colored("Digite os números correspondentes no menu para realizar as operações", "green", attrs=["bold"]))
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
                        cadastro_valido = self.cadastrar_medico()
                case 3:
                    medicos = self.medicoController.listarMedicos()
                    for medico in medicos:
                        cprint(self.formatar_dados_medico(medico), "yellow")
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
                cprint(f"MEDICO {medico[0]} ATUALIZADO COM SUCESSO!", "green")
                return True
            case 3:
                print()
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
            
            case 4:
                esp = self.medicoController.mostrarEspecializacao(crm)
                tipo_esp = colored(esp[0], "blue", attrs=["bold", "underline"])
                cprint(f"Sua especialização é: {tipo_esp}", "blue")
                
            
            case _:
                return False



    def cadastrar_medico(self):
        crm_valido = False
        msg_crm = "CRM:"
        while not crm_valido:
            novo_crm = input(f"{msg_crm} ")
            if len(novo_crm) != 12:
                msg_crm = "CRM inválido! CRM precisa ter 12 dígitos"
                crm_valido = False
            else:
                crm_valido = True

        dados = self.novos_dados()

        dados.insert(0, novo_crm)
        medico = self.medicoController.criarMedico(dados)
        if not medico:
            return False
        cprint("Médico cadastrado com sucesso", "green")
        cprint(self.formatar_dados_medico(medico), "yellow")
        return True

    def formatar_dados_medico(self,medico):
        return f'''
        CRM: {medico[0]}
        NOME COMPLETO: {medico[1]}
        ENDERECO: {medico[3]}
        TELEFONE: {medico[2]}
        ESPECIALIZAÇÃO: {medico[4]}
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
        
        while not esp_valida:
            novo_esp = int(input("Codigo da especialização: "))
            esp = self.especializacaoController.findEspecializacao(novo_esp)
            if not esp:
                esp_valida = False
                cprint("Código especialização inválido! Certifique-se de ser um dos seguintes codigos:", "red")
                especializacoes = self.especializacaoController.listarEspecializacoes()
                for esp in especializacoes:
                    tipo_esp = colored(esp[0], "blue")
                    print(f"{esp[1]}- {tipo_esp}")
            else: 
                esp_valida = True
        
        return [novo_nome, novo_telefone, novo_endereco, novo_esp]

        