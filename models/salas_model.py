import sqlite3
from pathlib import Path

class SalasModel:

    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.db_path = base_dir / "reservas.db"

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def listar_todos(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, capacidade, localizacao, projetor, computadores, status FROM salas")
        salas = cursor.fetchall()
        conexao.close()
        return salas

    def listar_salas_disponiveis(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, capacidade, localizacao FROM salas WHERE status = 'Disponível'")
        salas = cursor.fetchall()
        conexao.close()
        return salas

    def buscar_por_id(self, sala_id):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome, capacidade, localizacao, projetor, computadores, status FROM salas WHERE id = ?", 
            (sala_id,)
        )
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            return {
                "id": resultado[0],
                "nome": resultado[1],
                "capacidade": resultado[2],
                "localizacao": resultado[3],
                "projetor": resultado[4],
                "computadores": resultado[5],
                "status": resultado[6]
            }
        return None

    def buscar_por_nome(self, nome_sala):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome, capacidade, localizacao, projetor, computadores, status FROM salas WHERE nome LIKE ?", 
            (f"%{nome_sala}%",)
        )
        salas = cursor.fetchall()
        conexao.close()
        return salas