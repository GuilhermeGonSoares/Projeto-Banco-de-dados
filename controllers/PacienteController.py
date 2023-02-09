from conexao import criar_conexao
from util.message import msg_bd_error


class PacienteController:

    def __init__(self, conn):
        self.conn = conn

    def criarPaciente(self, dados):
        [cpf, nome, endereco, telefone] = dados
        query = f"INSERT INTO hospital.PACIENTE (cpf, nome, endereco, telefone) VALUES('{cpf}', '{nome}', '{endereco}', '{telefone}');"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()

            paciente = self.findPaciente(cpf)
            return paciente
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()

    def listarPacientes(self):
        query = "SELECT * FROM hospital.PACIENTE ORDER BY nome ASC;"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)

            pacientes = cursor.fetchall()
            return pacientes
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()
    
    def findPaciente(self, cpf):
        query = "SELECT * FROM hospital.PACIENTE p WHERE p.cpf="+cpf+";"      
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            paciente = cursor.fetchone()
            cursor.close()
            
            return paciente
        except Exception as e:
            cursor.close()
            msg_bd_error(e)

    def atualizarPaciente(self, cpf, dados):
        [nome, endereco, telefone] = dados
        query = f"UPDATE hospital.PACIENTE SET nome='{nome}', endereco='{endereco}', telefone='{telefone}' WHERE cpf={cpf};"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            
            self.conn.commit()
            paciente = self.findPaciente(cpf)

            cursor.close()
            return paciente
        except Exception as e:
            msg_bd_error(e)
            self.conn.rollback()
            cursor.close()

    def deletarPaciente(self, cpf):
        query = f"DELETE FROM hospital.PACIENTE WHERE cpf={cpf};"
        try:
            cursor = self.conn.cursor()
            paciente = self.findPaciente(cpf)
            
            cursor.execute(query)
            self.conn.commit()

            return paciente
        except Exception as e:
            msg_bd_error(e)
            self.conn.rollback()
        finally:    
            cursor.close()