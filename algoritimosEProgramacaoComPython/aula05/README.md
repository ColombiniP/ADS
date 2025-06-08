# Comando condicional

## Introdução

É inquestionável o fato de que os sistemas digitais estão constantemente tomando decisões, em frações de segundos.

A lógica de decisão adotada por uma máquina está registrada em seus circuitos de memória, ou seja, tal lógica foi reviamente elaborada e programada na máquina.

Assim, formalizar o processo de decisão que envolve qualquer tarefa que desejamos que a máquina realize constitui um importante e necessário conhecimento do programador.

## Definição dos operadores lógicos e relacionais

A essência de qualquer decisão é, em última análise, uma comparação. 

Podemos classificar nossos modos de comparação nas seguintes categorias, conforme aponta Law (2008):

- Equivalência ou similaridade: igual ou diferente.  

-  Qualidade: melhor ou pior.  

-  Dimensão: maior ou menor.  

+ Quantidade: mais ou menos, muito ou pouco.

## Operadores relacionais

Para representar as sentenças da declaração da comparação, usualmente denominada teste lógico ou condição lógica, utilizam-se os operadores relacionais: 

- A = B, A igual a B

- A ≠ B, A diferente de B

- A > B, A maior do que B

- A ≥ B, A maior ou igual a B

- A < B, A menor do que B

- A ≤ B, A menor ou igual a B

Em programação, A e B são variáveis ou constantes que serão avaliadas no momento em que a instrução de comparação for executada, conforme leciona Lutz (2011).

|**Operador relacional**|**Descrição**|**Representação em Python**|
|:----|:----:|:----:|
|A = B| A igual a B| A == B|
|A ≠ B| A Diferente de B | A != B|
|A > B| A Maior que B| A > B|
|A ≥ B| A Maior ou igual a B| A >= B|
|A < B| A Menore que B| A < B|
|A ≤ B| A Menore ou igual a B| A <= B|

## Operadores lógicos

Para a construção de testes lógicos mais completos, envolvendo mais de uma condição comparativa, utilizaremos os operadores lógicos OU, E e NÃO (NEGADO ou NEGAÇÃO). 

### Operador OU

Quando se diz A OU B, significa dizer que:  

- A condição A e a condição B podem ambas ser verdadeiras.
- A pode ser verdadeira e B falsa.
- A pode ser falsa e B verdadeira.

#### Tabela verdade para o operador OU

| A | B | A OU B |
| ---- | ---- | ---- |
| F | F | F |
| F | V | V |
| V | F | V |
| V | V | V |


O operador A ou B somente é falso (o resultado é F) quando A é falso e B é falso.

### Operador E

Trata-se do operador lógico que relaciona duas condições, A e B, que ocorrem somente juntas. Quando se diz A E B, significa dizer que A acontece (é verdadeiro) e B também necessariamente acontece (é verdadeiro). Vejamos um exemplo:

#### Tabela verdade para o operador E

| A | B | A E B |
| ---- | ---- | ---- |
| F | F | F |
| F | V | F |
| V | F | F |
| V | V | V |

O operador A . B somente é verdadeiro (o resultado é V) quando A é verdadeiro e B é verdadeiro.

### Operador de negação (não A)

Este é o operador mais simples utilizado em lógica e consiste na operação lógica de inversão do estado lógico da condição.

Quando se diz não A, ou a negação de A, significa dizer que, se A existe ou é verdadeiro, não A inexiste ou é falso. Vejamos um exemplo:

#### Tabela verdade para o operador NÃO 

| A | não A |
| --- | --- |
| F | V |
| V | F |

### Operadores lógicos e sua representação em Python

| **Operador lógico** | **Descrição** | **Representação em Python** |
| :----: | :----: | :----: |
| A ou B | A OU B | A or B *ou* A \|\| B |
| A e B | A E B | A and B *ou* A && B |
| não A | NÃO A | not A *ou* !A |


## Analisando os comandos if e if...else

O comando condicional if, do inglês “se”, é encontrado em praticamente todas as linguagens de programação de alto nível.

### Estrutura condicional if simples

A instrução if é a instrução básica em programação para a construção de decisões que a máquina vai realizar durante a execução do programa. Também chamada de fluxo de processamento.

```py
a = 10
if a > 5:
    print(a + ' é maior que 5')
```

![Imagem](https://dkrn4sk0rn31v.cloudfront.net/uploads/2020/10/Estrutura-Condicional-Simples.png)

Observe que, em Python, a tabulação e o alinhamento das instruções
definem os blocos de cada parte do comando if.

### Estrutura condicional if... else

A estrutura if... else (do inglês “se... senão”) é um legado da programação estruturada, pois orienta o fluxo da informação em um sentido “top-down”, isto é, de cima para baixo, desde o início até o fim do código.

```py
idade = int(input("Qual sua idade: "))

if idade >= 18:
    print("Entrada liberada!")
else:
    print("Somente para maiores de 18 anos!")
```

Se a condição lógica for VERDADEIRA, o Bloco *if* de comandos será executado. Se, no entanto, a condição lógica for FALSA, somente o Bloco *else* de instruções será executado.

### Estrutura condicional if... elif... else

Essa estrutura permite o encadeamento de vários testes, selecionando conjuntos diferentes de ações, de acordo com o resultado em cascata de cada condição lógica.

```py
def calculadora():
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    operacao = input("Digite a operação (+, -, /, *): ")
    
    resultado = num1
    
    if operacao == '+':
        resultado += num2
    elif operacao == '-':
        resultado -= num2
    elif operacao == '*':
        resultado *= num2
    elif operacao == '/':
        resultado /= num2
    else:
        print("Operação não reconhecida")
        
    print("O resultado é: %.f" % resultado)
```

Seguindo a mesma lógica, são executados 4 testes, e por último caso não seja passado nos 4 primeiros o bloco *else* é executado.

## [Resolução de problemas computacionais utilizando os comandos if e if... else](./resolucao.py)

Faça um programa que recebe as medidas do terreno e da garagem e a zona onde estará localizado o imóvel, calcula o percentual de ocupação da área da garagem em relação ao terreno e emite mensagem sobre o atendimento às regras de ocupação conforme o plano diretor.

```py
#Para a zona norte da cidade, o percentual máximo é de 25%.
#Para as zonas leste e oeste da cidade, o percentual máximo é de 30%.
#Para a zona sul, menos povoada, o percentual máximo é de 40%.

# Variáveis
zona_norte = 25
zona_leste = 30
zona_sul = 40

# funções
def areaTerreno(largura, profundidade):
    return largura * profundidade

def areaGaragem(largura, profundidade):
    return largura * profundidade
    
def percentOcupacao(areaGaragem, areaTerreno):
    return (areaGaragem / areaTerreno) * 100

largura_garagem_metros = float(input("Qual a largura da garagem em metros: "))
profundidade_gararem_metros = float(input("Qual a profundidade da garagem em metros: "))
areaG = areaGaragem(largura_garagem_metros, profundidade_gararem_metros)

largura_terreno_metros = float(input("Qual a largura do terreno em metros: "))
profundidade_terreno_metros = float(input("Qual a profundidade do terreno em metros: "))
areaT = areaTerreno(largura_terreno_metros, profundidade_terreno_metros)

percentual_plano = percentOcupacao(areaG, areaT)
zona_terreno = input("qual a zona de habitação - (norte=n, sul=s ou leste=l): ")

print(" ")
print("Área da garagem %2.fM" % areaG)
print("Área do terreno %2.fM" % areaT)
print('percentual destinado a garagem %2.f por cento' % percentual_plano)
print(" ")

# Condição
if zona_terreno == "n" and percentual_plano <= 25:
    print ("Dentro do padrão")
elif zona_terreno == "l" and percentual_plano <= 30:
    print ("Dentro do padrão")
elif zona_terreno == "s" and percentual_plano <= 40:
    print ("Dentro do padrão")
else:
    print("Fora do padrão")
```

Saída

```py
#Qual a largura da garagem em metros: 3
#Qual a profundidade da garagem em metros: 4
#Qual a largura do terreno em metros: 10
#Qual a profundidade do terreno em metros: 9
#qual a zona de habitação - (norte=n, sul=s ou leste=l): n
# 
#Área da garagem 12M
#Área do terreno 90M
#percentual destinado a garagem 13 por cento
# 
#Dentro do padrão
```