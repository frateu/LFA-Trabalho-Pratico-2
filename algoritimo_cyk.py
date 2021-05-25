import os

def ler_gramatica(filename="./gramatica.txt"):

    filename = os.path.join(os.curdir, filename)
    with open(filename) as gramatica:
        regras = gramatica.readlines()
        total_regras = []

        for regra in regras:
            antes, depois = regra.split(" => ")
            depois = depois[:-1].split(" | ")

            for de in depois:
                total_regras.append([antes, de])

        return total_regras

def concatenar_cyk(primeira, segunda):
    concatenado = []
    if primeira == [] or segunda == []:
        return []
    for p in primeira:
        for s in segunda:
            concatenado.append(p + s)
    return concatenado

def cyk_alg(palavra):
    total_regras = ler_gramatica()
    tamanho_palavra = len(palavra)

    tabela = [[[] for x in range(tamanho_palavra - y)] for y in range(tamanho_palavra)]
    
    for i in range(tamanho_palavra):
        for tr in total_regras:
            if str.islower(tr[1]):
                # print("entrou um " + tr[1] + " - " + palavra[i])
                if palavra[i] == tr[1]:
                    # print("entrou dois")
                    tabela[0][i].append(tr[0])

    variaveis = []
    for tr in total_regras:
        if str.isupper(tr[1]):
            variaveis.append(tr)

    for i in range(1, tamanho_palavra):
        for j in range(tamanho_palavra - i):
            for k in range(i):
                # print(tabela[k][j])
                # print(tabela[i-k-1][j+k+1])
                row = concatenar_cyk(tabela[k][j], tabela[i-k-1][j+k+1])
                # print("row: " + str(row))
                for ro in row:
                    var0 = [va[0] for va in variaveis]
                    var1 = [va[1] for va in variaveis]

                    tamanho_original = len(var1)

                    if ro in var1:
                        repeticoes = var1.count(ro)
                        for x in range(repeticoes):
                            # print("ro: " + ro)
                            # print("var1: " + str(var1))
                            if len(var1) == tamanho_original:
                                # print("original")
                                tabela[i][j].append(var0[var1.index(ro)])
                            else:
                                # print("mudou")
                                tabela[i][j].append(var0[var1.index(ro) + x])
                            # print("table: " + str(tabela[i][j]))
                            var1.pop(var1.index(ro))
    
    if 'S' in tabela[tamanho_palavra-1][0]:
        print("\nEssa palavra pertence a essa gramatica.")

        print("\n\nTabela: ")
        index = 1
        for tb in tabela:
            print(str(index) + ": " + str(tb))
            index += 1
    else:
        print("\nEssa palavra não pertence a essa gramatica.")
        
        print("\n\nTabela: ")
        index = 1
        for tb in tabela:
            print(str(index) + ": " + str(tb))
            index += 1