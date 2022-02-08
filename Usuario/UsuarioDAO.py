import traceback
import psycopg2
from Usuario.Usuario import Usuario
import PsycopgParameters

class UsuarioDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_usuario, nome, cpf, email, senha, telefone FROM public.\"Usuario\"")
            registros = cursor.fetchall()
            for r in registros:
                u = Usuario()
                u.id_usuario = r[0]
                u.nome = r[1]
                u.cpf = r[2]
                u.email = r[3]
                u.senha = r[4]
                u.telefone = r[5]
                resultados.append(u)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, id_usuario):
        u = None
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_usuario, nome, cpf, email, senha, telefone FROM public.\"Usuario\" WHERE id_usuario = " + str(id_usuario))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                u = Usuario()
                u.id_usuario = r[0]
                u.nome = r[1]
                u.cpf = r[2]
                u.email = r[3]
                u.senha = r[4]
                u.telefone = r[5]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return u

    def inserir(self, nome, cpf, email, senha, telefone):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"Usuario\" (nome, cpf, email, senha, telefone) VALUES ('" + nome + "', '" + cpf + "', '" + email + "', '" + senha + "', '" + telefone + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, id_usuario, nome, cpf, email, senha, telefone):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE public.\"Usuario\" SET nome = '" + nome + "', cpf = '" + cpf + "', email = '" + email + "', senha = '" + senha + "', telefone = '" + telefone + "' WHERE id_usuario = " + str(id_usuario))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, id_usuario):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM public.\"Usuario\" WHERE id_usuario = " + str(id_usuario))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
