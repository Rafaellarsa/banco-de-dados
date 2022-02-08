class Doacao(object):
    @property
    def id_doacao(self):
        return self._id_doacao

    @id_doacao.setter
    def id_doacao(self, id_doacao):
        self._id_doacao = id_doacao

    @property
    def id_tipo_doacao(self):
        return self._id_tipo_doacao

    @id_tipo_doacao.setter
    def id_tipo_doacao(self, id_tipo_doacao):
        self._id_tipo_doacao = id_tipo_doacao
        
    @property
    def id_acao(self):
        return self._id_acao

    @id_acao.setter
    def id_acao(self, id_acao):
        self._id_acao = id_acao
        
    @property
    def id_patrocinador(self):
        return self._id_patrocinador

    @id_patrocinador.setter
    def id_patrocinador(self, id_patrocinador):
        self._id_patrocinador = id_patrocinador

    @property
    def valor_doacao(self):
        return self._valor_doacao

    @valor_doacao.setter
    def valor_doacao(self, valor_doacao):
        self._valor_doacao = valor_doacao

    @property
    def data_doacao(self):
        return self._data_doacao

    @data_doacao.setter
    def data_doacao(self, data_doacao):
        self._data_doacao = data_doacao
