import traceback
import psycopg2
from CategoriaPatrocinio.CategoriaPatrocinio import CategoriaPatrocinio
import PsycopgParameters

class CategoriaPatrocinioDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_categoria_patrocinio, categoria, descricao FROM public.\"Categoria_Patrocinio\"")
            registros = cursor.fetchall()
            for r in registros:
                cp = CategoriaPatrocinio()
                cp.id_categoria_patrocinio = r[0]
                cp.categoria = r[1]
                cp.descricao = r[2]
                resultados.append(cp)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, id_categoria_patrocinio):
        cp = None
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_categoria_patrocinio, categoria, descricao FROM public.\"Categoria_Patrocinio\" WHERE id_categoria_patrocinio = " + str(id_categoria_patrocinio))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                cp = CategoriaPatrocinio()
                cp.id_categoria_patrocinio = r[0]
                cp.categoria = r[1]
                cp.descricao = r[2]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return cp

    def inserir(self, categoria, descricao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"Categoria_Patrocinio\" (categoria, descricao) VALUES ('" + categoria + "', '" + descricao + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, id_categoria_patrocinio, categoria, descricao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE public.\"Categoria_Patrocinio\" SET categoria = '" + categoria + "', descricao = '" + descricao + "' WHERE id_categoria_patrocinio = " + str(id_categoria_patrocinio))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, id_categoria_patrocinio):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM public.\"Categoria_Patrocinio\" WHERE id_categoria_patrocinio = " + str(id_categoria_patrocinio))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
