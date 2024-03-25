from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, medida, descricao, sabor):
        """_summary_

        Args:
            nome (string): Nome do item
            preco (float): preço do item
            medida (integer): medida do item, em gramas
            descricao (string): descrição do item
            sabor (string): "Salgado" ou "Doce"
        """
        super().__init__(nome, preco, medida, descricao)
        if sabor == 'Salgado' or 'Doce':
            self._sabor = sabor
        else: self._sabor = None

Prato()