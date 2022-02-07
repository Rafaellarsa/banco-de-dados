class Doacao(object):
    @property
    def id_doacao(self):
        return self._id_doacao

    @id_doacao.setter
    def id_doacao(self, id_doacao):
        self._id_doacao = id_doacao

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, local):
        self._local = local

    @property
    def num_voluntarios(self):
        return self._num_voluntarios

    @num_voluntarios.setter
    def num_voluntarios(self, num_voluntarios):
        self._num_voluntarios = num_voluntarios

    @property
    def num_beneficiados(self):
        return self._num_beneficiados

    @num_beneficiados.setter
    def num_beneficiados(self, num_beneficiados):
        self._num_beneficiados = num_beneficiados

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
