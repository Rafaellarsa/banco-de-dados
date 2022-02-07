import traceback
import psycopg2
from TipoDoacao.TipoDoacao import TipoDoacao
import PsycopgParameters

class TipoDoacaoDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_tipo_doacao, tipo, descricao FROM public.\"Tipo_Doacao\"")
            registros = cursor.fetchall()
            for r in registros:
                td = TipoDoacao()
                td.id_tipo_doacao = r[0]
                td.tipo = r[1]
                td.descricao = r[2]
                resultados.append(td)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, id_tipo_doacao):
        td = None
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_tipo_doacao, tipo, descricao FROM public.\"Tipo_Doacao\" WHERE id_tipo_doacao = " + str(id_tipo_doacao))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                td = TipoDoacao()
                td.id_tipo_doacao = r[0]
                td.tipo = r[1]
                td.descricao = r[2]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return td

    def inserir(self, tipo, descricao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"Tipo_Doacao\" (tipo, descricao) VALUES ('" + tipo + "', '" + descricao + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, id_tipo_doacao, tipo, descricao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE public.\"Tipo_Doacao\" SET tipo = '" + tipo + "', descricao = '" + descricao + "' WHERE id_tipo_doacao = " + str(id_tipo_doacao))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, id_tipo_doacao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM public.\"Tipo_Doacao\" WHERE id_tipo_doacao = " + str(id_tipo_doacao))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
