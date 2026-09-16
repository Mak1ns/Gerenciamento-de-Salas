from models.usuario_model import UsuarioModel

class AuthController:
    def tentar_login(self, email, senha):
        if not email or not senha:
            return False, None, "E-mail e senha são obrigatórios."
        
        usuario_db = UsuarioModel().buscar_usuario_por_email(email)
        
        if not usuario_db:
            return False, None, "Usuário não encontrado."

        if str(usuario_db.get("status")).strip().capitalize() != "Ativo":
            return False, None, "Usuário inativo no sistema."

        if str(usuario_db.get("senha")) != str(senha):
            return False, None, "E-mail ou senha inválidos."

        dados_usuario = {
            "id": usuario_db.get("id"),
            "nome": usuario_db.get("nome"),
            "email": usuario_db.get("email"),
            "perfil": usuario_db.get("perfil"), 
            "tipo": usuario_db.get("tipo"),
            "status": usuario_db.get("status")
        }
        
        return True, dados_usuario, "Login realizado com sucesso."