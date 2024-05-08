import mysql.connector

# Função para conectar ao banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gordoidiota123",
        database="dados"
    )

# Função para inserir um novo aluno na tabela aluno
def adicionar_aluno(cpf_aluno, nome, rgm):
    db = conectar_banco()
    cursor = db.cursor()
    
    # Executar a inserção dos dados na tabela aluno
    sql = "INSERT INTO aluno (cpf_aluno, nome, rgm) VALUES (%s, %s, %s)"
    val = (cpf_aluno, nome, rgm)
    cursor.execute(sql, val)
    
    # Commit para confirmar a transação
    db.commit()
    
    # Fechar cursor e conexão
    cursor.close()
    db.close()

# Função para ler e retornar todos os alunos da tabela aluno
def ler_alunos():
    db = conectar_banco()
    cursor = db.cursor()
    
    # Executar a consulta SQL para obter todos os alunos
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    
    # Fechar cursor e conexão
    cursor.close()
    db.close()
    
    return alunos
