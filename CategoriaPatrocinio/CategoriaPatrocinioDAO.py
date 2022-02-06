import traceback
import psycopg2
from CategoriaPatrocinio.CategoriaPatrocinio import CategoriaPatrocinio

class CategoriaPatrocinioDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, login, senha FROM pessoa")
            registros = cursor.fetchall()
            for r in registros:
                cp = CategoriaPatrocinio()
                cp.codigo = r[0]
                cp.nome = r[1]
                cp.login = r[2]
                cp.senha = r[3]
                resultados.append(cp)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, codigo):
        cp = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, login, senha FROM pessoa WHERE codigo = " + str(codigo))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                cp = CategoriaPatrocinio()
                cp.codigo = r[0]
                cp.nome = r[1]
                cp.login = r[2]
                cp.senha = r[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return cp

    def inserir(self, codigo, nome, login, senha):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO pessoa (codigo, nome, login, senha) VALUES (" + str(codigo) + ", '" + nome + "', '" + login + "', '" + senha + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, codigo, nome, login, senha):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("UPDATE pessoa SET nome = '" + nome + "', login = '" + login + "', senha = '" + senha + "' WHERE codigo = " + str(codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, codigo):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM pessoa WHERE codigo = " + str(codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso