# Comandos de entrada e saída (utilizando Python)

## Intro

Muitas vezes programas de computador, por meio de linguagens de programação, proveem interação entre humanos e interfaces por meio de comandos de entrada e saída de dados.

Em Python temos dois comandos responsáveis por ler os dados do teclado e exibir uma saída, respectivamente são, `input` e o `print`

## Saída de dados ultilizando a função `print()`

As linguagens de programação, incluindo o Python, disponibilizam um comando para exibir dados na saída padrão do computador para o usuário, o que pode ser em um terminal, em um console de IDE (*integrated development environment*, **interface de desenvolvimento integrado**) ou mesmo a tela do computador conforme Banin (2018). Essa mensagem pode ser uma *string* (sequência de caracteres) ou outros objetos.

### Sintaxe

Segundo Barry (2018), a sintaxe da função `print` é:

`print(*objects, sep=separator, end=end, file=sys.stdout, flush=Fals)`

**Onde os parâmetros são:**

- *objects (**obrigatório**): são os objetos que serão impressos; *strings*, variáveis ou constantes.

- sep (**opcional**): Especifica como os objetos exibidos serão separados. O padrão é ' '.

- end (**opcional**): Especifica o caractere impresso no dinal. O padrão é '\n' (quebra de linha).

- file (**opcional**): Arquivo para ser preenchido com determinado conteúdo.

- flush (**opcional**): Valor booleano para determinar se a saída é liberada (True) ou armazenada em um *buffer* (False). O padrão é False.

### Utilizando a função print()

Segundo Ramalho (2015), a partir do python3, o comando `print()` deve usar obrigatoriamente parênteses.

```python
print("Olá mundo!") # (a)

# Olá mundo! (b)
# (a) - Código com o comando print
# (b) - Resultado da impressão no prompt da IDE
```

Usando os parâmetros `sep`e `end`:

```py 

# Código
texto = "Alterando o valor de sep"
print(texto)
print("Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", sep="---")

#pula uma linha
print()

texto = "Alterando o valor de sep e end"
print(texto)
print("Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", sep="---", end="...\n")

# Saída
#
#Alterando o valor de sep
#Coluna 1 --- Coluna 2 --- Coluna 3 --- Coluna 4
#
#Alterando o valor de sep e end
#Coluna 1 --- Coluna 2 --- Coluna 3 --- Coluna 4...
```

### Sequências de escape

Escape é usando na função `print()` no Python, para que caracteres especiais ou formatações de texto seja interpretada pelo processamento do programa e ou ser exibida quando deveria ser interpretada.

| Sequência | Descrição |
| :--------: | :-------- |
| \n | Quebra de linha |
| \t | Tabulação horizontal |
| \v | Tabulação vertical |
| \\" | Aspas simples |
| \\' | Aspas duplas |
| \\\ |Barra invertida |
| \0 | Caractere nulo (Usado como terminador de string) |
| \a | Beep de alerta |

```py
# Código
print("\n\nOlá, Prezado aluno.\nTudo bem?\tVamos Aprender Python")

# Saída
#
#
#
#Olá, prezado aluno.
#Tudo bem?      Vamos aprender Python
#
```

Caracteres de escape são muito úteis para formatar uma exibição de texto na tela.

## Entrada de dados usando a função `input()`

Em Python a função `input()` permiter ler dados de uma entrada padrão - por exemplo, um teclado. O valor lido, por padrão, é uma estrig e deverá ser armazendao em uma variável.

### Sintaxe

Segundo Barry (2018) a sintaxe da função `input()` é:

*input(prompt)*

**Onde o parâmetro é:**

- prompt (**opcional**): Uma *string* que será impressa na tela em forma de mensagem.

### Utilizando a função input()

```py

#(a)
nome = input("Entre com seu nome: ")
print("Olá, " + nome + ", tudo bem?)

#Entre com seu nome: |
```
```py

#(b)
nome = input("Entre com seu nome: ")
print("Olá, " + nome + ", tudo bem?)

# Entre com seu nome: Jorge
# Olá, Jorge, Tudo bem?
```

- (a): Esperando o usuário digitar o nome;
- (b): Resultado final após a entrada da informação;

Digitando várias entradas

```py
#(a)
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
print('Olá' + nome + ' ' + sobrenome + '\nBem vindo!')
```
```py
#(b)
# Digite seu nome: Alessandro
# Digite seu sobrenome: del paraiso
```
```py
#(c)
# Olá Alessandro del paraiso
# Bem vindo!
```

- (a): Esperando o usuário digitar o nome;
- (b): entrada da informação;
- (c): Resultado final após a entrada de dados;


As entradas de dados do parâmetro prompt na função `input()` sempre retornam uma *string* isso pode ser um problema se precisar lidar com dados numéricos de uma entrada input(). Para lidar com isso podemos fazer o *casting* (conversão de tipos de dados)

```py
#input() e print() com cating
#Solicita nome, idade e altura do usuário
name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))
height = float(input('Digite sua altura (m): '))
```

Usando as funções `int()` e `float()` respectivamente, convertamos a idade para um tipo numérico inteiro e a altura para um tipo numérico decimal

```py
print('Olá ' + nome + '\n')
print('Sua idade é: ' + str(age) + ' anos.\n')
print('Sua altura é: ' + str(height) + ' metros.')
```
Usando a função `str()`convertemos novamente os tipos numéricos para *string*, é necessário pois estamos concatenando (+) pedaçõs de strings para mostrar na tela um texto único.

```py
#Digite seu nome: Carlos
#Digite sua idade: 34
#Digite sua altura: 1.80

#Olá Carlos
#Sua idade é 34 anos.
#Sua altura é 1.80 metros.
```

## Aplicações práticas das funções `input()` e `print()` e variáveis em problemas computacionais

Vamos criar um programa para converter a temperatura de graus Celsius para graus Fahrenheit e Kelvin

```py
temp_c = float(input("Digite a temperatura em graus Ceulsius: "))

temp_f = 1.8 * temp_c + 32 # Converte para Fahrenheit
temp_k = temp_c + 273.15 # Converte para Kelvin

print("Temperatura em Celsius: " + str(temp_c))
print("Temperatura em Fahrenheit: " + str(temp_f))
print("Temperatura em Kelvin: " + str(temp_k))

#Digite a temperatura em graus Ceulsius: 25
#Temperatura em Celsius: 25.0
#Temperatura em Fahrenheit: 77.0
#Temperatura em Kelvin: 298.15
```