import os
import csv

class Usuario_model:
    def buscar_usuario(self, nome, email):
        if not os.path.exists('usuarios.csv'):
            return None
        
        with open('usuarios.csv', mode='r') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            for linha in leitor_csv:
                if linha['nome'] == nome and linha['email'] == email:
                    return linha
        return None