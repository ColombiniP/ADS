# Atribuição e operadores aritméticos (Python)

## Introdução

Os operadores são símbolos utilizados para escrever expressões; eles são essenciais para o desenvolvimento de algortmos em qualquer linguagem de programação.

Veremos os operadores de atribuição e aritiméticos em Python.

## Guia de consulta rápida aos operadores de atribuição e aos operadores aritméticos em Python

### Operador de atribuição simples

- ***( = )***: O igual tem a função de atribuir um determinado valor ou uma expressão a uma variável.

    nome_da_variavel ( = ) valor_ou_expressao_a_ser_atribuido

    \>>> igualdade = 23  
    \>>> igualdado  
    23

### Operadores de atribuição compostos

- ***( += )***: Operador de atribuição de adição, soma e atribui o novo valor a uma variável

    valor_1 += valor_2  
    \>>> a = 1  
    \>>> a += 2  
    \>>> a  
    3

- ***( -= )***: Operador de atribuição de subtração, subtrai e atribui o novo valor a uma variável

    valor_1 -= valor_2  
    \>>> a = 5  
    \>>> a -= 2  
    \>>> a  
    3

- ***( \*= )***: Operador de atribuição de multiplicação, multiplica e atribui o novo valor a uma variável

    valor_1 *= valor_2  
    \>>> a = 2  
    \>>> a *= 3  
    \>>> a  
    6

- ***( /= )***: Operador de atribuição de divisão, divide e atribui o novo valor a uma variável

    valor_1 /= valor_2  
    \>>> a = 10  
    \>>> a /= 5  
    \>>> a  
    2

- ***( %= )***: Operador de atribuição de modulo, divide e atribui o resto da divisão ao novo valor de uma variável

    valor_1 %= valor_2  
    \>>> a = 10  
    \>>> a /= 3  
    \>>> a  
    1

- ***( \*\*= )***: Operador de atribuição de exponenciação, eleva e atribui o novo valor de uma variável

    valor_1 **= valor_2  
    \>>> a = 2  
    \>>> a **= 3  
    \>>> a  
    8

- ***( //= )***: Operador de atribuição de divisão inteiro, retorna o valo inteiro da divisão e atribui o novo valor a uma variável

    valor_1 //= valor_2  
    \>>> a = 10  
    \>>> a //= 3  
    \>>> a  
    3

### Operadores aritméticos

- ***( + )***: Operador adição, soma dois valores

    valor_1 + valor_2  
    \>>> 3 + 5    
    8

- ***( - )***: Operador subtração, subtrai dois valores

    valor_1 - valor_2  
    \>>> 3 - 5    
    -2

- ***( \* )***: Operador multiplicação, multiplica dois valores

    valor_1 * valor_2  
    \>>> 3 * 5    
    15

- ***( / )***: Operador divisão, divide dois valores

    valor_1 / valor_2  
    \>>> 3 / 5    
    0.6

- ***( % )***: Operador modulo, retorna o resto da divisão de dois valores

    valor_1 % valor_2  
    \>>> 3 % 5    
    3

- ***( // )***: Operador de divisão inteiro, retorna o valor inteiro da divisão de dois valores

    valor_1 // valor_2  
    \>>> 3 // 5    
    0

- ***( \*\* )***: Operador potência, retorna o valor exponencial de uma base e um expoente de dois valores

    valor_1 \*\* valor_2  
    \>>> 3 \*\* 5    
    234

### Regras de prioridade

- Parêntese mais interno para o mais externo
- Grupo de operadores que vierem primeira a partir desta ordem:
    
    - (\*\*) 
    - (//)(%) 
    - (*)(/) 
    - (+)(-)

## [Teste de mesa](https://pt.wikipedia.org/wiki/Teste_de_mesa)

Quando desenvolvemos um código, muitas vezes é necessário que validemos se o código é funcional. Os testes garantem que eliminamos uma série de erros que poderiam trazer um resultado inesperado ao código. Testes realizados durante a fase de desenvolvimento são conhecidos como **teste de mesa** conforme leciona Schach (2009).

Nos testes de mesa usamos dados válidos e inválidos para ver como o código reaje tanto em caso correto quando errado.

### Procedimento para o teste de mesa

Como regra geral, o teste de mesa avalia a capacidade de um algoritmo de funcionar conforme o esperado. Se tomarmos uma expressão como exemplo, o procedimento consiste em aplicar uma série de valores de entrada no algoritmo e anotar suas saídas.

### Exemplo de aplicação do teste de mesa

Para exemplificar, uma expressão aritmética, vamos tomar a função matemática na equação 

$$
y(x) = x² + \dfrac{23(x - 1)}{4x} - 7x  
$$

Essa e função pode ser desmembrada em três partes A, B, C, sendo que a parte A representa o termo $x²$, a parte B representa $\dfrac{23(x-1)}{4x}$, e a parte C representa o termo $-7x$.

A fração da parte B ainda teve seu numerador e seu denomidador separados nas variáveis B1 e B2, respectivamente

| **Comandos em Python** | **Valores de entrada** | **Valores de saída** |**Valor esperado** |
|:----|:----:|:----:|:-----:|
|\>>> x = 1 | 1 |  |  |
|\>>> A = x**2 |  | 1 | 1 |
|\>>> B1 = 23 * ( x - 1 ) |  | 0 | 0 |
|\>>> B2 = 4 * x |  | 4 | 4 |
|\>>> B = B1 / B2 |  | 0 | 0 |
|\>>> C = -7 * x |  | -7 | -7 |
|\>>> y = A + B + C |  | -6 | -6 |

## Aplicações práticas nos problemas computacionais

Por meio de dois exemplos, será ilustrado, de forma simples, como os operadores aritméticos e de atribuição podem ser empregados na solução de problemas computacionais.

### Exemplo 1: determinando o índice de massa corporal (IMC)

O IMC é uma medida internacional usada para determinar a relação entre a
altura e o peso corporal de um indivíduo.

Formula do calculo:

$$
IMC = \dfrac{massa}{altura²}
$$

```py
def IMC():
    massa = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = massa / (altura ** 2)

    print("Seu IMC é: %2.2f" % imc)

IMC()

#Digite seu peso: 105
#Digite sua altura: 1.80
#Seu IMC é: 32.41
```

### Calculadora interativa simples

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

calculadora()

#Digite um número: 1
#Digite outro número: 2
#Digite a operação (+, -, /, *): -
#O resultado é: -1

```

