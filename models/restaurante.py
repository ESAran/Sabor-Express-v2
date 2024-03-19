# Criação da Classe
class Restaurante:
    restaurantes = []

    # Construtor: define os argumentos que necessita para criação do Objeto.
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    # Método que determina como o Objeto vai ser exibido como string
    def __str__(self):
        return f'{self.nome}, {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            estado = 'Em funcionamento' if restaurante.ativo == True else 'Fechado' 
            print(f'''{restaurante.nome}
 - Categoria: {restaurante.categoria}
 - {estado}''')

restaurante_manu = Restaurante("Manu's Risottos", 'Risotos e Massas')

restaurante_dudu = Restaurante('Pizzaranria', 'Pizzaria')

print('')
Restaurante.listar_restaurantes()