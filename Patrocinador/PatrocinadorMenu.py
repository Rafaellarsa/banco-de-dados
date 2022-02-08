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
        for p in patrocinadores:
            print("*** Id: " + str(p.id_usuario) + " - Periodicidade: " + p.periodicidade + " - Id da categoria de patrocínio: " + str(p.id_categoria_patrocinio) + " ***")
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
            print("*** Id: " + str(patrocinador.id_usuario) + " - Periodicidade: " + patrocinador.periodicidade + " - Id da categoria de patrocínio: " + str(patrocinador.id_categoria_patrocinio) + " ***")
        else:
            print("*** Não foi possível localizar este patrocinador ***")
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_inserir_um_patrocinador(self):
        print("==========================================")
        print("Inserir um Novo Patrocinador")
        print("==========================================")
        id_usuario = int(input("Digite o id do novo patrocinador: "))
        periodicidade = input("Digite a periodicidade do novo patrocinador: ")
        id_categoria_patrocinio = input("Digite o id da categoria de patrocínio do novo patrocinador: ")
        patrocinadorDAO = PatrocinadorDAO()
        sucesso = patrocinadorDAO.inserir(id_usuario, periodicidade, id_categoria_patrocinio)
        if sucesso == True:
            print("*** Patrocinador inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este patrocinador ***")
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_atualizar_um_patrocinador(self):
        print("==========================================")
        print("Atualizar um Patrocinador Existente")
        print("==========================================")
        id_usuario = int(input("Digite o id do patrocinador: "))
        periodicidade = input("Digite a nova periodicidade do patrocinador: ")
        id_categoria_patrocinio = input("Digite o id da nova categoria de patrocínio do patrocinador: ")
        patrocinadorDAO = PatrocinadorDAO()
        sucesso = patrocinadorDAO.atualizar(id_usuario, periodicidade, id_categoria_patrocinio)
        if sucesso == True:
            print("*** Patrocinador atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este patrocinador ***")
        self.menu_cadastrar_patrocinadores()

    def menu_cadastrar_patrocinadores_remover_um_patrocinador(self):
        print("==========================================")
        print("Remover um patrocinador existente")
        print("==========================================")
        id_usuario = int(input("Digite o id do patrocinador: "))
        patrocinadorDAO = PatrocinadorDAO()
        sucesso = patrocinadorDAO.remover(id_usuario)
        if sucesso == True:
            print("*** Patrocinador removido com sucesso ***")
        else:
            print("*** Não foi possível remover este patrocinador ***")
        self.menu_cadastrar_patrocinadores()
