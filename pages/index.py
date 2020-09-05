#!C:/Python/Python38/python.exe

print("Content-type: text/html\r\n\r\n")
print("""
<html lang="pt-br">
    <head>
        <title>Vagas Estacionamento</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="../css/style.css">
        <link href="../css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div style="padding:1px" class="container-fluid jumbotron text-center">
            <h1 class="titulo">Vagas de Estacionamento</h1>
        </div>
            <form action='banco.py' method='get' target='_blank'>
                <select id='select' name='select' class='custom-select'>
                    <option value='op1' name='op1' selected>Mostrar todas as vagas</option>
                    <option value='op2' name='op2'>Mostrar vagas livres</option> 
                    <option value='op3' name='op3'>Estacionar carro</option>
                    <option value='op4' name='op4'>Remover carro</option>
                    <option value='op5' name='op5'>Mostrar vagas atualizadas</option>
                </select>
                <input type='submit' value='Confirmar'>
            </form>
    </body>
</html>
""")




