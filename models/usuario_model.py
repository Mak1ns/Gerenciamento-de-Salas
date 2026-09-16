import sqlite3
from pathlib import Path

class UsuarioModel:
    def __init__(self):
        
        base_dir = Path(__file__).resolve().parent.parent
        self.db_path = base_dir / "reservas.db"

    def conectar(self):
        
        return sqlite3.connect(self.db_path)

    def buscar_usuario_por_email(self, email):
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
            
            cursor.execute(
                "SELECT id, nome, email, senha, tipo FROM usuarios WHERE email = ?", 
                (email,)
            )
            resultado = cursor.fetchone()
            
            conexao.close()

            if resultado:
                return {
                    "id": resultado[0],
                    "nome": resultado[1],
                    "email": resultado[2],
                    "senha": resultado[3],
                    "perfil": resultado[4],
                    "tipo": resultado[4], 
                    "status": "Ativo"        
                }
            return None
            
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            return None