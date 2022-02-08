from Voluntario.VoluntarioDAO import VoluntarioDAO
import main

class VoluntarioMenu(object):
    def menu_cadastrar_voluntarios(self):
        print("==========================================")
        print("Cadastro de Voluntários")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tListar Todos os Voluntários Existentes")
        print("2\t\tListar um Voluntário Existente")
        print("3\t\tInserir um Novo Voluntário")
        print("4\t\tAtualizar um Voluntário Existente")
        print("5\t\tRemover um Voluntário Existente")
        print("0\t\tVoltar ao Menu Principal")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            main.Voluntariado().menu_principal()
            return
        if opcao == 1:
            self.menu_cadastrar_voluntarios_listar_todos_voluntarios()
            return
        if opcao == 2:
            self.menu_cadastrar_voluntarios_listar_um_voluntario()
            return
        if opcao == 3:
            self.menu_cadastrar_voluntarios_inserir_um_voluntario()
            return
        if opcao == 4:
            self.menu_cadastrar_voluntarios_atualizar_um_voluntario()
            return
        if opcao == 5:
            self.menu_cadastrar_voluntarios_remover_um_voluntario()
            return
        self.menu_cadastrar_voluntarios()

    def menu_cadastrar_voluntarios_listar_todos_voluntarios(self):
        print("==========================================")
        print("Listar Todos os Voluntários Existentes")
        print("==========================================")
        voluntarioDAO = VoluntarioDAO()
        voluntarios = voluntarioDAO.listar_todos()
        for v in voluntarios:
            print("*** Id: " + str(v.id_usuario) + " - Data de início: " + v.data_inicio + " ***")
        print("*** " + str(len(voluntarios)) + " voluntário(s) encontrado(s) ***")
        self.menu_cadastrar_voluntarios()

    def menu_cadastrar_voluntarios_listar_um_voluntario(self):
        print("==========================================")
        print("Listar um Voluntário Existente")
        print("==========================================")
        codigo = int(input("Digite o código do voluntário: "))
        voluntarioDAO = VoluntarioDAO()
        voluntario = voluntarioDAO.listar(codigo)
        if voluntario is not None:
            print("*** Id: " + str(voluntario.id_usuario) + " - Data de início: " + voluntario.data_inicio + " ***")
        else:
            print("*** Não foi possível localizar este voluntário ***")
        self.menu_cadastrar_voluntarios()

    def menu_cadastrar_voluntarios_inserir_um_voluntario(self):
        print("==========================================")
        print("Inserir um Novo Voluntário")
        print("==========================================")
        id_usuario = int(input("Digite o id do novo voluntário: "))
        data_inicio = input("Digite a data de início do novo voluntário: ")
        voluntarioDAO = VoluntarioDAO()
        sucesso = voluntarioDAO.inserir(id_usuario, data_inicio)
        if sucesso == True:
            print("*** Voluntário inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este voluntário ***")
        self.menu_cadastrar_voluntarios()

    def menu_cadastrar_voluntarios_atualizar_um_voluntario(self):
        print("==========================================")
        print("Atualizar um Voluntário Existente")
        print("==========================================")
        id_usuario = int(input("Digite o id do voluntário: "))
        data_inicio = input("Digite a nova data de início do voluntário: ")
        voluntarioDAO = VoluntarioDAO()
        sucesso = voluntarioDAO.atualizar(id_usuario, data_inicio)
        if sucesso == True:
            print("*** Voluntário atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este voluntário ***")
        self.menu_cadastrar_voluntarios()

    def menu_cadastrar_voluntarios_remover_um_voluntario(self):
        print("==========================================")
        print("Remover um voluntário existente")
        print("==========================================")
        id_usuario = int(input("Digite o id do voluntário: "))
        voluntarioDAO = VoluntarioDAO()
        sucesso = voluntarioDAO.remover(id_usuario)
        if sucesso == True:
            print("*** Voluntário removido com sucesso ***")
        else:
            print("*** Não foi possível remover este voluntário ***")
        self.menu_cadastrar_voluntarios()
