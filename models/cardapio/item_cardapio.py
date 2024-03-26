class ItemCardapio:
    def __init__(self, nome, preco, medida, descricao):
        self._nome = nome.capitalize()
        self._preco = float(preco)
        self._medida = int(medida)
        self._descricao = descricao.capitalize()

    def __str__(self):
        return f'{self._nome} | R$ {self._preco} | {self._descricao}'