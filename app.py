import requests

url = 'https://raw.githubusercontent.com/ESAran/Sabor-Express-v2/main/models/restaurantes.json'
response = requests.get(url)
print(response)

'''def main():
    pass

if __name__ == '__main__':
    main()'''