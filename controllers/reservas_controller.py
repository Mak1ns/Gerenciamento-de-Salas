from models.reservas_model import ReservasModel


class ReservasController:
    def __init__(self):
        self.model = ReservasModel()

    def verificar_conflito(self, id_sala, data, hora_inicio, hora_fim):
        
        return self.model.existe_conflito(id_sala, data, hora_inicio, hora_fim)

    def agendar_sala(self, id_usuario, id_sala, data, hora_inicio, hora_fim, finalidade):
        if hora_inicio >= hora_fim:
            return False, "Horário de início deve ser anterior ao horário de término."

        
        return self.model.criar_reserva(
            professor_id=id_usuario,
            sala_id=id_sala,
            data=data,
            horario_inicio=hora_inicio,
            horario_fim=hora_fim,
            finalidade=finalidade
        )

    def listar_reservas_por_usuario(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)