from models.usuario_model import UsuarioModel

class AuthController:
    def tentar_login(self, email, senha):
        if not email or not senha:
            return False, None, "E-mail e senha são obrigatórios."
        
        usuario_db = UsuarioModel().buscar_usuario_por_email(email)
        
        if not usuario_db:
            return False, None, "Usuário não encontrado."

        if usuario_db and usuario_db.get("senha") == senha:
            return True, usuario_db, ""
        return False, None, "E-mail ou senha inválidos."

        if usuario_db and usuario_db.get("status") == "ativo":
            return False, None, "Usuário inativo."
        
        dados_usuario = {
            "nome": usuario_db.get("nome"),
            "email": usuario_db.get("email"),
            "perfil": usuario_db.get("perfil"),
        }
        return True, dados_usuario, "Login realizado com sucesso."
    