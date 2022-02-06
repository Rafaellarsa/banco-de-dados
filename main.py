import TipoAcao.TipoAcaoMenu
import Acao.AcaoMenu
import TipoDoacao.TipoDoacaoMenu
import Doacao.DoacaoMenu
import CategoriaPatrocinio.CategoriaPatrocinioMenu
import Usuario.UsuarioMenu
import Patrocinador.PatrocinadorMenu
import Voluntario.VoluntarioMenu

# Classe que inicia a aplicação
class Voluntariado(object):
    # Menu principal da aplicação
    def menu_principal(self):
        print("==========================================")
        print("Voluntariado")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("1\t\tCadastro de Tipos de Ação")
        print("2\t\tCadastro de Ações")
        print("3\t\tCadastro de Tipos de Doação")
        print("4\t\tCadastro de Doações")
        print("5\t\tCadastro de Categorias de Patrocínio")
        print("6\t\tCadastro de Usuários")
        print("7\t\tCadastro de Patrocinadores")
        print("8\t\tCadastro de Voluntários")
        print("0\t\tSair da Aplicação")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-8]: "))
        if opcao == 0:
            return
        if opcao == 1:
            TipoAcao.TipoAcaoMenu.TipoAcaoMenu().menu_cadastrar_tipos_acao()
            return
        if opcao == 2:
            Acao.AcaoMenu.AcaoMenu().menu_cadastrar_acoes()
            return
        if opcao == 3:
            TipoDoacao.TipoDoacaoMenu.TipoDoacaoMenu().menu_cadastrar_tipos_doacao()
            return
        if opcao == 4:
            Doacao.DoacaoMenu.DoacaoMenu().menu_cadastrar_doacoes()
            return
        if opcao == 5:
            CategoriaPatrocinio.CategoriaPatrocinioMenu.CategoriaPatrocinioMenu().menu_cadastrar_categorias_patrocinio()
            return
        if opcao == 6:
            Usuario.UsuarioMenu.UsuarioMenu().menu_cadastrar_usuarios()
            return
        if opcao == 7:
            Patrocinador.PatrocinadorMenu.PatrocinadorMenu().menu_cadastrar_patrocinadores()
            return
        if opcao == 8:
            Voluntario.VoluntarioMenu.VoluntarioMenu().menu_cadastrar_voluntarios()
            return
        self.menu_principal()

# Código principal que inicializa a aplicação
if __name__ == "__main__":
    voluntariado = Voluntariado()
    voluntariado.menu_principal()
