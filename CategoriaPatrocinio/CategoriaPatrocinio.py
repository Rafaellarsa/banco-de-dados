class CategoriaPatrocinio(object):
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha