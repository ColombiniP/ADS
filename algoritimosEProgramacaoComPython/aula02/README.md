# Tipos de dados e variáveis (utilizando Python)

## Introdução

Nessa seção vamos ver e aprender como os dados são representados internamente em um computador. Identificaremos, constantes e variáveis e como são programadas.

## Representação interna de dados em um computador

Segunfo ***Parvert (2008)*** o computador é uma máquina "burra", utilizado por uma criança inteligente.

A máquina depende de um ser humano, um programador para criar os programas e executar tarefas

O que é **o computador**? É uma máquina criada para receber e processar dados, portanto temos componentes de entrada e de saída (E/S), memória e componente de processamento (CPU)

**CPU** é o cérebro do comutador, responsável por guardar e recuperar valores da memória e executar a aritmética básica e a lógica, pela CPU passa qualquer instrução a ser executada, apesar de conseguir fazer operações em milésimos de segundos, ainda depende de um ser humano para desenvolver sua lógica.

**Memória** é outro componente fundamental. É nesse local que é armazenado valores e posteriormente recuperados, é relativamente rápido mas perde se conteúdo quando a máquina é deligada. 

**Disco rígido** é o componente que grava dados e recupera dados, parecido com a memória, é consideravelmente mais lento, e não perde dados sem energia, tem mais espaço para armazenar informações.

**Dispositivos de entrada e sáida** são os periféricos, mouse, teclado, telas, impressoras, todo hardware que se conecta à máquina para imputar dados ou receber dados processados.

A estrutura interna do computador opera com um sistema númerico com base em 2 símbolos, 0 e 1, ligado e desligado, vardadeiro ou falso. Esse sistema é chamado de sistema binário ou sistema na base 2, 

No sistema **binário** a menor unidade de informação é o ***bit*** (***binary digit***) e só tem dois valores possíves de armazenar, o 0 ou o 1. A partir de conjuntos de ***bits*** podemos representar qualquer valor.  

![Sistema Binário](https://upload.wikimedia.org/wikipedia/commons/2/2b/Convers%C3%A3o_de_Bin%C3%A1rio_para_Decimal.png)

De acordo com ***Edelweiss e Livi (2014)***, códigos mais simples armazenam caracteres em ***bytes*** (conjunto de 8 bits): <span style="background:yellow; color:black;">0100</span>  <span style="background:yellow; color:black;">0001</span>
  
Para representar carcteres (letras e caracteres especiais), criamos algumas convenções que deferencia o conjunto de ***bytes*** usada para representar o caracter. Vejamos 3 modelos:

- ASCII (7 bits por carctere): Utilizado por grande parte dos computadores e alguns periféricos, nesse padrão o ***bit*** mais a esquerda é sempre igual a 0.
  
- EBCDIC (8 bits por caractere) Utiliza 1 ***byte*** para representar cada caractere

- UNICODE (16,32 ou mais ***bits***): Abrange mais de 100.000 mil caracteres, podendo utilizar um, dois ou mais ***bytes*** para representar caracteres.


### Unidades de medida da memória

![unidades de medidia da memória](https://i.ytimg.com/vi/yK9fvJ7Mmhg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDgBrQgeGahW_WinPrsuzuKhMwyMQ)

## Definindo constantes, variáveis e seus tipos

### Variáveis e seus tipos

Conforme ***Kalb (2016)***, uma variável é uma localização de memória nomeada que possui um determinado valor. Este pode variar conforme o tempo e, por isso, é denominado variável.

Pense na memória como um escaninho, vários espaços que servem para armazenar informações:

![imagem de um escaninho](https://media.istockphoto.com/id/1472947169/pt/foto/wooden-accessory-case.jpg?s=612x612&w=0&k=20&c=71nHgQirUUV1xNu_4DwqgTmNuiQp9xORxt3Wji-9yfw=)

Cada caixa é um espaço na memória do computador e quando definimos uma variável, ela é alocada em um desses espaços para ser usada posteriormente pelo código que a chama pelo seu nome.

```py
# Definindo as variáveis
variavel_idade = 33
variavel_nome = "Paschoal"

# Após definir, chamamos no código no momento de usar
print(f"{variavel_nome} tem {variavel_idade} anos de idade!")

# Saída
# Paschoal tem 33 anos de idade!
```

Perceba que após definir o nome da variável, colocamos um sinal de ( = ) que atribui o valor àquela variável, sendo assim o ( = ) é o operador de atribuição.

#### Boas práticas para nomear variáveis

- Começar com letra ou underscore ( _ )
  - _variavel
  - variavel

- Não começar com dígitos
  - <span style="text-decoration:line-through;">1nome</span>

- Ter no máximo 256 carcteres

- Letras, dígitos, underscores e cifrões podem ser inseridos
  - nome1
  - $idade_limite
  
- Não conter espaços e símbolos matemáticos (+,-,*,/)

- Variáveis pode ser escritas com o padrão cammelCase e snake_case
  - nomeCompleto (cammelCase)
  - nome_completo (snake_case)

Uma variável também pode receber como valor outra variável, vejamos:

```py
# Operação de soma
a = 5
b = 3

# z é uma variávez que recebe as variáveis, a e b e faz uma operação aritmérica de soma
z = a + b
```
Cada dado que adicionamos as variáveis possuem um tipo, esses tipos são chamados imutáveis e comportam valores específicos, vejamos: 

### Tipos booleanos
- `bool`: Só assume valores de vardadeiro (```True```) ou falso (```False```).  

### [Tipos numéricos](https://www.w3schools.com/python/python_numbers.asp)
- `int`: São objetos númericos e em Python tem um tamanho arbtrário, sendo possível calcular números que os resultados são grandes valores.
- `float`: Representa números reais racionais, `2.12, 10.51, ....` chamdos números de ponto flutuante, são decimáis e possuem 64 dígitos binários de precisão.
- `complex`: Representa números complexos.

---
- `None`: Represa um lugar reservado vázio; apenas ocupa espaço e a variável não tem valor atribuido.

### [Tipos texto](https://www.w3schools.com/python/python_strings.asp)
- `str`: Dado utilizado para representar texto; sequência de caracteres(strings) são declaradas a partir do uso de aspas simples ou duplas.

---
- [`tuple`](https://www.w3schools.com/python/python_tuples.asp): São usadas para armazenar vários itens em uma única variável. Usa-se () e separa os dados armazenados por vírgula. ```("Banana", "Maçã", "Ameixa")```
- `type`: Objetos utilizados para a manipulação de tipos.

### Constantes

As constantes representam dados ou objetos que não mudam seu valor ao longo da execução de um software.

Em **Python** as constantes normalmente são declaradas e disponibilizada em um **módulo**. módulo é um arquivo separado do código principal que armazena variáveis, funções, etc., que são importados para o arquivo principal.

Exemplo.:

```py
# Constante para o valor de PI
PI = 3.14159

# Constante para a gravidade
GRAVIDADE = 9.8

# Exemplo de uso
raio = 5
area_do_circulo = PI * raio**2
print(f"A área do círculo é: {area_do_circulo}")
```

As constantes são escritas em letras maiúsculas e underscore ( _ ) caso tenha mais de uma palavra no nome da constante.

```NOME_COMPLETO = "Paschoal Colombini"```

Esse valor vai permanecer o mesmo até o fim da execução do código, por convenção, já que Python não impede de valores constantes serem reatribuidos, mas o próximo programador que ver a variável escrita dessa forma vai saber que os valores não devem ser alterados