import pandas as pd
from pathlib import Path

class ReservasModel:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.databse_path = base_dir / "assets" / "data" / "reservas.csv"
        self.garantir_csv_existe()

    def garantir_csv_existe(self):
        if not self.databse_path.exists():
            self.reservas_path.parent.mkdir(parents=True, exist_ok=True)
            df = pd.DataFrame(columns=["id_reserva", "id_usuario", "id_sala", "data", "hora_inicio", "hora_fim", "status"])
            df.to_csv(self.databse_path, index=False)
            
    def listar_todos(self):
        return pd.read_csv(self.databse_path, dtype={ "data": str, "hora_inicio": str, "hora_fim": str,})
   
    def save_reservas(self, id_usuario, id_sala, data, hora_inicio, hora_fim):
        df = self.listar_todos()
        novo_id = 1 if df.empty else df["id_reserva"].max() + 1
        
        nova_reserva = pd.DataFrame([{
            "id_reserva": novo_id,
            "id_usuario": id_usuario,
            "id_sala": id_sala,
            "data": data,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "status": "pendente"
        }])
        df = pd.concat([df, nova_reserva], ignore_index=True)
        df.to_csv(self.databse_path, index=False)
        
        return True, "Sala reservada com sucesso!"
    
    def buscar_por_usuario(self,id_usuario):
        df = self.listar_todos()
        if df.empty:
            return df
            return df[df["id_usuario"] == id_usuario]
        