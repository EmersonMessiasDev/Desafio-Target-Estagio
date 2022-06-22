'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

entrada = int(input('Digite um numero: '))
num1 =0
num2 =1
fibonacci = []

cont = 3
while cont <= entrada:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    fibonacci.append(num3)
    cont += 1
if entrada not in fibonacci:
    print(f'O numero {entrada} não pertence a sequência')
else:
    print(f'O numero {entrada} pertence a sequência')
    
