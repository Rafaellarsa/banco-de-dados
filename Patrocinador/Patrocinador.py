class Patrocinador(object):
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def periodicidade(self):
        return self._periodicidade

    @periodicidade.setter
    def periodicidade(self, periodicidade):
        self._periodicidade = periodicidade

    @property
    def id_categoria_patrocinio(self):
        return self._id_categoria_patrocinio

    @id_categoria_patrocinio.setter
    def id_categoria_patrocinio(self, id_categoria_patrocinio):
        self._id_categoria_patrocinio = id_categoria_patrocinio
