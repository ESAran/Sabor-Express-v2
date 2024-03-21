from models.avaliacao import Avaliacao

# Criação da Classe
class Restaurante:
    restaurantes = []

    # Construtor: define os argumentos que necessários para criação do Objeto.
    def __init__(self, nome, categoria):
        self._nome = nome.capitalize()
        self._categoria = categoria.capitalize()
        self._ativo = False
        self.avaliacao = []
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
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao .append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self.avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self.avaliacao)
        quantidade_notas = len(self.avaliacao)
        media_notas = round(soma_notas / quantidade_notas, 1)
        if media_notas >= 0 and media_notas < 0.5:
                return '✰✰✰✰✰'
        elif media_notas >= 0.5 and media_notas < 1:
                return '☆✰✰✰✰'
        elif media_notas >= 1 and media_notas < 1.5:
                return '★✰✰✰✰'
        elif media_notas >= 1.5 and media_notas < 2:
                return '★☆✰✰✰'  
        elif media_notas >= 2 and media_notas < 2.5:
                return '★★✰✰✰'  
        elif media_notas >= 2.5 and media_notas < 3:
                return '★★☆✰✰'  
        elif media_notas >= 3 and media_notas < 3.5:
                return '★★★✰✰'  
        elif media_notas >= 3.5 and media_notas < 4:
                return '★★★☆✰'  
        elif media_notas >= 4 and media_notas < 4.5:
                return '★★★★✰'  
        elif media_notas >= 4.5 and media_notas < 5:
                return '★★★★☆'
        elif media_notas == 5:
                return '★★★★★'
