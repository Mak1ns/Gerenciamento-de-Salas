from models.salas_model import SalasModel


class SalasController:

    def __init__(self):
        self.model = SalasModel()

    def listar_salas(self):
        return self.model.listar_todos()

    def buscar_sala(self, nome):
        if not nome:
            return self.model.listar_todos()

        return self.model.buscar_por_nome(nome)

    def quantidade_salas(self):
        salas = self.model.listar_todos()
        return len(salas)