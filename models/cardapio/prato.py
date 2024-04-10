from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, medida, pessoas, descricao, sabor):
        """
        #### Pratos do Restaurante
        
        Args:
            nome (string): nome do prato
            preco (float): preço do prato
            medida (integer): medida em gramas
            pessoas (integer): quantidade de pessoas servidas
            descricao (string): breve descrição
            sabor (string): 'Salgado' ou 'Doce'
        """
        super().__init__(nome, preco, medida, descricao)
        if int(pessoas):
            self._pessoas = pessoas
        else: self._pessoas = None
        if sabor == 'Salgado' or 'Doce':
            self._sabor = sabor
        else: self._sabor = None

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.2)