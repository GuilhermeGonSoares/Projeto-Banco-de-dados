
from conexao import criar_conexao
from util.message import msg_bd_error


class EspecializacaoController:

    def __init__(self, conn):
        self.conn = conn

    def findEspecializacao(self, codigo):
        query = f"SELECT * FROM hospital.ESPECIALIZACAO e WHERE e.codigo={codigo} ORDER BY e.tipo_da_especializacao;"

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)

            especializacao = cursor.fetchone()

            return especializacao
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()

    def listarEspecializacoes(self):
        query = "SELECT DISTINCT e.tipo_da_especializacao, e.codigo FROM hospital.ESPECIALIZACAO e INNER JOIN hospital.MEDICO m ON e.codigo=m.FK_ESPECIALIZACAO_codigo ORDER BY e.codigo;"

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)

            especializacoes = cursor.fetchall()

            return especializacoes
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()