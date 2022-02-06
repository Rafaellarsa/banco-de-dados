from TipoAcao.TipoAcaoDAO import TipoAcaoDAO
import main

class TipoAcaoMenu(object):
    def menu_cadastrar_tipos_acao(self):
        print("==========================================")
        print("Cadastro de Tipos de Ação")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todos os Tipos de Ação Existentes")
        print("2\t\tListar um Tipo de Ação Existente")
        print("3\t\tInserir um Novo Tipo de Ação")
        print("4\t\tAtualizar um Tipo de Ação Existente")
        print("5\t\tRemover um Tipo de Ação Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_tipos_acao_listar_todos_tipos_acao()
            return
        if opcao == 2:
            self.menu_cadastrar_tipos_acao_listar_um_tipo_acao()
            return
        if opcao == 3:
            self.menu_cadastrar_tipos_acao_inserir_um_tipo_acao()
            return
        if opcao == 4:
            self.menu_cadastrar_tipos_acao_atualizar_um_tipo_acao()
            return
        if opcao == 5:
            self.menu_cadastrar_tipos_acao_remover_um_tipo_acao()
            return
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_listar_todos_tipos_acao(self):
        print("==========================================")
        print("Listar Todos os Tipos de Ação Existentes")
        print("==========================================")
        tipoAcaoDAO = TipoAcaoDAO()
        tiposAcao = tipoAcaoDAO.listar_todos()
        for td in tiposAcao:
            print("*** Código: " + str(td.codigo) + " - Nome: " + td.nome + " - Login: " + td.login + " - Senha: " + td.senha + " ***")
        print("*** " + str(len(tiposAcao)) + " tipo(s) de ação encontrado(s) ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_listar_um_tipo_acao(self):
        print("==========================================")
        print("Listar um Tipo de Ação Existente")
        print("==========================================")
        codigo = int(input("Digite o código do tipo de ação: "))
        tipoAcaoDAO = TipoAcaoDAO()
        tipoAcao = tipoAcaoDAO.listar(codigo)
        if tipoAcao is not None:
            print("*** Código: " + str(tipoAcao.codigo) + " - Nome: " + tipoAcao.nome + " - Login: " + tipoAcao.login + " - Senha: " + tipoAcao.senha + " ***")
        else:
            print("*** Não foi possível localizar este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_inserir_um_tipo_acao(self):
        print("==========================================")
        print("Inserir um Novo Tipo de Ação")
        print("==========================================")
        codigo = int(input("Digite o código do novo tipo de ação: "))
        nome = input("Digite o nome do novo tipo de ação: ")
        login = input("Digite o login do novo tipo de ação: ")
        senha = input("Digite a senha do novo tipo de ação: ")
        tipoAcaoDAO = TipoAcaoDAO()
        sucesso = tipoAcaoDAO.inserir(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Tipo de Ação inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_atualizar_um_tipo_acao(self):
        print("==========================================")
        print("Atualizar um Tipo de Ação Existente")
        print("==========================================")
        codigo = int(input("Digite o código do tipo de ação: "))
        nome = input("Digite o novo nome do tipo de ação: ")
        login = input("Digite o novo login do tipo de ação: ")
        senha = input("Digite a nova senha do tipo de ação: ")
        tipoAcaoDAO = TipoAcaoDAO()
        sucesso = tipoAcaoDAO.atualizar(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Tipo de Ação atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_remover_um_tipo_acao(self):
        print("==========================================")
        print("Remover um tipo de ação existente")
        print("==========================================")
        codigo = int(input("Digite o código do tipo de ação: "))
        tipoAcaoDAO = TipoAcaoDAO()
        sucesso = tipoAcaoDAO.remover(codigo)
        if sucesso == True:
            print("*** Tipo de Ação removido com sucesso ***")
        else:
            print("*** Não foi possível remover este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()
