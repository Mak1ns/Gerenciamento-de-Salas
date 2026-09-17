import sqlite3
from pathlib import Path

class ReservasModel:
    def __init__(self):
        
        base_dir = Path(__file__).resolve().parent.parent
        self.db_path = base_dir / "reservas.db"

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def criar_reserva(self, professor_id, sala_id, data, horario_inicio, horario_fim, finalidade):
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
            #  status 'Aprovada'
            cursor.execute("""
                INSERT INTO reservas (professor_id, sala_id, data, horario_inicio, horario_fim, finalidade, status)
                VALUES (?, ?, ?, ?, ?, ?, 'Aprovada')
            """, (professor_id, sala_id, str(data), str(horario_inicio), str(horario_fim), finalidade))
            conexao.commit()
            conexao.close()
            return True, "Reserva realizada com sucesso!"
        except Exception as e:
            return False, f"Erro ao criar reserva: {e}"

    def listar_todas(self):
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT r.id, u.nome, s.nome, r.data, r.horario_inicio, r.horario_fim, r.finalidade, r.status
                FROM reservas r
                LEFT JOIN usuarios u ON r.professor_id = u.id
                LEFT JOIN salas s ON r.sala_id = s.id
                ORDER BY r.data DESC, r.horario_inicio DESC
            """)
            reservas = cursor.fetchall()
            conexao.close()
            return reservas
        except Exception as e:
            print(f"Erro ao listar reservas: {e}")
            return []

    def listar_por_usuario(self, usuario_id):
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT r.id, u.nome, s.nome, r.data, r.horario_inicio, r.horario_fim, r.finalidade, r.status
                FROM reservas r
                LEFT JOIN usuarios u ON r.professor_id = u.id
                LEFT JOIN salas s ON r.sala_id = s.id
                WHERE r.professor_id = ?
                ORDER BY r.data DESC, r.horario_inicio DESC
            """, (usuario_id,))
            reservas = cursor.fetchall()
            conexao.close()
            return reservas
        except Exception as e:
            print(f"Erro ao listar reservas por usuário: {e}")
            return []

    def excluir_reserva(self, reserva_id):
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
            conexao.commit()
            conexao.close()
            return True, "Reserva excluída com sucesso!"
        except Exception as e:
            return False, f"Erro ao excluir reserva: {e}"

    def atualizar_reserva(self, reserva_id, sala_id, data, horario_inicio, horario_fim, finalidade):
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
            cursor.execute("""
                UPDATE reservas 
                SET sala_id = ?, data = ?, horario_inicio = ?, horario_fim = ?, finalidade = ?
                WHERE id = ?
            """, (sala_id, str(data), str(horario_inicio), str(horario_fim), finalidade, reserva_id))
            conexao.commit()
            conexao.close()
            return True, "Reserva atualizada com sucesso!"
        except Exception as e:
            return False, f"Erro ao atualizar reserva: {e}"