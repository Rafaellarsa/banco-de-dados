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
        for ta in tiposAcao:
            print("*** Id: " + str(ta.id_tipo_acao) + " - Tipo: " + ta.tipo + " - Descrição: " + ta.descricao + " ***")
        print("*** " + str(len(tiposAcao)) + " tipo(s) de ação encontrado(s) ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_listar_um_tipo_acao(self):
        print("==========================================")
        print("Listar um Tipo de Ação Existente")
        print("==========================================")
        id_tipo_acao = int(input("Digite o id do tipo de ação: "))
        tipoAcaoDAO = TipoAcaoDAO()
        tipoAcao = tipoAcaoDAO.listar(id_tipo_acao)
        if tipoAcao is not None:
            print("*** Id: " + str(tipoAcao.id_tipo_acao) + " - Tipo: " + tipoAcao.tipo + " - Descrição: " + tipoAcao.descricao + " ***")
        else:
            print("*** Não foi possível localizar este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_inserir_um_tipo_acao(self):
        print("==========================================")
        print("Inserir um Novo Tipo de Ação")
        print("==========================================")
        tipo = input("Digite o nome do novo tipo de ação: ")
        descricao = input("Digite a descrição do novo tipo de ação: ")
        tipoAcaoDAO = TipoAcaoDAO()
        sucesso = tipoAcaoDAO.inserir(tipo, descricao)
        if sucesso == True:
            print("*** Tipo de Ação inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_atualizar_um_tipo_acao(self):
        print("==========================================")
        print("Atualizar um Tipo de Ação Existente")
        print("==========================================")
        id_tipo_acao = int(input("Digite o id do tipo de ação: "))
        tipo = input("Digite o novo nome do tipo de ação: ")
        descricao = input("Digite a nova descrição do tipo de ação: ")
        tipoAcaoDAO = TipoAcaoDAO()
        sucesso = tipoAcaoDAO.atualizar(id_tipo_acao, tipo, descricao)
        if sucesso == True:
            print("*** Tipo de Ação atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()

    def menu_cadastrar_tipos_acao_remover_um_tipo_acao(self):
        print("==========================================")
        print("Remover um tipo de ação existente")
        print("==========================================")
        id_tipo_acao = int(input("Digite o id do tipo de ação: "))
        tipoAcaoDAO = TipoAcaoDAO()
        sucesso = tipoAcaoDAO.remover(id_tipo_acao)
        if sucesso == True:
            print("*** Tipo de Ação removido com sucesso ***")
        else:
            print("*** Não foi possível remover este tipo de ação ***")
        self.menu_cadastrar_tipos_acao()
