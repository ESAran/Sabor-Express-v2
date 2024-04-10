from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, medida, descricao, alcolica=False):
        """
        #### Bebidas dos restaurantes

        Args:
            nome (string): nome da bebida
            preco (float): preco da bebida
            medida (integer): medida da bebida em ml
            descricao (string): descrição breve 
            alcolica (bool, optional): Bebida Alcólica. Padrão: False.
        """
        super().__init__(nome, preco, medida, descricao)
        self._alcolica = alcolica

    @property
    def tipo_bebida(self):
        return 'Alcólica' if self._alcolica == True else 'Não Alcólica'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.1)