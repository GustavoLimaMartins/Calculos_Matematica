'''Gustavo Lima Martins
Email: gustavolimamartins2018@gmail.com
Data de nascimento: 24/05/1999
Faculdade: Faculdade de Tecnologia Termomecanica
Curso: Engenharia de Controle e Automação'''

# 1. Fibonacci
n1 = 0
n2 = 1
n3 = 0

# Lista
fibonacci = [n1, n2]
posicao = 1

while posicao <= 8:
    n_num = fibonacci[posicao]
    ant_num = fibonacci[posicao-1]
    n3 = n_num + ant_num
    fibonacci.append(n3)
    posicao += 1

print(f"Os {len(fibonacci)} primeiros números de Fibonacci são: {fibonacci}")
