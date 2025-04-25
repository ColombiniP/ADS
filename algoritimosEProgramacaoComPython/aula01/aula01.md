# Introdução à lógica de programção e ao ambiente Python

## Introdução
	
Vamos estudar e resolver desafios lógicos e estratégias para a criação de aplicativos de computadores, e treinar nesso pensamento para a programação de computadores, teremos contato com o ambitente e a linguagem Python.

## Resolução de desafios lógicos

Lógica é um fenomeno humano usado para explicar as relações e causalidades (padrões) observados na natureza.

O termo **lógica** foi definido na Grécia antiga por Aristóteles que definiu que o raciocícinio pode ser representado por declarações (**premissas**) que descreve fatos ou conhecimento de senso comum.

Na matemática também temos a **lógica** aplicada, em **demonstrações de teoremas**
- X = A
- Y = A
- Logo, X = Y


## A lógica e a resolução de problemas

Métodos de **aplicação de lógica**  
- Método dedutivo
- Método indutivo

Esses dois métodos são largamente aplicados na resolução de ***problemas***, e temos os seguintes passos:  

> Russell e Norving(2013)  

1. Enunciar o problema  

	Enunciar significa descrever o problema ou ainda o objetivo que se deseja obter, não usamos expressões ou palavras vagas e ou descrições emocionais, o enunciado é objetivo

2. Descrever todas as partes constituintes do problema

	Decompomos o enunciado em partes lógicas, essas partes são declarações (**premissas**) do problema e formam todo o conhecimento **verdadeiro** que se tem sobre o problema.

   - Fatos descritos no enunciado.
   - Conhecimentos de senso comum.
   - Conhecimentos técnicos referentes ao problema.
   - Relações de causa e efeito conhecidas.
   - Sujeitos que, segundo o enunciado, realizam ações.
   - Objetos que, segundo o enunciado, sofrem ações.

3. Ordenação lógica das premissas

	egra de **causa e efeito**.

   - Premissas que são reconhecidas como causa devem vir antes de premissas reconhecidas como efeitos (ou consequências).
   - Premisas que são efeitos, também podem ser causas de outras premissas que deverão ser declaradas posteriormente

4. Avaliação conclusiva

	Aqui aplicamos os métodos dedutivos ou indutivos na sequência de premissas para obtermos a solução do problema.

5. Conclusão

	Formalizamos a conclusão obtida, que agora é uma premissa válida e pode ser utilizada em outro problema. Caso não tenhamos obtido uma conclusão, retornamos ao passo 2° e verificamos a falta de premissas e seguir os passos seguintes para encontrar a solução.

### Método indutivo

Segundo ***Law (2008)*** o método de análise indutiva as premissas conduzem a uma "lei de formação"  

pela repetição de algum padrão de comportamento

Nesse modelo chegamos a uma conclusão da verdade por observação de padrões, o que é perigoso em certas situações como: Número de amostras observadas e região.

Podemos observar por exemplo, que de 5000 cisnes avistados todos eram da cor branca, e logo concluimos pela amostra observada que todos os cisnes são brancos, mas em outros lugares como na Nova Zelândia podemos observar cisnes na cor preta.

Então esse método indutivo pode levar a conclusões erradas.

### Método dedutivo

Segundo ***Law (2008)*** no método dedutivo as premisas são ordenadas em uma sequência de causa e efeito.

Nesse modelo temos um maior número de premissas, todas válidas, para gerar uma conclusão igualmente válida. É o método utilizado no ciência pois se baseia na obtenção da verdade a partir de fatos e conhecimentos que possam ser comprovados sem generalizações.

1. Todo ser humano possui DNA
2. O DNA é única e está presente em seu corpo e de seus descendentes
3. Descendentes é um ser humano gerado a partir de outrs dois seres humanos
4. Os geradores, chamamos pai e mãe
5. Os gerados, camamos filho ou filha
6. Obtemos e identificamos o DNA do ser humano por um teste que chamamos, teste de DNA
7. O teste de DNA mostra o DNA presente de um indiciduo e caracteristicas de seus geradores
8. Maria foi submetida ao teste de DNA
9. Não foi identificado caracteristicas de DNA de João no teste de Maria

Logo, João não é pai de Maria ou Maria não é filha de João. 

## Operadores lógicos

Para a construção das premissas utilizamos **operadores lógicos**, que estabelecem relações entre os elementos que compõem a premissa, conforma ***Russel e Norvig (2013)***

### Operador de IMPLICAÇÃO (A -> B)

Esse operador constitue a operação lógica CAUSA->EFEITO.
Quando A IMPLICA B (A -> B), isso significa que se A (CAUSA) for verdadeiro, B (EFEITO) necessariamente é verdadeiro.

Vejamos a tabela verdade do operador de implicação:

||||
|---|---|---|
|A|B|A->B|
|F|F|V|
|F|V|V|
|V|V|V|
|V|F|F|

O operador A B somente é falso (F) quando A é verdadeiro e B é falso

Explicação do [**modus ponens**](https://www.youtube.com/watch?v=7qFNuku7wUk)

### Operdor OU (A + B)

Nesse operador A OU B (A + B) dizemos que para uma premissa ser verdadeira podemos ter: 
A é verdadeiro e B é falso;
A é falso e B é verdadeiro;
A e B são verdadeiros;

Vejamos a tabela verdade do operador OU

||||
|---|---|---|
|A|B|A + B|
|F|F|F|
|F|V|V|
|V|V|V|
|V|F|V|

O operador A + B só é falso se os dois A e B forem falsos juntos.

### Operador E (A . B)

Nesse operador A E B (A . B) dizemos que a premissa e o efeito necessariamente precisam ser verdadeiros juntos, se um dos dois for falso, toda a proposição é falsa
A é veradeiro E B é verdadeiro;

Vejamos a tabela verdade do operador E

||||
|---|---|---|
|A|B|A . B|
|F|F|F|
|F|V|F|
|V|V|V|
|V|F|F|

O operador A . B é verdadeiro somente quando A é verdade e B também é verdade

### Operador de NEGAÇÃO (~A)

Operador de negação de A, NÃO A (~A) causa a inversão da premissa, significa por exemplo, se A é verdade, ~A é falso

Vejamos a tabela verdade do operador ~ 

|||
|---|---|
|A|~A|
|F|V|
|V|F|

## Estratégia de desenvolvimento de programas de computadores

Atualmente os computadore não tem a capacidade de por si mesmos criar e desenvolver programas para executar tarefas, é necessário que um programador crie o programa para que o computador execute uma determinada tarefa.

O programador usa de lógica para a criação de programas, ordenando de forma sequencial e precisas, também chamado de comandos, as instruções para o computador executar suas tarefas.

A programação é o processo de registrar na memória da máquina essa sequência de comandos, escrita em uma linguagem de programação.

Damos o nome de algoritmo a essa sequência de passos gravados na memória da máquina.

## Algoritmos

De acordo com ***Cormen et al. (2012)***, um **algoritmo** é uma sequência de instruções, escritas de forma clara, ordenada e finita, e elaborada para realizar uma determonada tarefa ou resolver um problema.

Segundo ***Cormen (2014)***, a criação de algoritmos obedece à sequência descrita a seguir.


1. Descrição do problema ou tarefa a ser feita

	Uma descrição clara e objetiva definindo com precisão qual a tarefa a ser realizada.

2. Decompor a tarefa ou problema em todas as ações necessárias 

	Deve-se relacionar todos os itens necessários para a realização. Nenhuma instrução (ação) pode ser esquecida ou implicitamente entendida

3. Ordenação lógica das ações

	Deve-se proceder à ordenação das ações de modo que, ao final, a terefa esteja resolvido com sucesso.

4. Conclusão

	Deve-se avaliar a sequência de instruções determinando se o objetivo foi alcançado
	Esse teste é conhecido como teste de mesa

## O ambiente de programação Python e as características da linguagem

O processo de transformar um algoritmo em um programa de computador é conhecido como **codificação**.

Programa corresponde à transcrição da sequência de instruções do algoritmo em uma sequência de instruções de máquina, gerando um programa que pode ser executado pelo computador.

No universo de linguagens de programação disponíveis, veremos uma que seja mais próxima do entendimento humano, o que torna o processo de codificação mais fácil, essa linguagem é o Python. 

## Introdução ao Python

Criado em 1991 por Guido Van Rossum, [Python](https://www.python.org/) é hoje uma das linguagens mais utilizadas no mundo.

Seu grande sucesso se deve a baixa curva de aprendizagem e facilidade para a programação

Algumas de suas vantagens segundo ***Maruch e Maruch (2006)***

- Liguagem clara e simples
- Linguagem [Multiparadigmas](https://dev.to/dnovais/o-que-significa-ser-multi-paradigma-8ad)
	- [Procedural](https://dev.to/fernandakipper/programacao-orientada-objetos-e-programacao-procedural-qual-a-diferenca-22lj)
	- Orientada a objetos
	- Funcional
- [Linguagem interpretada](https://www.freecodecamp.org/portuguese/news/linguagens-de-programacao-interpretadas-x-compiladas-qual-e-a-diferenca/)
- Linguagem altamente portável
- linguagem de [***script***](https://pt.wikipedia.org/wiki/Linguagem_de_script#:~:text=Linguagem%20de%20script%20ou%20scripting,vez%2C%20por%20um%20operador%20humano.)

## Python: Fundamentos

Em python temos o modo iterativo, em um terminal ou prompt de comando, digite: python e você poderá digitar comandos que serão imediatamente executados, ou usa uma IDE, que é um ambiente de desenvolvimento integrado, mais recomendado pela sua facilidade de escrita e visualização, além de testes que podem ser realizados.

Precisamos entender alguns conceitos básicos que são variáveis e expressões.

As variáveis são declaradas comçando com uma letra:

```py
x = 2
y = 3
z = x + y 
#RESULTADO z = 5
```

Vemos x, y e z, essas letras são variáveis, são espaços alocados na memória da máquina que guardam valores a ser utilizados ao longo do programa, o ideal é que os nomes das variáveis sejam declarativos.

```py
numb = 10
name = "Paschoal"
area_do_quadrado = base * altura

# Nomes declarativos que explicam o que fazem
```

Python é uma linguagem que infere o tipo das variáveis automaticamente, tipos são dados que tem caracteristicas especificas, como por exemplo:

- Tipo númerico (1 ou 1.5)
- Tipo de caracteres ('a' ou "a" )
- Tipo String (sequêcia de caracteres) ("Essa é uma única string", ou 'Essa também é uma única string')
- Tipo lógico ou booleano (```True``` ou ```False```)

Em algumas linguagens é necessário a declaração explicita do tipo do dados gravado em uma variável, em Python não é declarado.

As funções e instruções são blocos de código que retornam um valor ou executam uma ação.

Esxistem instruções já pré definidas, que são carregadas junto com a linguagem e você também pode escrever suas próprias instruções, por exemplo: 

- Entrada de dados, pede ao usuário alguma informação
	```py
	nome_da_variavel = input("Digite seu nome")
	```
	Pede ao usuário que digite um valor e salva na variável

- Saída de dados, escreve alguma informação ao usuário
	```py
	print("Olá Usuário!")
	```
	Escreve na tela uma informação ao usuário

- Soma de dois valores numéricos (função personalizada)
	```py
	def soma(a,b):
		return a + b

	print(soma(3,5))
	# Resultado na tela é a soma de 3+5 = 8
	```
## Programa Python

Usando uma IDE, podemos escrever um programa que calcule a área de quadra, que é dado pela formula A = B * H

Em Python esse programa ficaria assim:

```py
def areaDoQuadrado(base,altura):
	area = base * altura
	return area

area_do_quadrado = areaDoQuadrado(10,12)
print(area_do_quadrado)
# Resultado = 120
``` 

Para rodar esse programa, em seu terminal ou prompt de comando, vá até a pasta que escreveu o código, e digite python3 nome_do_arquivo.py