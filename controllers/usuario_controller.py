from models.usuario_model import UsuarioModel


class UsuarioController:

    def __init__(self):
        self.model = UsuarioModel()

    def listar_usuarios(self):
        return self.model.listar_todos()

    def buscar_usuario(self, nome):
        if not nome:
            return self.model.listar_todos()

        return self.model.buscar_por_nome(nome)

    def quantidade_usuarios(self):
        usuarios = self.model.listar_todos()
        return len(usuarios)