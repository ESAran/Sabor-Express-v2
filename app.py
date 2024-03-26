from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

# CONFIGURAÇÕES RESTAURANTE 1
# Restaurante
restaurante_manu = Restaurante("Manu's Risottos", 'Risotos e Massas')
restaurante_manu.alternar_estado()

# Cardápio
bebida_morango1 = Bebida('Suco de Morango', 12.00, 400, 'Suco de morango natural feito com amor.')
bebida_morango2 = Bebida('Drink de Morango', 34.00, 450, 'Drink de morango com gin feito com amor.')
prato_risoto1 = Prato('Risotto de Funghi', 115.00, 700, 2, 'Prato romântico de risoto de funghi, especialidade da casa.', 'Salgado')
prato_risoto2 = Prato('Risotto de Limão siciliano', 90.00, 700, 2, 'Prato romântico de risoto de limão siciliano.', 'Salgado')

# Avaliações
restaurante_manu.receber_avaliacao('Eduardo', 5)
restaurante_manu.receber_avaliacao('Manuella', 5)

# CONFIGURAÇÕES RESTAURANTE 2
# Restaurante
restaurante_dudu = Restaurante('pizzaranria', 'Pizzaria')
restaurante_dudu.alternar_estado()

# Cardápio
bebida_refri = Bebida('Coca-Cola (lata)', 6.00, 350, 'Lata de refrigerante Coca-Cola')
bebida_cerveja = Bebida('Corona', 34.00, 450, 'Garrafa de cerveja Corona')
prato_pizza = Prato('Pizza de Strogonoff', 60.00, 1000, 2, 'Famosa pizza de strogonoff, especialidade da casa.', 'Salgado')
prato_pizza_doce = Prato('Pizza de Abacaxi c/ Chocolate Branco', 90.00, 700, 2, 'Famosa pizza de abacaxi com chocolate branco, especialidade da casa.', 'Doce')

# Avaliações
restaurante_dudu.receber_avaliacao('Manuella', 2)
restaurante_dudu.receber_avaliacao('Eduardo', 5)
restaurante_dudu.receber_avaliacao('Alfredo', 4)

# CONFIGURAÇÕES RESTAURANTE 3
hamburgueria = Restaurante('Merdero', 'Hamburgueria')

def main():
    Restaurante.listar_restaurantes()
    print(prato_risoto1)
    print(prato_pizza_doce)

if __name__ == '__main__':
    main()