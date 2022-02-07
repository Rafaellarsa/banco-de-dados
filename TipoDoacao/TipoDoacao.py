class TipoDoacao(object):
    @property
    def id_tipo_doacao(self):
        return self._id_tipo_doacao

    @id_tipo_doacao.setter
    def id_tipo_doacao(self, id_tipo_doacao):
        self._id_tipo_doacao = id_tipo_doacao

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
