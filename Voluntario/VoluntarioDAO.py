import traceback
import psycopg2
from Voluntario.Voluntario import Voluntario

class VoluntarioDAO(object):
    def listar_todos(self):
        resultados = []
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, login, senha FROM pessoa")
            registros = cursor.fetchall()
            for r in registros:
                v = Voluntario()
                v.codigo = r[0]
                v.nome = r[1]
                v.login = r[2]
                v.senha = r[3]
                resultados.append(v)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar(self, codigo):
        v = None
        try:
            connection = psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, login, senha FROM pessoa WHERE codigo = " + str(codigo))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                v = Voluntario()
                v.codigo = r[0]
                v.nome = r[1]
                v.login = r[2]
                v.senha = r[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return v

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
