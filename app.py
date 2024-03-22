from models.restaurante import Restaurante

restaurante_manu = Restaurante("Manu's Risottos", 'Risotos e Massas')
restaurante_manu.alternar_estado()
restaurante_manu.receber_avaliacao('Eduardo', 5)
restaurante_manu.receber_avaliacao('Manuella', 5)

restaurante_dudu = Restaurante('pizzaranria', 'Pizzaria')
restaurante_dudu.receber_avaliacao('Manuella', 2)
restaurante_dudu.receber_avaliacao('Eduardo', 5)
restaurante_dudu.receber_avaliacao('Alfredo', 4)
restaurante_dudu.alternar_estado()

hamburgueria = Restaurante('Merdero', 'Hamburgueria')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()