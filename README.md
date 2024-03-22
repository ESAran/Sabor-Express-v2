# Sabor-Express-v2

O seguinte repositório faz parte do curso **Python: aplicando a Orientação a Objetos** da [Alura](alura.com.br).

Data de conclusão: 22/03/2024

Carga horária: **6h**

* Entenda a importância da Orientação a Objetos com Python
* Descubra a importância de classes e atributos inspirado um projeto real
* Utilize métodos estáticos e encapsulamento
* Entenda como as propriedades como elas podem conter lógica adicional além de simplesmente acessar e atribuir valores
* Compreenda como as classes no Python podem organizar e estruturar seu código de forma eficiente
* Aprenda a usar o construtor para inicializar objetos e definir seus estados iniciais

link do curso: [Python: aplicando a Orientação a Objetos](https://cursos.alura.com.br/course/python-aplicando-orientacao-objetos "Curso Alura")

![Static Badge](https://img.shields.io/badge/Git_e_GitHub-grey?logo=github) ![Static Badge](https://img.shields.io/badge/Python-blue?logo=python&logoColor=yellow)

---

# Programa

O programa consiste em uma versão do aplicativo [Sabor Express](https://github.com/ESAran/Sabor-Express) com paradiga de programação orientada a objetos.

> O aplicativo foi realizado de forma simples, não tendo como objetivo ser uma versão finalizada do anterior, mas somente para utilização e aprendizado da estrutura orientada.

### Arquivos

Possui os arquivos de `app.py`, `avaliacao.py` e `restaurante.py` com suas respectivas funções.

A classe Avaliação se conecta na classe Restaurante, podendo gerar uma nota do mesmo através das média obtida.

#### restaurante.py

```python
class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente.capitalize()
        self._nota = nota
```

```python
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
        if 0 <= nota <= 5:
                avaliacao = Avaliacao(cliente, nota)
                self.avaliacao .append(avaliacao)
...
```

#### app.py

Arquivo principal do programa que mostra o funcionamento dos anteriores.

![1711120813808](image/README/1711120813808.png)

```python
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
```



# Orientação a Objetos

"Como a maioria das atividades que fazemos no dia a dia, programar também possui modos diferentes de se fazer. Esses modos são chamados de **paradigmas de programação** e, entre eles, estão a **programação orientada a objetos** (POO) e a programação estruturada. Quando começamos a utilizar linguagens como [Java](https://www.alura.com.br/artigos/java), [C#](https://www.alura.com.br/curso-online-csharp-parte-2-introducao-orientacao-objetos), [Python](https://www.alura.com.br/artigos/python) e outras que possibilitam o paradigma orientado a objetos, é comum errarmos e aplicarmos a programação estruturada achando que estamos usando recursos da orientação a objetos" (Alura, 2024).

Artigo referente à o que é POO:

[POO: o que é programação orientada a objetos?](https://www.alura.com.br/artigos/poo-programacao-orientada-a-objetos?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=111087461203&hsa_ad=687448474447&hsa_src=g&hsa_tgt=dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=EAIaIQobChMIv7rR2sGDhQMVIF9IAB14aQDwEAAYASAAEgL0afD_BwE "POO Alura")

## Estrutura

Esse paradigma se baseia principalmente em dois conceitos chave: **classes** e **objetos** .

```python
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo;
        self.velocidade = 0

    def acelerar(self):
        # Codigo para acelerar o carro

    def frear(self):
        # Codigo para frear o carro

    def acenderFarol(self):
        # Codigo para acender o farol do carro
```

### Classe

a classe em si é um conceito abstrato, como um molde, que se torna concreto e palpável através da criação de um objeto. Chamamos essa criação de  *instanciação da classe* , como se estivéssemos usando esse molde (classe) para criar um objeto.

#### __ init__

O `__init__` no python é o Construtor, que define os argumentos necessários para a criação do objeto.

```python
...
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
...
```

#### __ str__

O `__str__ `é o método que determina como o Objeto vai ser exibido como string.

```python
...
    def __str__(self):
        return f'{self.nome}, {self.categoria}'
...
```

#### @property

Em Python, o decorador `@property` é usado para transformar um método em uma propriedade de uma classe.

Ele permite que um método seja acessado como atributo, sem a necessidade de chamá-lo como uma função.

```python
...
    @property
    def ativo(self):
        return 'Em funcionamento' if self._ativo == True else 'Fechado' ...
    def __str__(self):
        return f'{self.nome}, {self.categoria}'
...
```

```python
def __init__(self, nome, categoria):
	self.nome = nome
        self.categoria = categoria
        self._ativo = False
...
print(restaurante_dudu.ativo)
print(restaurante_dudu._ativo)
print(vars(restaurante_dudu))
______________________________________________________________
#retorno
Fechado
False
{'nome': 'Pizzaranria', 'categoria': 'Pizzaria', '_ativo': False}
```

#### @classmethod

O `@classmethod` é um decorador que indica que o método pertence à classe.

```python
...
    @classmethod
    def listar_restaurantes(cls):
        print(' ___________________________________________________________________________________')
        print(f'| {'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Situação'.ljust(25)} |')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)} |')
...
```
