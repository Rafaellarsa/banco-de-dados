from Patrocinador.PatrocinadorDAO import PatrocinadorDAO
import main

class PatrocinadorMenu(object):
    def menu_cadastrar_patrocinadores(self):
        print("==========================================")
        print("Cadastro de Patrocinadores")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todos os Patrocinadores Existentes")
        print("2\t\tListar um Patrocinador Existente")
        print("3\t\tInserir um Novo Patrocinador")
        print("4\t\tAtualizar um Patrocinador Existente")
        print("5\t\tRemover um Patrocinador Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_patrocinadores_listar_todos_patrocinadores()
            return
        if opcao == 2:
            self.menu_cadastrar_patrocinadores_listar_um_patrocinador()
            return
        if opcao == 3:
            self.menu_cadastrar_patrocinadores_inserir_um_patrocinador()
            return
        if opcao == 4:
            self.menu_cadastrar_patrocinadores_atualizar_um_patrocinador()
            return
        if opcao == 5:
            self.menu_cadastrar_patrocinadores_remover_um_patrocinador()
            return
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_listar_todos_patrocinadores(self):
        print("==========================================")
        print("Listar Todos os Patrocinadores Existentes")
        print("==========================================")
        patrocinadorDAO = PatrocinadorDAO()
        patrocinadores = patrocinadorDAO.listar_todos()
        for v in patrocinadores:
            print("*** Código: " + str(v.codigo) + " - Nome: " + v.nome + " - Login: " + v.login + " - Senha: " + v.senha + " ***")
        print("*** " + str(len(patrocinadores)) + " patrocinador(es) encontrado(s) ***")
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_listar_um_patrocinador(self):
        print("==========================================")
        print("Listar um Patrocinador Existente")
        print("==========================================")
        codigo = int(input("Digite o código do patrocinador: "))
        patrocinadorDAO = PatrocinadorDAO()
        patrocinador = patrocinadorDAO.listar(codigo)
        if patrocinador is not None:
            print("*** Código: " + str(patrocinador.codigo) + " - Nome: " + patrocinador.nome + " - Login: " + patrocinador.login + " - Senha: " + patrocinador.senha + " ***")
        else:
            print("*** Não foi possível localizar este patrocinador ***")
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_inserir_um_patrocinador(self):
        print("==========================================")
        print("Inserir um Novo Patrocinador")
        print("==========================================")
        codigo = int(input("Digite o código do novo patrocinador: "))
        nome = input("Digite o nome do novo patrocinador: ")
        login = input("Digite o login do novo patrocinador: ")
        senha = input("Digite a senha do novo patrocinador: ")
        patrocinadorDAO = PatrocinadorDAO()
        sucesso = patrocinadorDAO.inserir(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Patrocinador inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este patrocinador ***")
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_atualizar_um_patrocinador(self):
        print("==========================================")
        print("Atualizar um Patrocinador Existente")
        print("==========================================")
        codigo = int(input("Digite o código do patrocinador: "))
        nome = input("Digite o novo nome do patrocinador: ")
        login = input("Digite o novo login do patrocinador: ")
        senha = input("Digite a nova senha do patrocinador: ")
        patrocinadorDAO = PatrocinadorDAO()
        sucesso = patrocinadorDAO.atualizar(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Patrocinador atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este patrocinador ***")
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_remover_um_patrocinador(self):
        print("==========================================")
        print("Remover um patrocinador existente")
        print("==========================================")
        codigo = int(input("Digite o código do patrocinador: "))
        patrocinadorDAO = PatrocinadorDAO()
        sucesso = patrocinadorDAO.remover(codigo)
        if sucesso == True:
            print("*** Patrocinador removido com sucesso ***")
        else:
            print("*** Não foi possível remover este patrocinador ***")
        self.menu_cadastrar_patrocinadores()
