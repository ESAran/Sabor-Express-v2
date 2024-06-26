# Sabor-Express-v2

O seguinte repositório faz parte do curso **Python: avance na Orientação a Objetos e consuma API** da [Alura](alura.com.br).

Data de conclusão: (data)

Carga horária: **8h**

* Implemente herança e classes abstratas
* Domine o conceito de polimorfismo
* Aprenda como integrar seus projetos com aplicações externas
* Entenda como criar arquivos JSON com Python de forma prática
* Crie e ative ambientes virtuais em Python

link do curso: [Python: avance na Orientação a Objetos e consuma API](https://cursos.alura.com.br/course/python-avance-orientacao-objetos-consuma-api "Curso Alura")

![Static Badge](https://img.shields.io/badge/Git_e_GitHub-grey?logo=github) ![Static Badge](https://img.shields.io/badge/Python-blue?logo=python&logoColor=yellow)

---

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

### Funções interessantes

Algumas funções interessantes para o uso de OO.

#### isinstance()

O `isinstance` em python é uma função que valida se o objeto é uma instância de uma determinada classe.

```python
    def adicionar_item_cardapio(self, item):
        # Verifica se 'item' é uma instância do ItemCardapio
        if isinstance(item, ItemCardapio):  
            self._cardapio.append(item)
```
