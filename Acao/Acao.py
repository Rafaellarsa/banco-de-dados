class Acao(object):
    @property
    def id_acao(self):
        return self._id_acao

    @id_acao.setter
    def id_acao(self, id_acao):
        self._id_acao = id_acao

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, local):
        self._local = local

    @property
    def num_beneficiados(self):
        return self._num_beneficiados

    @num_beneficiados.setter
    def num_beneficiados(self, num_beneficiados):
        self._num_beneficiados = num_beneficiados

    @property
    def num_voluntarios(self):
        return self._num_voluntarios

    @num_voluntarios.setter
    def num_voluntarios(self, num_voluntarios):
        self._num_voluntarios = num_voluntarios

    @property
    def id_tipo_acao(self):
        return self._id_tipo_acao

    @id_tipo_acao.setter
    def id_tipo_acao(self, id_tipo_acao):
        self._id_tipo_acao = id_tipo_acao

    @property
    def id_voluntario(self):
        return self._id_voluntario

    @id_voluntario.setter
    def id_voluntario(self, id_voluntario):
        self._id_voluntario = id_voluntario
