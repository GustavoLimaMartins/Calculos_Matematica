'''Gustavo Lima Martins
Email: gustavolimamartins2018@gmail.com
Data de nascimento: 24/05/1999
Faculdade: Faculdade de Tecnologia Termomecanica
Curso: Engenharia de Controle e Automação'''

try:
    range_matriz = int(input("Matriz 2x2 - Digite o número 1\nMatriz 3x3 - Digite o número 2\nMatriz 4x4 - Digite o número 3\nEscreva o valor: "))
    if range_matriz > 3 or range_matriz <= 0:
        print("Tente novamente! Digite um número entre 1 e 3...")
except:
    print("Tente novamente! Apenas números inteiros são aceitos...")

if range_matriz == 1:
    print("Matriz selecionada: \n[a, b]\n[c, d]")
    try:
        a = input("Digite o valor de (a): ")
        b = input("Digite o valor de (b): ")
        c = input("Digite o valor de (c): ")
        d = input("Digite o valor de (d): ")
        m_2x2 = [a, b, c, d]
        d_principal = float(a) + float(d)
        d_secundaria = float(b) + float(c)
    except:
        print("Tente novamente! Apenas números são aceitos...")

    print("\nNa matriz: {}\nA diferença entre a diagonal principal e a secundária é: {:.0f}" .format(m_2x2, (d_principal-d_secundaria)))

elif range_matriz == 2:
    print("Matriz selecionada: \n[a, b, c]\n[d, e, f]\n[g, h, i]")
    try:
        a = input("Digite o valor de (a): ")
        b = input("Digite o valor de (b): ")
        c = input("Digite o valor de (c): ")
        d = input("Digite o valor de (d): ")
        e = input("Digite o valor de (e): ")
        f = input("Digite o valor de (f): ")
        g = input("Digite o valor de (g): ")
        h = input("Digite o valor de (h): ")
        i = input("Digite o valor de (i): ")
        m_3x3 = [a, b, c, d, e, f, g, h, i]
        d_principal = float(a) + float(e) + float(i)
        d_secundaria = float(c) + float(e) + float(g)
    except:
        print("Tente novamente! Apenas números são aceitos...")

    print("\nNa matriz: {}\nA diferença entre a diagonal principal e a secundária é: {:.0f}" .format(m_3x3, (d_principal-d_secundaria)))

elif range_matriz == 3:
    print("Matriz selecionada: \n[a, b, c, d]\n[e, f, g, h]\n[i, j, k, l]\n[m, n, o, p]")
    try:
        a = input("Digite o valor de (a): ")
        b = input("Digite o valor de (b): ")
        c = input("Digite o valor de (c): ")
        d = input("Digite o valor de (d): ")
        e = input("Digite o valor de (e): ")
        f = input("Digite o valor de (f): ")
        g = input("Digite o valor de (g): ")
        h = input("Digite o valor de (h): ")
        i = input("Digite o valor de (i): ")
        j = input("Digite o valor de (j): ")
        k = input("Digite o valor de (k): ")
        l = input("Digite o valor de (l): ")
        m = input("Digite o valor de (m): ")
        n = input("Digite o valor de (n): ")
        o = input("Digite o valor de (o): ")
        p = input("Digite o valor de (p): ")
        m_4x4 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
        d_principal = float(a) + float(f) + float(k) + float(p)
        d_secundaria = float(d) + float(g) + float(j) + float(m)
    except:
        print("Tente novamente! Apenas números são aceitos...")

    print("\nNa matriz: {}\nA diferença entre a diagonal principal e a secundária é: {:.0f}" .format(m_4x4, (d_principal-d_secundaria)))
