from Doacao.DoacaoDAO import DoacaoDAO
import main

class DoacaoMenu(object):
    def menu_cadastrar_doacoes(self):
        print("==========================================")
        print("Cadastro de Doações")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todas as Doações Existentes")
        print("2\t\tListar uma Doação Existente")
        print("3\t\tInserir uma Nova Doação")
        print("4\t\tAtualizar uma Doação Existente")
        print("5\t\tRemover uma Doação Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_doacoes_listar_todas_doacoes()
            return
        if opcao == 2:
            self.menu_cadastrar_doacoes_listar_uma_doacao()
            return
        if opcao == 3:
            self.menu_cadastrar_doacoes_inserir_uma_doacao()
            return
        if opcao == 4:
            self.menu_cadastrar_doacoes_atualizar_uma_doacao()
            return
        if opcao == 5:
            self.menu_cadastrar_doacoes_remover_uma_doacao()
            return
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_listar_todas_doacoes(self):
        print("==========================================")
        print("Listar Todas as Doações Existentes")
        print("==========================================")
        doacaoDAO = DoacaoDAO()
        doacoes = doacaoDAO.listar_todos()
        for d in doacoes:
            print("*** Código: " + str(d.codigo) + " - Nome: " + d.nome + " - Login: " + d.login + " - Senha: " + d.senha + " ***")
        print("*** " + str(len(doacoes)) + " doação(ões) encontrada(s) ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_listar_uma_doacao(self):
        print("==========================================")
        print("Listar uma Doação Existente")
        print("==========================================")
        codigo = int(input("Digite o código da doação: "))
        doacaoDAO = DoacaoDAO()
        doacao = doacaoDAO.listar(codigo)
        if doacao is not None:
            print("*** Código: " + str(doacao.codigo) + " - Nome: " + doacao.nome + " - Login: " + doacao.login + " - Senha: " + doacao.senha + " ***")
        else:
            print("*** Não foi possível localizar este voluntário ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_inserir_uma_doacao(self):
        print("==========================================")
        print("Inserir uma Nova Doação")
        print("==========================================")
        codigo = int(input("Digite o código da nova doação: "))
        nome = input("Digite o nome da nova doação: ")
        login = input("Digite o login da nova doação: ")
        senha = input("Digite a senha da nova doação: ")
        doacaoDAO = DoacaoDAO()
        sucesso = doacaoDAO.inserir(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Doação inserida com sucesso ***")
        else:
            print("*** Não foi possível inserir esta doação ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_atualizar_uma_doacao(self):
        print("==========================================")
        print("Atualizar uma Doação Existente")
        print("==========================================")
        codigo = int(input("Digite o código da doação: "))
        nome = input("Digite o novo nome da doação: ")
        login = input("Digite o novo login da doação: ")
        senha = input("Digite a nova senha da doação: ")
        doacaoDAO = DoacaoDAO()
        sucesso = doacaoDAO.atualizar(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Doação atualizada com sucesso ***")
        else:
            print("*** Não foi possível atualizar esta doação ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_remover_uma_doacao(self):
        print("==========================================")
        print("Remover uma doação existente")
        print("==========================================")
        codigo = int(input("Digite o código da doação: "))
        doacaoDAO = DoacaoDAO()
        sucesso = doacaoDAO.remover(codigo)
        if sucesso == True:
            print("*** Doação removida com sucesso ***")
        else:
            print("*** Não foi possível remover esta doação ***")
        self.menu_cadastrar_doacoes()
