import pandas as pd
from pathlib import Path


class UsuarioModel:

    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.database_path = base_dir / "assets" / "data" / "usuarios.csv"

    def listar_todos(self):
        return pd.read_csv(self.database_path)

    def buscar_por_id(self, usuario_id):
        usuarios = self.listar_todos()

        resultado = usuarios[
            usuarios["id"] == usuario_id
        ]

        if resultado.empty:
            return None

        return resultado.iloc[0]

    def buscar_por_nome(self, nome):
        usuarios = self.listar_todos()

        return usuarios[
            usuarios["nome"].str.contains(
                nome,
                case=False,
                na=False
            )
        ]