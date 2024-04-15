import requests, json

url = 'https://raw.githubusercontent.com/ESAran/Sabor-Express-v2/main/models/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        # identifica o nome do restaurante (company)
        nome_restaurante = item['Company']
        # verifica se já existe a estrutura do restaurante, se não cria ela
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        # adiciona dados dos restaurantes no restaurante
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else: print(f'Erro: {response.status_code}')

print(dados_restaurante['McDonald’s'])

# Cria arquivo do restaurante com os dados dele
for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'restaurantes//{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as file:
        json.dump(dados, file, ident=4)

'''def main():
    pass

if __name__ == '__main__':
    main()'''