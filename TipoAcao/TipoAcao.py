class TipoAcao(object):
    @property
    def id_tipo_acao(self):
        return self._id_tipo_acao

    @id_tipo_acao.setter
    def id_tipo_acao(self, id_tipo_acao):
        self._id_tipo_acao = id_tipo_acao

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
