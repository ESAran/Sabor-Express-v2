from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco, descricao):
        self._nome = nome.capitalize()
        self._preco = float(preco)
        self._descricao = descricao.capitalize()

    def __str__(self):
        return f'{self._nome} | R$ {self._preco} | {self._descricao}'
    
    @abstractmethod
    def aplicar_desconto(self):
            pass