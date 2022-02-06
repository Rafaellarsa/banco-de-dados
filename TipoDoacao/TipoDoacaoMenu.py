from TipoDoacao.TipoDoacaoDAO import TipoDoacaoDAO
import main

class TipoDoacaoMenu(object):
    def menu_cadastrar_tipos_doacao(self):
        print("==========================================")
        print("Cadastro de Tipos de Doação")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todos os Tipos de Doação Existentes")
        print("2\t\tListar um Tipo de Doação Existente")
        print("3\t\tInserir um Novo Tipo de Doação")
        print("4\t\tAtualizar um Tipo de Doação Existente")
        print("5\t\tRemover um Tipo de Doação Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_tipos_doacao_listar_todos_tipos_doacao()
            return
        if opcao == 2:
            self.menu_cadastrar_tipos_doacao_listar_um_tipo_doacao()
            return
        if opcao == 3:
            self.menu_cadastrar_tipos_doacao_inserir_um_tipo_doacao()
            return
        if opcao == 4:
            self.menu_cadastrar_tipos_doacao_atualizar_um_tipo_doacao()
            return
        if opcao == 5:
            self.menu_cadastrar_tipos_doacao_remover_um_tipo_doacao()
            return
        self.menu_cadastrar_tipos_doacao()

    def menu_cadastrar_tipos_doacao_listar_todos_tipos_doacao(self):
        print("==========================================")
        print("Listar Todos os Tipos de Doação Existentes")
        print("==========================================")
        tipoDoacaoDAO = TipoDoacaoDAO()
        tiposDoacao = tipoDoacaoDAO.listar_todos()
        for td in tiposDoacao:
            print("*** Código: " + str(td.codigo) + " - Nome: " + td.nome + " - Login: " + td.login + " - Senha: " + td.senha + " ***")
        print("*** " + str(len(tiposDoacao)) + " tipo(s) de doação encontrado(s) ***")
        self.menu_cadastrar_tipos_doacao()

    def menu_cadastrar_tipos_doacao_listar_um_tipo_doacao(self):
        print("==========================================")
        print("Listar um Tipo de Doação Existente")
        print("==========================================")
        codigo = int(input("Digite o código do tipo de doação: "))
        tipoDoacaoDAO = TipoDoacaoDAO()
        tipoDoacao = tipoDoacaoDAO.listar(codigo)
        if tipoDoacao is not None:
            print("*** Código: " + str(tipoDoacao.codigo) + " - Nome: " + tipoDoacao.nome + " - Login: " + tipoDoacao.login + " - Senha: " + tipoDoacao.senha + " ***")
        else:
            print("*** Não foi possível localizar este tipo de doação ***")
        self.menu_cadastrar_tipos_doacao()

    def menu_cadastrar_tipos_doacao_inserir_um_tipo_doacao(self):
        print("==========================================")
        print("Inserir um Novo Tipo de Doação")
        print("==========================================")
        codigo = int(input("Digite o código do novo tipo de doação: "))
        nome = input("Digite o nome do novo tipo de doação: ")
        login = input("Digite o login do novo tipo de doação: ")
        senha = input("Digite a senha do novo tipo de doação: ")
        tipoDoacaoDAO = TipoDoacaoDAO()
        sucesso = tipoDoacaoDAO.inserir(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Tipo de Doação inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este tipo de doação ***")
        self.menu_cadastrar_tipos_doacao()

    def menu_cadastrar_tipos_doacao_atualizar_um_tipo_doacao(self):
        print("==========================================")
        print("Atualizar um Tipo de Doação Existente")
        print("==========================================")
        codigo = int(input("Digite o código do tipo de doação: "))
        nome = input("Digite o novo nome do tipo de doação: ")
        login = input("Digite o novo login do tipo de doação: ")
        senha = input("Digite a nova senha do tipo de doação: ")
        tipoDoacaoDAO = TipoDoacaoDAO()
        sucesso = tipoDoacaoDAO.atualizar(codigo, nome, login, senha)
        if sucesso == True:
            print("*** Tipo de Doação atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este tipo de doação ***")
        self.menu_cadastrar_tipos_doacao()

    def menu_cadastrar_tipos_doacao_remover_um_tipo_doacao(self):
        print("==========================================")
        print("Remover um tipo de doação existente")
        print("==========================================")
        codigo = int(input("Digite o código do tipo de doação: "))
        tipoDoacaoDAO = TipoDoacaoDAO()
        sucesso = tipoDoacaoDAO.remover(codigo)
        if sucesso == True:
            print("*** Tipo de Doação removido com sucesso ***")
        else:
            print("*** Não foi possível remover este tipo de doação ***")
        self.menu_cadastrar_tipos_doacao()
