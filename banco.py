import sqlite3

def conectar():
    return sqlite3.connect("reservas.db")

def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    # Tabela de usuários com a coluna 'departamento'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL,
            departamento TEXT DEFAULT 'Geral'
        )
    """)
    # ... (demais tabelas)
    conexao.commit()
    conexao.close()

def criar_usuarios_iniciais():
    conexao = conectar()
    cursor = conexao.cursor()

    usuarios = [
        ("Administrador", "admin@faculdade.com", "1234", "Administrador", "TI / Administração"),
        ("João da Silva", "joao@faculdade.com", "1234", "Professor", "Departamento de Computação")
    ]

    for usuario in usuarios:
        try:
            cursor.execute("""
                INSERT INTO usuarios (nome, email, senha, tipo, departamento)
                VALUES (?, ?, ?, ?, ?)
            """, usuario)
        except sqlite3.IntegrityError:
            pass

    conexao.commit()
    conexao.close()

def criar_usuarios_iniciais():
    conexao = conectar()
    cursor = conexao.cursor()

    usuarios = [
        ("Administrador", "admin@faculdade.com", "1234", "Administrador"),
        ("João da Silva", "joao@faculdade.com", "1234", "Professor")
    ]

    for usuario in usuarios:
        try:
            cursor.execute("""
                INSERT INTO usuarios (nome, email, senha, tipo)
                VALUES (?, ?, ?, ?)
            """, usuario)
        except sqlite3.IntegrityError:
            pass

    conexao.commit()
    conexao.close()

def criar_salas_iniciais():
    conexao = conectar()
    cursor = conexao.cursor()

    
    cursor.execute("SELECT COUNT(*) FROM salas")
    total_salas = cursor.fetchone()[0]

   
    if total_salas == 0:
        salas = [
            ("Laboratório de Informática 01", 40, "Bloco A", "Sim", 40, "Disponível"),
            ("Sala de Aula 102", 50, "Bloco B", "Sim", 0, "Disponível"),
            ("Auditório Principal", 150, "Bloco Central", "Sim", 0, "Disponível")
        ]

        for sala in salas:
            cursor.execute("""
                INSERT INTO salas (nome, capacidade, localizacao, projetor, computadores, status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, sala)

        conexao.commit()
    
    conexao.close()

if __name__ == "__main__":
    criar_banco()
    criar_usuarios_iniciais()
    criar_salas_iniciais()
    print("Banco de dados atualizado com sucesso!")