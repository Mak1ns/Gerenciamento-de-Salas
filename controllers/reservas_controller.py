from models.reservas_model import ReservasModel

class ReservasController:
    def __init__(self):
        self.model = ReservasModel()
        
    def verificar_conflito(self, id_sala, data, hora_inicio, hora_fim):
        df = self.model.listar_todos()
        if df.empty:
            return False
    
        filtro = (df["id_sala"] == id_sala) & (df["data"] == data) & (df ["status"] == "Ativo")
        df_sala = df[filtro]
        
        if df_sala.empty:
            return False
        
        conflitos = df_sala[
            (df_sala["hora_inicio"] < hora_fim) & 
             (df_sala["hora_fim"] > hora_inicio)
        ]
        
        return not conflitos.empty
        
    def agendar_sala(self, id_usuario, id_sala, data, hora_inicio, hora_fim):
        if hora_inicio >= hora_fim:
            return False, "Horário de início deve ser anterior ao  horário de término."
        
        if self.verificar_conflito(id_sala, data, hora_inicio, hora_fim):
            return False, "Conflito de horário! A sala já está reservada no dia e horario selecionado."
        
        self.model.save_reservas(id_usuario, id_sala, data, hora_inicio, hora_fim)
        return True, "Sala reservada com sucesso!"
    
    def listar_reservas_por_usuario(self, id_usuario):
        return self.model.buscar_por_usuario(id_usuario)
