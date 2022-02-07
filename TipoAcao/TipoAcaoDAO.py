import traceback
import psycopg2
from TipoAcao.TipoAcao import TipoAcao
import PsycopgParameters

class TipoAcaoDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_tipo_acao, tipo, descricao FROM public.\"Tipo_Acao\"")
            registros = cursor.fetchall()
            for r in registros:
                ta = TipoAcao()
                ta.id_tipo_acao = r[0]
                ta.tipo = r[1]
                ta.descricao = r[2]
                resultados.append(ta)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, id_tipo_acao):
        ta = None
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id_tipo_acao, tipo, descricao FROM public.\"Tipo_Acao\" WHERE id_tipo_acao = " + str(id_tipo_acao))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                ta = TipoAcao()
                ta.id_tipo_acao = r[0]
                ta.tipo = r[1]
                ta.descricao = r[2]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return ta

    def inserir(self, tipo, descricao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"Tipo_Acao\" (tipo, descricao) VALUES ('" + tipo + "', '" + descricao + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, id_tipo_acao, tipo, descricao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE public.\"Tipo_Acao\" SET tipo = '" + tipo + "', descricao = '" + descricao + "' WHERE id_tipo_acao = " + str(id_tipo_acao))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, id_tipo_acao):
        sucesso = False
        try:
            connection = psycopg2.connect(user=PsycopgParameters.user, password=PsycopgParameters.password,
                                          host=PsycopgParameters.host, port=PsycopgParameters.port,
                                          database=PsycopgParameters.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM public.\"Tipo_Acao\" WHERE id_tipo_acao = " + str(id_tipo_acao))
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso
