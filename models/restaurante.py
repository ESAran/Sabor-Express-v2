class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   GREY = '\033[90m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
# Criação da Classe
class Restaurante:
    restaurantes = []

    # Construtor: define os argumentos que necessários para criação do Objeto.
    def __init__(self, nome, categoria):
        self._nome = nome.capitalize()
        self._categoria = categoria.capitalize()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    # Método que determina como o Objeto vai ser exibido como string
    def __str__(self):
        return f'{self._nome}, {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('\n ___________________________________________________________________________________')
        print(f'|{color.UNDERLINE} {'Nome'.ljust(25)} | {'Categoria'.ljust(25)} |      {'Situação'.ljust(20)} |{color.END}')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} |')
        print('')

    @property
    def ativo(self):
        return '☑  | Em funcionamento' if self._ativo == True else '☐  | Fechado' 
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_manu = Restaurante("Manu's Risottos", 'Risotos e Massas')
restaurante_manu.alternar_estado()
restaurante_dudu = Restaurante('pizzaranria', 'Pizzaria')

Restaurante.listar_restaurantes()