import traceback
import psycopg2
from Acao.Acao import Acao
import PsycopgParameters

class AcaoDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_acao, local, num_beneficiados, num_voluntarios, id_tipo_acao, id_voluntario_responsavel FROM public.\"Acao\"")
            registros = cursor.fetchall()
            for r in registros:
                a = Acao()
                a.id_acao = r[0]
                a.local = r[1]
                a.num_beneficiados = r[2]
                a.num_voluntarios = r[3]
                a.id_tipo_acao = r[4]
                a.id_voluntario_responsavel = r[5]
                resultados.append(a)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, id_acao):
        a = None
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_acao, local, num_beneficiados, num_voluntarios, id_tipo_acao, id_voluntario_responsavel FROM public.\"Acao\" WHERE id_acao = " + str(id_acao))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                a = Acao()
                a.id_acao = r[0]
                a.local = r[1]
                a.num_beneficiados = r[2]
                a.num_voluntarios = r[3]
                a.id_tipo_acao = r[4]
                a.id_voluntario_responsavel = r[5]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return a

    def inserir(self, local, num_beneficiados, num_voluntarios, id_tipo_acao, id_voluntario_responsavel):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"Acao\" (local, num_beneficiados, num_voluntarios, id_tipo_acao, id_voluntario_responsavel) VALUES ('" + local + "', '" + num_beneficiados + "', '" + num_voluntarios + "', " + id_tipo_acao + ", " + id_voluntario_responsavel + ")")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, id_acao, local, num_beneficiados, num_voluntarios, id_tipo_acao, id_voluntario_responsavel):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE public.\"Acao\" SET local = '" + local + "', num_beneficiados = '" + num_beneficiados + "', num_voluntarios = '" + num_voluntarios + "', id_tipo_acao = " + id_tipo_acao + ", id_voluntario_responsavel = " + id_voluntario_responsavel + " WHERE id_acao = " + str(id_acao))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, id_acao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM public.\"Acao\" WHERE id_acao = " + str(id_acao))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
