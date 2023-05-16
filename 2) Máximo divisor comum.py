'''Gustavo Lima Martins
Email: gustavolimamartins2018@gmail.com
Data de nascimento: 24/05/1999
Faculdade: Faculdade de Tecnologia Termomecanica
Curso: Engenharia de Controle e Automação'''

lista = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132]
total_div = []
divisores = []
div1 = 1

ultimo = int(lista[len(lista)-1])

while div1 <= ultimo:
    divisores.append(div1)
    div1 += 1

n_lista = 0

for i in lista:
    dividendo = int(lista[n_lista])
    n_lista += 1

    for i in divisores:
        conta = (dividendo / i)
        conta = str(conta)
        posicao = conta.find(".")

        if (conta[posicao+1] == "0" and len(conta) == 3) or conta[posicao+1] == "0" and len(conta) == 4:
            total_div.append(i)

mdc = []
for i in total_div:
    comum = total_div.count(i)

    if comum == len(lista):
        mdc.append(i)

print("O máximo divisor comum (MDC) da lista {} é {}" .format(lista, max(mdc)))
