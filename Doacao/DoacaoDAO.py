import traceback
import psycopg2
from Doacao.Doacao import Doacao
import PsycopgParameters

class DoacaoDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_doacao, local, num_beneficiados, num_voluntarios, id_tipo_doacao, id_acao, id_patrocinador FROM public.\"Doacao\"")
            registros = cursor.fetchall()
            for r in registros:
                d = Doacao()
                d.id_doacao = r[0]
                d.local = r[1]
                d.num_beneficiados = r[2]
                d.num_voluntarios = r[3]
                d.id_tipo_doacao = r[4]
                d.id_acao = r[5]
                d.id_patrocinador = r[6]
                resultados.append(d)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, id_doacao):
        d = None
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_doacao, local, num_beneficiados, num_voluntarios, id_tipo_doacao, id_acao, id_patrocinador FROM public.\"Doacao\" WHERE id_acao = " + str(id_doacao))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                d = Doacao()
                d.id_doacao = r[0]
                d.local = r[1]
                d.num_beneficiados = r[2]
                d.num_voluntarios = r[3]
                d.id_tipo_doacao = r[4]
                d.id_acao = r[5]
                d.id_patrocinador = r[6]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return d

    def inserir(self, local, num_beneficiados, num_voluntarios, id_tipo_doacao, id_acao, id_patrocinador):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"Doacao\" (local, num_beneficiados, num_voluntarios, id_tipo_doacao, id_acao, id_patrocinador) VALUES ('" + local + "', '" + num_beneficiados + "', '" + num_voluntarios + "', '" + id_tipo_doacao + "', '" + id_acao + "', '" + id_patrocinador + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, id_doacao, local, num_beneficiados, num_voluntarios, id_tipo_doacao, id_acao, id_patrocinador):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE public.\"Doacao\" SET local = '" + local + "', num_beneficiados = '" + num_beneficiados + "', num_voluntarios = '" + num_voluntarios + "', id_tipo_doacao = '" + id_tipo_doacao + "', id_acao = '" + id_acao + "', id_patrocinador = '" + id_patrocinador + "' WHERE id_doacao = " + str(id_doacao) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, id_doacao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM public.\"Doacao\" WHERE id_doacao = " + str(id_doacao) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
