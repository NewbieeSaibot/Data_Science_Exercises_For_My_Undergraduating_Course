#imports
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='',host='localhost', database='topicos2')
TABLES = {}
TABLES['empregado'] = (
    "CREATE TABLE `empregado` ("
    "  `emp_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `fab_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nome` varchar(100) NOT NULL,"
    "  `data_nascimento` date NOT NULL,"
    "  `data_contratacao` date NOT NULL,"
    "  PRIMARY KEY (`emp_id`)"
    ") ENGINE=InnoDB")
TABLES['fabrica'] = (
    "CREATE TABLE `fabrica` ("
    "  `fab_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nome` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`fab_id`)"
    ") ENGINE=InnoDB")

cursor = cnx.cursor()
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Criando tabela {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Tabela já existe.")
        else:
            print("Aí deu ruim")
            print(err.msg)
    else:
        print("OK")

cursor.close()
