import pandas as pd
from pathlib import Path


class SalasModel:

    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.database_path = base_dir / "assets" / "data" / "salas.csv"

    def listar_todos(self):
        return pd.read_csv(self.database_path)

    def buscar_por_id(self, sala_id):
        salas = self.listar_todos()

        resultado = salas[
            salas["id_sala"] == sala_id
        ]

        if resultado.empty:
            return None

        return resultado.iloc[0]

    def buscar_por_nome(self, nome_sala):
        salas = self.listar_todos()

        return salas[
            salas["nome_sala"].str.contains(
                nome_sala,
                case=False,
                na=False
            )
        ]