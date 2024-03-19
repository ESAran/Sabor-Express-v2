class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_manu = Restaurante()
restaurante_manu.nome = "Manu's Risottos"
restaurante_manu.categoria = 'Risotos e Massas'

restaurante_dudu = Restaurante()

restaurantes = [restaurante_manu, restaurante_dudu]

print(restaurante_manu.ativo)

