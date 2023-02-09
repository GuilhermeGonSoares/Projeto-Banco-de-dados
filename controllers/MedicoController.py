
from conexao import criar_conexao
from util.message import msg_bd_error


class MedicoController:

    def __init__(self, conn):
        self.conn = conn

    def criarMedico(self, dados):
        [crm, nome, telefone, endereco, fk_esp] = dados
        query = f"INSERT INTO hospital.MEDICO (crm, nome, telefone, endereco, FK_ESPECIALIZACAO_codigo) VALUES('{crm}', '{nome}', '{telefone}', '{endereco}', '{fk_esp}');"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()

            medico = self.findMedico(crm)
            return medico
        except Exception as e:
            self.conn.rollback()
            msg_bd_error(e)
        finally:
            cursor.close()

    def listarMedicos(self):
        query = "SELECT crm, nome, telefone, endereco, tipo_da_especializacao FROM hospital.MEDICO m INNER JOIN hospital.ESPECIALIZACAO e ON m.FK_ESPECIALIZACAO_codigo = e.codigo ORDER BY m.nome ASC;"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)

            medicos = cursor.fetchall()
            return medicos
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()
    
    def findMedico(self, crm):
        query = "SELECT crm, nome, telefone, endereco, tipo_da_especializacao FROM hospital.MEDICO m INNER JOIN hospital.ESPECIALIZACAO e ON m.FK_ESPECIALIZACAO_codigo = e.codigo WHERE m.crm="+crm+";"      
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            medico = cursor.fetchone()
            cursor.close()
            
            return medico
        except Exception as e:
            cursor.close()
            msg_bd_error(e)

    def atualizarMedico(self, crm, dados):
        [nome, telefone, endereco, fk_esp] = dados
        query = f"UPDATE hospital.MEDICO SET nome='{nome}', endereco='{endereco}', telefone='{telefone}', FK_ESPECIALIZACAO_codigo='{fk_esp}' WHERE crm={crm};"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            
            self.conn.commit()
            medico = self.findMedico(crm)

            cursor.close()
            return medico
        except Exception as e:
            msg_bd_error(e)
            self.conn.rollback()
            cursor.close()

    def deletarMedico(self, crm):
        query = f"DELETE FROM hospital.MEDICO WHERE crm={crm};"
        try:
            cursor = self.conn.cursor()
            medico = self.findMedico(crm)
            
            cursor.execute(query)
            self.conn.commit()

            return medico
        except Exception as e:
            msg_bd_error(e)
            self.conn.rollback()
        finally:    
            cursor.close()

    def listarMedicosPelaEspecializacao(self, codigo_esp):
        query = f"SELECT crm, nome, telefone, endereco, tipo_da_especializacao FROM hospital.MEDICO m INNER JOIN hospital.ESPECIALIZACAO e ON m.FK_ESPECIALIZACAO_codigo = e.codigo WHERE e.codigo={codigo_esp};"      
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            medicos = cursor.fetchall()

            return medicos
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()
    
    def mostrarEspecializacao(self, crm):
        query = f"SELECT tipo_da_especializacao FROM hospital.MEDICO m INNER JOIN hospital.ESPECIALIZACAO e ON m.FK_ESPECIALIZACAO_codigo=e.codigo WHERE m.crm='{crm}';"

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            esp = cursor.fetchone()

            return esp
        except Exception as e:
            msg_bd_error(e)
        finally:
            cursor.close()

