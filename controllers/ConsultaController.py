
import datetime

from conexao import criar_conexao
from util.message import msg_bd_error


class ConsultaController:

    def __init__(self, conn):
        self.conn = conn

    def criarConsulta(self, dados):
        [cpf, crm_medico, valor, eh_plano_saude] = dados
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')[0]

        query = f"INSERT INTO hospital.CONSULTA (fk_MEDICO_crm, fk_PACIENTE_cpf, data, valor, plano_saude) VALUES('{crm_medico}', '{cpf}', '{data}', '{valor}', '{eh_plano_saude}');" 

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()

            return self.findConsulta(crm_medico, cpf)
        except Exception as e:
            self.conn.rollback()
            msg_bd_error(e)
        finally:
            cursor.close()

    def findConsulta(self, crm, cpf):
        query = f"SELECT * FROM hospital.CONSULTA WHERE fk_MEDICO_crm='{crm}' AND fk_PACIENTE_cpf='{cpf}';"

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)

            consulta = cursor.fetchone()

            return consulta
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()

    def listarConsultas(self):
        query = f"SELECT p.cpf, p.nome , m.crm, m.nome , e.tipo_da_especializacao FROM hospital.PACIENTE p INNER JOIN hospital.CONSULTA c ON p.cpf = c.fk_PACIENTE_cpf INNER JOIN hospital.MEDICO m ON c.fk_MEDICO_crm=m.crm INNER JOIN hospital.ESPECIALIZACAO e ON m.FK_ESPECIALIZACAO_codigo=e.codigo;"

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            consultas = cursor.fetchall()

            return consultas
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()