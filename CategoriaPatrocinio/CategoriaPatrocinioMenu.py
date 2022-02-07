from CategoriaPatrocinio.CategoriaPatrocinioDAO import CategoriaPatrocinioDAO
import main

class CategoriaPatrocinioMenu(object):
    def menu_cadastrar_categorias_patrocinio(self):
        print("==========================================")
        print("Cadastro de Categorias de Patrocínio")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todas as Categorias de Patrocínio Existentes")
        print("2\t\tListar uma Categoria de Patrocínio Existente")
        print("3\t\tInserir uma Nova Categoria de Patrocínio")
        print("4\t\tAtualizar uma Categoria de Patrocínio Existente")
        print("5\t\tRemover uma Categoria de Patrocínio Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_categorias_patrocinio_listar_todas_categorias_patrocinio()
            return
        if opcao == 2:
            self.menu_cadastrar_categorias_patrocinio_listar_uma_categoria_patrocinio()
            return
        if opcao == 3:
            self.menu_cadastrar_categorias_patrocinio_inserir_uma_categoria_patrocinio()
            return
        if opcao == 4:
            self.menu_cadastrar_categorias_patrocinio_atualizar_uma_categoria_patrocinio()
            return
        if opcao == 5:
            self.menu_cadastrar_categorias_patrocinio_remover_uma_categoria_patrocinio()
            return
        self.menu_cadastrar_categorias_patrocinio()

    def menu_cadastrar_categorias_patrocinio_listar_todas_categorias_patrocinio(self):
        print("==========================================")
        print("Listar Todas as Categorias de Patrocínio Existentes")
        print("==========================================")
        categoriaPatrocinioDAO = CategoriaPatrocinioDAO()
        categoriasPatrocinio = categoriaPatrocinioDAO.listar_todos()
        for cp in categoriasPatrocinio:
            print("*** Id: " + str(cp.id_categoria_patrocinio) + " - Categoria: " + cp.categoria + " - Descrição: " + cp.descricao + " ***")
        print("*** " + str(len(categoriasPatrocinio)) + " categoria(s) de patrocínio encontrada(s) ***")
        self.menu_cadastrar_categorias_patrocinio()

    def menu_cadastrar_categorias_patrocinio_listar_uma_categoria_patrocinio(self):
        print("==========================================")
        print("Listar uma Categoria de Patrocínio Existente")
        print("==========================================")
        id_categoria_patrocinio = int(input("Digite o id da categoria de patrocínio: "))
        categoriaPatrocinioDAO = CategoriaPatrocinioDAO()
        categoriaPatrocinio = categoriaPatrocinioDAO.listar(id_categoria_patrocinio)
        if categoriaPatrocinio is not None:
            print("*** Id: " + str(categoriaPatrocinio.id_categoria_patrocinio) + " - Tipo: " + categoriaPatrocinio.categoria + " - Descrição: " + categoriaPatrocinio.descricao + " ***")
        else:
            print("*** Não foi possível localizar esta categoria de patrocínio ***")
        self.menu_cadastrar_categorias_patrocinio()

    def menu_cadastrar_categorias_patrocinio_inserir_uma_categoria_patrocinio(self):
        print("==========================================")
        print("Inserir uma Nova Categoria de Patrocínio")
        print("==========================================")
        categoria = input("Digite o nome da nova categoria de patrocínio: ")
        descricao = input("Digite a descrição da nova categoria de patrocínio: ")
        categoriaPatrocinioDAO = CategoriaPatrocinioDAO()
        sucesso = categoriaPatrocinioDAO.inserir(categoria, descricao)
        if sucesso == True:
            print("*** Categoria de Patrocínio inserida com sucesso ***")
        else:
            print("*** Não foi possível inserir esta categoria de patrocínio ***")
        self.menu_cadastrar_categorias_patrocinio()

    def menu_cadastrar_categorias_patrocinio_atualizar_uma_categoria_patrocinio(self):
        print("==========================================")
        print("Atualizar uma Categoria de Patrocínio Existente")
        print("==========================================")
        id_categoria_patrocinio = int(input("Digite o id da categoria de patrocínio: "))
        categoria = input("Digite o novo nome da categoria de patrocínio: ")
        descricao = input("Digite a nova descrição da categoria de patrocínio: ")
        categoriaPatrocinioDAO = CategoriaPatrocinioDAO()
        sucesso = categoriaPatrocinioDAO.atualizar(id_categoria_patrocinio, categoria, descricao)
        if sucesso == True:
            print("*** Categoria de Patrocínio atualizada com sucesso ***")
        else:
            print("*** Não foi possível atualizar esta categoria de patrocínio ***")
        self.menu_cadastrar_categorias_patrocinio()

    def menu_cadastrar_categorias_patrocinio_remover_uma_categoria_patrocinio(self):
        print("==========================================")
        print("Remover uma categoria de patrocínio existente")
        print("==========================================")
        id_categoria_patrocinio = int(input("Digite o id da categoria de patrocínio: "))
        categoriaPatrocinioDAO = CategoriaPatrocinioDAO()
        sucesso = categoriaPatrocinioDAO.remover(id_categoria_patrocinio)
        if sucesso == True:
            print("*** Categoria de Patrocínio removida com sucesso ***")
        else:
            print("*** Não foi possível remover esta categoria de patrocínio ***")
        self.menu_cadastrar_categorias_patrocinio()
