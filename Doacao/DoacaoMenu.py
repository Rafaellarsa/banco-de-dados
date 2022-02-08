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
            print("*** Id: " + str(d.id_doacao) + " - Id do tipo de doação: " + str(d.id_tipo_doacao) + " - Id da ação: " + str(d.id_acao) + " - Id do patrocinador: " + str(d.id_patrocinador) + " - Valor da doação: " + str(d.valor_doacao) + " - Data da doação: " + d.data_doacao + " ***")
        print("*** " + str(len(doacoes)) + " doação(ões) encontrada(s) ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_listar_uma_doacao(self):
        print("==========================================")
        print("Listar uma Doação Existente")
        print("==========================================")
        id_doacao = int(input("Digite o id da doação: "))
        doacaoDAO = DoacaoDAO()
        doacao = doacaoDAO.listar(id_doacao)
        if doacao is not None:
            print("*** Id: " + str(doacao.id_doacao) + " - Id do tipo de doação: " + str(doacao.id_tipo_doacao) + " - Id da ação: " + str(doacao.id_acao) + " - Id do patrocinador: " + str(doacao.id_patrocinador) + " - Valor da doação: " + str(doacao.valor_doacao) + " - Data da doação: " + doacao.data_doacao + " ***")
        else:
            print("*** Não foi possível localizar esta doação ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_inserir_uma_doacao(self):
        print("==========================================")
        print("Inserir uma Nova Doação")
        print("==========================================")
        id_tipo_doacao = input("Digite o id do tipo da nova doação: ")
        id_acao = input("Digite o id da ação da nova doação: ")
        id_patrocinador = input("Digite o id do patrocinador da nova doação: ")
        valor_doacao = input("Digite o valor da nova doação: ")
        data_doacao = input("Digite a data da nova doação: ")
        doacaoDAO = DoacaoDAO()
        sucesso = doacaoDAO.inserir(id_tipo_doacao, id_acao, id_patrocinador, valor_doacao, data_doacao)
        if sucesso == True:
            print("*** Doação inserida com sucesso ***")
        else:
            print("*** Não foi possível inserir esta doação ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_atualizar_uma_doacao(self):
        print("==========================================")
        print("Atualizar uma Doação Existente")
        print("==========================================")
        id_doacao = int(input("Digite o id da doação: "))
        id_tipo_doacao = input("Digite o id do novo tipo da doação: ")
        id_acao = input("Digite o id da nova ação da doação: ")
        id_patrocinador = input("Digite o id do novo patrocinador da doação: ")
        valor_doacao = input("Digite o novo valor da doação: ")
        data_doacao = input("Digite a nova data da doação: ")
        doacaoDAO = DoacaoDAO()
        sucesso = doacaoDAO.atualizar(id_doacao, id_tipo_doacao, id_acao, id_patrocinador, valor_doacao, data_doacao)
        if sucesso == True:
            print("*** Doação atualizada com sucesso ***")
        else:
            print("*** Não foi possível atualizar esta doação ***")
        self.menu_cadastrar_doacoes()

    def menu_cadastrar_doacoes_remover_uma_doacao(self):
        print("==========================================")
        print("Remover uma doação existente")
        print("==========================================")
        id_doacao = int(input("Digite o id da doação: "))
        doacaoDAO = DoacaoDAO()
        sucesso = doacaoDAO.remover(id_doacao)
        if sucesso == True:
            print("*** Doação removida com sucesso ***")
        else:
            print("*** Não foi possível remover esta doação ***")
        self.menu_cadastrar_doacoes()
