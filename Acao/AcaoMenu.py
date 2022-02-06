from Acao.AcaoDAO import AcaoDAO
import main

class AcaoMenu(object):
    def menu_cadastrar_acoes(self):
        print("==========================================")
        print("Cadastro de Ações")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todas as Ações Existentes")
        print("2\t\tListar uma Ação Existente")
        print("3\t\tInserir uma Nova Ação")
        print("4\t\tAtualizar uma Ação Existente")
        print("5\t\tRemover uma Ação Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_acoes_listar_todas_acoes()
            return
        if opcao == 2:
            self.menu_cadastrar_acoes_listar_uma_acao()
            return
        if opcao == 3:
            self.menu_cadastrar_acoes_inserir_uma_acao()
            return
        if opcao == 4:
            self.menu_cadastrar_acoes_atualizar_uma_acao()
            return
        if opcao == 5:
            self.menu_cadastrar_acoes_remover_uma_acao()
            return
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_listar_todas_acoes(self):
        print("==========================================")
        print("Listar Todas as Ações Existentes")
        print("==========================================")
        acaoDAO = AcaoDAO()
        acoes = acaoDAO.listar_todos()
        for a in acoes:
            print("*** Código: " + str(a.codigo) + " - Nome: " + a.nome + " - Login: " + a.login + " - Senha: " + a.senha + " ***")
        print("*** " + str(len(acoes)) + " ação(ões) encontrada(s) ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_listar_uma_acao(self):
        print("==========================================")
        print("Listar uma Ação Existente")
        print("==========================================")
        codigo = int(input("Digite o código da ação: "))
        acaoDAO = AcaoDAO()
        acao = acaoDAO.listar(codigo)
        if acao is not None:
            print("*** Código: " + str(acao.codigo) + " - Nome: " + acao.nome + " - Login: " + acao.login + " - Senha: " + acao.senha + " ***")
        else:
            print("*** Não foi possível localizar este voluntário ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_inserir_uma_acao(self):
        print("==========================================")
        print("Inserir uma Nova Ação")
        print("==========================================")
        codigo = int(input("Digite o código da nova ação: "))
        nome = input("Digite o nome da nova ação: ")
        login = input("Digite o login da nova ação: ")
        senha = input("Digite a senha da nova ação: ")
        acaoDAO = AcaoDAO()
        sucesso = acaoDAO.inserir(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Ação inserida com sucesso ***")
        else:
            print("*** Não foi possível inserir esta ação ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_atualizar_uma_acao(self):
        print("==========================================")
        print("Atualizar uma Ação Existente")
        print("==========================================")
        codigo = int(input("Digite o código da ação: "))
        nome = input("Digite o novo nome da ação: ")
        login = input("Digite o novo login da ação: ")
        senha = input("Digite a nova senha da ação: ")
        acaoDAO = AcaoDAO()
        sucesso = acaoDAO.atualizar(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Ação atualizada com sucesso ***")
        else:
            print("*** Não foi possível atualizar esta ação ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_remover_uma_acao(self):
        print("==========================================")
        print("Remover uma ação existente")
        print("==========================================")
        codigo = int(input("Digite o código da ação: "))
        acaoDAO = AcaoDAO()
        sucesso = acaoDAO.remover(codigo)
        if sucesso == True:
            print("*** Ação removida com sucesso ***")
        else:
            print("*** Não foi possível remover esta ação ***")
        self.menu_cadastrar_acoes()
