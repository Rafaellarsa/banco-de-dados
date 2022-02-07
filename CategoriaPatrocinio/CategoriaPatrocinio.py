class CategoriaPatrocinio(object):
    @property
    def id_categoria_patrocinio(self):
        return self._id_categoria_patrocinio

    @id_categoria_patrocinio.setter
    def id_categoria_patrocinio(self, id_categoria_patrocinio):
        self._id_categoria_patrocinio = id_categoria_patrocinio

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
