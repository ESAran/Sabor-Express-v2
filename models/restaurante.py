from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio
from sys import platform

# Criação da Classe
class Restaurante:
    restaurantes = []

    # Construtor: define os argumentos que necessários para criação do Objeto.
    def __init__(self, nome, categoria):
        self._nome = nome.capitalize()
        self._categoria = categoria.capitalize()
        self._ativo = False
        self.avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    # Método que determina como o Objeto vai ser exibido como string
    def __str__(self):
        return f'{self._nome}, {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('\n _____________________________________________________________________________________________________')
        print(f'|\033[4m {'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(15)} |      {'Situação'.ljust(20)} |\033[0m')
        ultimo_item = cls.restaurantes[-1]
        for restaurante in cls.restaurantes:
            if restaurante == ultimo_item:
                print(f'|\033[4m {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(15)} | {restaurante.ativo.ljust(25)} |\033[0m')
            else:
                print(f'| {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(15)} | {restaurante.ativo.ljust(25)} |')
        print('')

    @property
    def ativo(self):
        return '☑  | Em funcionamento' if self._ativo == True else '☐  | Fechado' 
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
                avaliacao = Avaliacao(cliente, nota)
                self.avaliacao .append(avaliacao)



    @property
    def media_avaliacoes(self):
        if not self.avaliacao:
            return ' -  |'
        soma_notas = sum(avaliacao._nota for avaliacao in self.avaliacao)
        quantidade_notas = len(self.avaliacao)
        media_notas = round(soma_notas / quantidade_notas, 1)
        if platform == 'darwin':
                if 0 <= media_notas < 0.5:
                        return f'{media_notas} | ☆☆☆☆☆'
                elif 0.5 <= media_notas < 1:
                        return f'{media_notas} | ✰☆☆☆☆'
                elif 1 <= media_notas < 1.5:
                        return f'{media_notas} | ★☆☆☆☆'
                elif 1.5 <= media_notas < 2:
                        return f'{media_notas} | ★✰☆☆☆'  
                elif 2 <= media_notas < 2.5:
                        return f'{media_notas} | ★★☆☆☆'  
                elif 2.5 <= media_notas < 3:
                        return f'{media_notas} | ★★✰☆☆'  
                elif 3 <= media_notas < 3.5:
                        return f'{media_notas} | ★★★☆☆'  
                elif 3.5 <= media_notas < 4:
                        return f'{media_notas} | ★★★✰☆'  
                elif 4 <= media_notas < 4.5:
                        return f'{media_notas} | ★★★★☆'  
                elif 4.5 <= media_notas < 5:
                        return f'{media_notas} | ★★★★✰'
                elif media_notas == 5:
                        return f'{media_notas} | ★★★★★'
        else:
                if 0 <= media_notas < 0.5:
                        return f'{media_notas} | ✰✰✰✰✰'
                elif 0.5 <= media_notas < 1:
                        return f'{media_notas} | ☆✰✰✰✰'
                elif 1 <= media_notas < 1.5:
                        return f'{media_notas} | ★✰✰✰✰'
                elif 1.5 <= media_notas < 2:
                        return f'{media_notas} | ★☆✰✰✰'  
                elif 2 <= media_notas < 2.5:
                        return f'{media_notas} | ★★✰✰✰'  
                elif 2.5 <= media_notas < 3:
                        return f'{media_notas} | ★★☆✰✰'  
                elif 3 <= media_notas < 3.5:
                        return f'{media_notas} | ★★★✰✰'  
                elif 3.5 <= media_notas < 4:
                        return f'{media_notas} | ★★★☆✰'  
                elif 4 <= media_notas < 4.5:
                        return f'{media_notas} | ★★★★✰'  
                elif 4.5 <= media_notas < 5:
                        return f'{media_notas} | ★★★★☆'
                elif media_notas == 5:
                        return f'{media_notas} | ★★★★★'
                
    def adicionar_item_cardapio(self, item):
        # Verifica se é uma instância do item
        if isinstance(item, ItemCardapio):  
            self._cardapio.append(item)

    @classmethod
    def listar_restaurantes(cls):
        print('\n _____________________________________________________________________________________________________')
        print(f'|\033[4m {'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(15)} |      {'Situação'.ljust(20)} |\033[0m')
        ultimo_item = cls.restaurantes[-1]
        for restaurante in cls.restaurantes:
            if restaurante == ultimo_item:
                print(f'|\033[4m {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(15)} | {restaurante.ativo.ljust(25)} |\033[0m')
            else:
                print(f'| {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(15)} | {restaurante.ativo.ljust(25)} |')
        print('')