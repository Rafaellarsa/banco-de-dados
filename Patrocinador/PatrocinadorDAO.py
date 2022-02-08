import traceback
import psycopg2
from Patrocinador.Patrocinador import Patrocinador
import PsycopgParameters

class PatrocinadorDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_usuario, periodicidade, id_categoria_patrocinio FROM public.\"Patrocinador\"")
            registros = cursor.fetchall()
            for r in registros:
                p = Patrocinador()
                p.id_usuario = r[0]
                p.periodicidade = r[1]
                p.id_categoria_patrocinio = r[2]
                resultados.append(p)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, id_usuario):
        p = None
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_usuario, periodicidade, id_categoria_patrocinio FROM public.\"Patrocinador\" WHERE id_usuario = " + str(id_usuario))
            r = cursor.fetchone()
            if cursor.rowcount == 1:
                p = Patrocinador()
                p.id_usuario = r[0]
                p.periodicidade = r[1]
                p.id_categoria_patrocinio = r[2]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return p

#pendente
    def inserir(self, id_usuario, periodicidade, id_categoria_patrocinio):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"Patrocinador\" (id_usuario, periodicidade, id_categoria_patrocinio) VALUES ('" + id_usuario + "', '" + periodicidade + "', '" + id_categoria_patrocinio + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, id_usuario, periodicidade, id_categoria_patrocinio):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE public.\"Patrocinador\" SET periodicidade = '" + periodicidade + "', id_categoria_patrocinio = '" + id_categoria_patrocinio + "' WHERE id_usuario = " + str(id_usuario))
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
            cursor.execute("DELETE FROM public.\"Patrocinador\" WHERE id_usuario = " + str(id_usuario))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
