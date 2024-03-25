from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, medida, descricao, alcolica=False):
        super().__init__(nome, preco, medida, descricao)
        self._alcolica = alcolica

    @property
    def tipo_bebida(self):
        return 'Alcólica' if self._alcolica == True else 'Não Alcólica'