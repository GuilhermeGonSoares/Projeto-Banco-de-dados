import os

import mysql.connector
from dotenv import load_dotenv

from util.message import msg_bd_connection, msg_bd_error

load_dotenv()


def criar_conexao():
    try:
        msg_bd_connection("Conectando ao banco de dados")
        #Conectar ao banco de dados
        connection = mysql.connector.connect(
            host=os.environ.get("DATABASE_HOST"),
            user=os.environ.get("DATABASE_USERNAME"),
            password=os.environ.get("DATABASE_PASSWORD"),
            database=os.environ.get("hospital")
        )
        return connection
    except mysql.connector.Error as error:
        msg_bd_error("Error ao conectar ao banco de dados")
        msg_bd_error(error)

def fechar_conexao(connection):
    if connection.is_connected():
        connection.close()
        msg_bd_connection("Conexão fechada.")