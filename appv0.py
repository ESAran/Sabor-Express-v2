from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
import requests
#region CONFIGURAÇÕES RESTAURANTE 1
# Restaurante
restaurante_manu = Restaurante("Manu's Risottos", 'Risotos e Massas')
restaurante_manu.alternar_estado()

# Comidas
bebida_morango1 = Bebida('Suco de Morango', 12.00, 'Suco de morango natural feito com amor.', alcolica=False)
bebida_morango2 = Bebida('Drink de Morango', 34.00, 'Drink de morango com gin feito com amor.', alcolica=True)
bebida_abacaxi1 = Bebida('Suco de Abacaxi', 12.00, 'Suco de abacaxi natural frexxxquinho.')
prato_risoto1 = Prato('Risotto de Funghi', 115.00, 2, 'Prato romântico de risoto de funghi, especialidade da casa.', 'Salgado')
prato_risoto2 = Prato('Risotto de Limão siciliano', 115.00, 2, 'Prato romântico de risoto de limão siciliano.', 'Salgado')

# Cardapio
restaurante_manu.adicionar_item_cardapio(bebida_morango1)
restaurante_manu.adicionar_item_cardapio(bebida_morango2)
restaurante_manu.adicionar_item_cardapio(bebida_abacaxi1)
restaurante_manu.adicionar_item_cardapio(prato_risoto1)
prato_risoto2.aplicar_desconto()
restaurante_manu.adicionar_item_cardapio(prato_risoto2)

# Avaliações
restaurante_manu.receber_avaliacao('Eduardo', 5)
restaurante_manu.receber_avaliacao('Manuella', 5)
#endregion

#region CONFIGURAÇÕES RESTAURANTE 2
# Restaurante
restaurante_dudu = Restaurante('pizzaranria', 'Pizzaria')
restaurante_dudu.alternar_estado()

# Comidas
bebida_refri = Bebida('Coca-Cola (lata)', 6.00, 'Lata de refrigerante Coca-Cola',alcolica=False)
bebida_cerveja = Bebida('Corona', 15.00, 'Garrafa de cerveja Corona', alcolica=True)
prato_pizza = Prato('Pizza de Strogonoff', 85.00, 2, 'Famosa pizza de strogonoff, especialidade da casa.', 'Salgado')
prato_pizza2 = Prato('Pizzazin de Coraçãozin', 50.00, 1, 'Famosa pizzazinha de coraçãozinho pequena, especialidade da casa.', 'Salgado')
prato_pizza_doce = Prato('Pizza de Abacaxi c/ Chocolate Branco', 90.00, 2, 'Famosa pizza de abacaxi com chocolate branco, especialidade da casa.', 'Doce')

# Cardápio
restaurante_dudu.adicionar_item_cardapio(bebida_refri)
restaurante_dudu.adicionar_item_cardapio(bebida_cerveja)
prato_pizza.aplicar_desconto()
restaurante_dudu.adicionar_item_cardapio(prato_pizza)
restaurante_dudu.adicionar_item_cardapio(prato_pizza2)
restaurante_dudu.adicionar_item_cardapio(prato_pizza_doce)

# Avaliações
restaurante_dudu.receber_avaliacao('Manuella', 2)
restaurante_dudu.receber_avaliacao('Eduardo', 5)
restaurante_dudu.receber_avaliacao('Alfredo', 4)
#endregion

#region CONFIGURAÇÕES RESTAURANTE 3
hamburgueria = Restaurante('Merdero', 'Hamburgueria')
#endregion

def main():
    Restaurante.listar_restaurantes()
    restaurante_dudu.exibir_cardapio
    restaurante_manu.exibir_cardapio
if __name__ == '__main__':
    main()