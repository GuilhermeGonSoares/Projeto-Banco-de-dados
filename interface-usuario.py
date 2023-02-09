from termcolor import cprint

from conexao import criar_conexao, fechar_conexao
from controllers.ConsultaController import ConsultaController
from controllers.EspecializacaoController import EspecializacaoController
from controllers.MedicoController import MedicoController
from controllers.PacienteController import PacienteController
from util.message import atendimento, atendimento_paciente, boas_vindas, menu
from views.AtendimentoPacienteView import AtendimentoPacienteView
from views.ConsultaView import consultaView
from views.MedicoView import MedicoView

conn = criar_conexao()

pacienteController = PacienteController(conn)
especializacaoController = EspecializacaoController(conn)
medicoController = MedicoController(conn)
consultaController = ConsultaController(conn)


boas_vindas()
opcoes = -1
while opcoes != 0:
    atendimento()
    
    opcoes = int(input())
    print()
    if opcoes == 1:
        AtendimentoPacienteView(pacienteController, especializacaoController, medicoController, consultaController)
    if opcoes == 2:
        MedicoView(medicoController, especializacaoController)
    if opcoes == 3:
        consultaView(consultaController)
        
if opcoes == 0:
    fechar_conexao(conn)