from mysql.connector import connect as conectarComBd
class Conexao:

    conexao = conectarComBd(
      host="localhost",
      user="root",
      password="abcd",
      database="gerenciadormercado"
    )
    cursor = conexao.cursor

