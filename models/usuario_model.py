import os
import csv

class UsuarioModel:
    def buscar_usuario_por_email(self, email):
        caminho_csv = os.path.join("assets", "data", "usuarios.csv")
        if not os.path.exists(caminho_csv):
            return None
        
        with open(caminho_csv, mode='r') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            for linha in leitor_csv:
                if linha['email'] == email:
                    return linha
        return None