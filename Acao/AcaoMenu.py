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
            print("*** Id: " + str(a.id_acao) + " - Local: " + a.local + " - Número de beneficiários: " + a.num_beneficiados + " - Número de voluntários: " + a.num_voluntarios + " - Id do tipo de ação: " + a.id_tipo_acao + " - Id do voluntário: " + a.id_voluntario_responsavel + " ***")
        print("*** " + str(len(acoes)) + " ação(ões) encontrada(s) ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_listar_uma_acao(self):
        print("==========================================")
        print("Listar uma Ação Existente")
        print("==========================================")
        id_acao = int(input("Digite o id da ação: "))
        acaoDAO = AcaoDAO()
        acao = acaoDAO.listar(id_acao)
        if acao is not None:
            print("*** Id: " + str(acao.id_acao) + " - Local: " + acao.local + " - Número de beneficiários: " + acao.num_beneficiados + " - Número de voluntários: " + acao.num_voluntarios + " - Id do tipo de ação: " + acao.id_tipo_acao + " - Id do voluntário: " + acao.id_voluntario_responsavel + " ***")
        else:
            print("*** Não foi possível localizar esta ação ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_inserir_uma_acao(self):
        print("==========================================")
        print("Inserir uma Nova Ação")
        print("==========================================")
        local = input("Digite o local da nova ação: ")
        num_beneficiados = input("Digite o número de beneficiários da nova ação: ")
        num_voluntarios = input("Digite o número de voluntários da nova ação: ")
        id_tipo_acao = input("Digite o id do tipo da nova ação: ")
        id_voluntario_responsavel = input("Digite o id do voluntário da nova ação: ")
        acaoDAO = AcaoDAO()
        sucesso = acaoDAO.inserir(local, num_beneficiados, num_voluntarios, id_tipo_acao, id_voluntario_responsavel)
        if sucesso == True:
            print("*** Ação inserida com sucesso ***")
        else:
            print("*** Não foi possível inserir esta ação ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_atualizar_uma_acao(self):
        print("==========================================")
        print("Atualizar uma Ação Existente")
        print("==========================================")
        id_acao = int(input("Digite o id da ação: "))
        local = input("Digite o novo local da nova ação: ")
        num_beneficiados = input("Digite o novo número de beneficiários da ação: ")
        num_voluntarios = input("Digite o novo número de voluntários da ação: ")
        id_tipo_acao = input("Digite o id do novo tipo da ação: ")
        id_voluntario_responsavel = input("Digite o id do novo voluntário da ação: ")
        acaoDAO = AcaoDAO()
        sucesso = acaoDAO.atualizar(id_acao, local, num_beneficiados, num_voluntarios, id_tipo_acao, id_voluntario_responsavel)
        if sucesso == True:
            print("*** Ação atualizada com sucesso ***")
        else:
            print("*** Não foi possível atualizar esta ação ***")
        self.menu_cadastrar_acoes()

    def menu_cadastrar_acoes_remover_uma_acao(self):
        print("==========================================")
        print("Remover uma ação existente")
        print("==========================================")
        id_acao = int(input("Digite o id da ação: "))
        acaoDAO = AcaoDAO()
        sucesso = acaoDAO.remover(id_acao)
        if sucesso == True:
            print("*** Ação removida com sucesso ***")
        else:
            print("*** Não foi possível remover esta ação ***")
        self.menu_cadastrar_acoes()
