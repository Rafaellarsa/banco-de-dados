from Usuario.UsuarioDAO import UsuarioDAO
import main

class UsuarioMenu(object):
    def menu_cadastrar_usuarios(self):
        print("==========================================")
        print("Cadastro de Usuários")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todos os Usuários Existentes")
        print("2\t\tListar um Usuário Existente")
        print("3\t\tInserir um Novo Usuário")
        print("4\t\tAtualizar um Usuário Existente")
        print("5\t\tRemover um Usuário Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_usuarios_listar_todos_usuarios()
            return
        if opcao == 2:
            self.menu_cadastrar_usuarios_listar_um_usuario()
            return
        if opcao == 3:
            self.menu_cadastrar_usuarios_inserir_um_usuario()
            return
        if opcao == 4:
            self.menu_cadastrar_usuarios_atualizar_um_usuario()
            return
        if opcao == 5:
            self.menu_cadastrar_usuarios_remover_um_usuario()
            return
        self.menu_cadastrar_usuarios()

    def menu_cadastrar_usuarios_listar_todos_usuarios(self):
        print("==========================================")
        print("Listar Todos os Usuários Existentes")
        print("==========================================")
        usuarioDAO = UsuarioDAO()
        usuarios = usuarioDAO.listar_todos()
        for u in usuarios:
            print("*** Id: " + str(u.id_usuario) + " - Nome: " + u.nome + " - Cpf: " + u.cpf + " - Email: " + u.email + " - Senha: " + u.senha + " - Telefone: " + u.telefone + " ***")
        print("*** " + str(len(usuarios)) + " usuário(s) encontrado(s) ***")
        self.menu_cadastrar_usuarios()

    def menu_cadastrar_usuarios_listar_um_usuario(self):
        print("==========================================")
        print("Listar um Usuário Existente")
        print("==========================================")
        codigo = int(input("Digite o código do usuário: "))
        usuarioDAO = UsuarioDAO()
        usuario = usuarioDAO.listar(codigo)
        if usuario is not None:
            print("*** Id: " + str(usuario.id_usuario) + " - Nome: " + usuario.nome + " - Cpf: " + usuario.cpf + " - Email: " + usuario.email + " - Senha: " + usuario.senha + " - Telefone: " + usuario.telefone + " ***")
        else:
            print("*** Não foi possível localizar este usuário ***")
        self.menu_cadastrar_usuarios()

    def menu_cadastrar_usuarios_inserir_um_usuario(self):
        print("==========================================")
        print("Inserir um Novo Usuário")
        print("==========================================")
        nome = input("Digite o nome do novo usuário: ")
        cpf = input("Digite o cpf do novo usuário: ")
        email = input("Digite o email do novo usuário: ")
        senha = input("Digite a senha do novo usuário: ")
        telefone = input("Digite o telefone do novo usuário: ")
        usuarioDAO = UsuarioDAO()
        sucesso = usuarioDAO.inserir(nome, cpf, email, senha, telefone)
        if sucesso == True:
            print("*** Usuário inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este usuário ***")
        self.menu_cadastrar_usuarios()

    def menu_cadastrar_usuarios_atualizar_um_usuario(self):
        print("==========================================")
        print("Atualizar um Usuário Existente")
        print("==========================================")
        id_usuario = int(input("Digite o id do usuário: "))
        nome = input("Digite o novo nome do usuário: ")
        cpf = input("Digite o novo cpf do usuário: ")
        email = input("Digite o novo email do usuário: ")
        senha = input("Digite a nova senha do usuário: ")
        telefone = input("Digite o novo telefone do usuário: ")
        usuarioDAO = UsuarioDAO()
        sucesso = usuarioDAO.atualizar(id_usuario, nome, cpf, email, senha, telefone)
        if sucesso == True:
            print("*** Usuário atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este usuário ***")
        self.menu_cadastrar_usuarios()

    def menu_cadastrar_usuarios_remover_um_usuario(self):
        print("==========================================")
        print("Remover um usuário existente")
        print("==========================================")
        id_usuario = int(input("Digite o código do usuário: "))
        usuarioDAO = UsuarioDAO()
        sucesso = usuarioDAO.remover(id_usuario)
        if sucesso == True:
            print("*** Usuário removido com sucesso ***")
        else:
            print("*** Não foi possível remover este usuário ***")
        self.menu_cadastrar_usuarios()
