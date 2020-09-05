#!C:/Python/Python38/python.exe

import pymysql
import cgi, cgitb

# Abrindo uma conexão com o banco de dados      
bd = pymysql.connect(host='localhost',
                        user='root',
                        db='cursoPython',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
                              
# instancia um objeto cursor utilizando o método cursor
cursor = bd.cursor()

s = cgi.FieldStorage()

print("Content-type: text/html\r\n\r\n")
print("""
<html lang="pt-br">
    <head>
        <title>Vagas Estacionamento</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="../css/style.css">
        <link href="../css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div style="padding:1px" class="container-fluid jumbotron text-center">
            <h1>Estacionamento</h1>
        </div>
    </body>
</html>
""")


def cria_tabela():
    sql = """CREATE TABLE IF NOT EXISTS `estacionamento` (`id_vaga` INT PRIMARY KEY NOT NULL, `nome_vaga` VARCHAR(255) NOT NULL, `status_vaga` VARCHAR(255) NOT NULL)"""
    cursor.execute(sql)
    insereDados()

def insereDados():
    for i in range(1,21):
        if i <= 20:
            sql = "INSERT IGNORE INTO `estacionamento`(`id_vaga`, `nome_vaga`, `status_vaga`) VALUES ('%d','Vaga %d','Livre')" % (i,i)
            cursor.execute(sql)
        else:
            print("cadastrado")


def atualizaDados():
    print("<h3>Escolha uma vaga:</h3>")
    print("""
    <form method='post' target='_self'>
        <select id='vagas' name='vagas' class='custom-select'>
            <option value='1' name='v1'>Vaga 1</option>
            <option value='2' name='v2'>Vaga 2</option> 
            <option value='3' name='v3'>Vaga 3</option>
            <option value='4' name='v4'>Vaga 4</option>
            <option value='5' name='v5'>Vaga 5</option>
            <option value='6' name='v6'>Vaga 6</option>
            <option value='7' name='v7'>Vaga 7</option>
            <option value='8' name='v8'>Vaga 8</option>
            <option value='9' name='v9'>Vaga 9</option>
            <option value='10' name='v10'>Vaga 10</option>
            <option value='11' name='v11'>Vaga 11</option>
            <option value='12' name='v12'>Vaga 12</option>
            <option value='13' name='v13'>Vaga 13</option>
            <option value='14' name='v14'>Vaga 14</option>
            <option value='15' name='v15'>Vaga 15</option>
            <option value='16' name='v16'>Vaga 16</option>
            <option value='17' name='v17'>Vaga 17</option>
            <option value='18' name='v18'>Vaga 18</option>
            <option value='19' name='v19'>Vaga 19</option>
            <option value='20' name='v20'>Vaga 20</option>
        </select>
        <input type='submit' value='Confirmar'">
    </form>
    """)
    valor1 = s.getvalue('vagas')
    status1 = "SELECT `status_vaga` FROM `estacionamento` WHERE `status_vaga` = 'Livre' AND `id_vaga` = %r" % valor1
    status2 = "SELECT `status_vaga` FROM `estacionamento` WHERE `status_vaga` = 'Ocupada' AND `id_vaga` = %r" % valor1
    cursor.execute(status1)
    e1 = cursor.fetchall()
    cursor.execute(status2)
    e2 = cursor.fetchall()
    for row, i in enumerate(e1):
        status1 = i['status_vaga']
        if status1 == 'Livre':
            #valor = s.getvalue('vagas')
            sql = "UPDATE `estacionamento` SET `status_vaga` = 'Ocupada' WHERE id_vaga = %r" % valor1
            cursor.execute(sql)
            print("<h4 class='text-success text-center'>Vaga %r atualizada</h4>" % valor1)
    for row, i in enumerate(e2):
        status2 = i['status_vaga']
        if status2 == 'Ocupada':
            print("<h4 class='text-success text-center'>Vaga %r ja ocupada</h4>" % valor1)


def removeDados():
    print("<h3>Escolha uma vaga:</h3>")
    print("""
    <form method='post' target='_self'>
        <select id='vagas' name='vagas' class='custom-select'>
            <option value='1' name='v1'>Vaga 1</option>
            <option value='2' name='v2'>Vaga 2</option> 
            <option value='3' name='v3'>Vaga 3</option>
            <option value='4' name='v4'>Vaga 4</option>
            <option value='5' name='v5'>Vaga 5</option>
            <option value='6' name='v6'>Vaga 6</option>
            <option value='7' name='v7'>Vaga 7</option>
            <option value='8' name='v8'>Vaga 8</option>
            <option value='9' name='v9'>Vaga 9</option>
            <option value='10' name='v10'>Vaga 10</option>
            <option value='11' name='v11'>Vaga 11</option>
            <option value='12' name='v12'>Vaga 12</option>
            <option value='13' name='v13'>Vaga 13</option>
            <option value='14' name='v14'>Vaga 14</option>
            <option value='15' name='v15'>Vaga 15</option>
            <option value='16' name='v16'>Vaga 16</option>
            <option value='17' name='v17'>Vaga 17</option>
            <option value='18' name='v18'>Vaga 18</option>
            <option value='19' name='v19'>Vaga 19</option>
            <option value='20' name='v20'>Vaga 20</option>
        </select>
        <input type='submit' value='Confirmar'>
    </form>
    """)
    valor1 = s.getvalue('vagas')
    status2 = "SELECT `status_vaga` FROM `estacionamento` WHERE `status_vaga` = 'Livre' AND `id_vaga` = %r" % valor1
    status1 = "SELECT `status_vaga` FROM `estacionamento` WHERE `status_vaga` = 'Ocupada' AND `id_vaga` = %r" % valor1
    cursor.execute(status1)
    e1 = cursor.fetchall()
    cursor.execute(status2)
    e2 = cursor.fetchall()
    for row, i in enumerate(e1):
        status1 = i['status_vaga']
        if status1 == 'Ocupada':
            #valor = s.getvalue('vagas')
            sql = "UPDATE `estacionamento` SET `status_vaga` = 'Livre' WHERE id_vaga = %r" % valor1
            cursor.execute(sql)
            print("<h4 class='text-success text-center'>Vaga %r atualizada</h4>" % valor1)
    for row, i in enumerate(e2):
        status2 = i['status_vaga']
        if status2 == 'Livre':
            print("<h4 class='text-success text-center'>Vaga %r ja esta livre</h4>" % valor1)


def mostraLivre():
    sql1 = "SELECT `nome_vaga`, `status_vaga` FROM `estacionamento` WHERE `status_vaga` = 'Livre'"
    cursor.execute(sql1)
    dado1 = cursor.fetchall()
    print("""<table class="table table-hover table-bordered table-striped text-center">
				<thead>
					<tr class="d-flex">
						<th class="col-3 text-center">
							Vagas
						</th>
                        <th class="col-3 text-center">
                            Status
                        </th>
					</tr>
				</thead>
				<tbody>
                </tbody>
    """)
    for row1 in dado1:
        print("<tr class='d-flex'><td class='col-3'>%r</td><td class='col-3'>%r</td></tr>" % (row1['nome_vaga'], row1['status_vaga']))


def mostraAtualizado():
    sql = "SELECT COUNT(`status_vaga`) AS `status_vaga` FROM `estacionamento` WHERE `status_vaga` = 'Livre'"
    cursor.execute(sql)
    s1 = cursor.fetchall()
    for row in s1:
        status = row['status_vaga']
        print("<p><h4 class='text-success text-center'>O total de Vagas Livres: %r</h4></p>" % status)
    sql2 = "SELECT COUNT(`status_vaga`) AS `status_vaga` FROM `estacionamento` WHERE `status_vaga` = 'Ocupada'"
    cursor.execute(sql2)
    s2 = cursor.fetchall()
    for row in s2:
        status = row['status_vaga']
        print("<h4 class='text-success text-center'>O total de Vagas Ocupadas: %r</h4>" % status)


def mostra_todos():
    sql1 = "SELECT `nome_vaga`, `status_vaga` FROM `estacionamento`"
    cursor.execute(sql1)
    dado1 = cursor.fetchall()
    print("""<table class="table table-hover table-bordered table-striped text-center">
				<thead>
					<tr class="d-flex">
						<th class="col-3 text-center">
							Vagas
						</th>
                        <th class="col-3 text-center">
                            Status
                        </th>
					</tr>
				</thead>
				<tbody>
                </tbody>
    """)
    for row1 in dado1:
        print("<tr class='d-flex'><td class='col-3'>%r</td><td class='col-3'>%r</td></tr>" % (row1['nome_vaga'], row1['status_vaga']))


def valor():
    if s.getvalue('select') == 'op1':
        valor = s.getvalue('select')
        mostra_todos()
    elif s.getvalue('select') == 'op2':
        valor = s.getvalue('select')
        mostraLivre()
    elif s.getvalue('select') == 'op3':
        valor = s.getvalue('select')
        atualizaDados()
    elif s.getvalue('select') == 'op4':
        valor = s.getvalue('select')
        removeDados()
    elif s.getvalue('select') == 'op5':
        valor = s.getvalue('select')
        mostraAtualizado()


cria_tabela()
valor()

bd.commit()
# fecha a conexão
bd.close()
 
    
