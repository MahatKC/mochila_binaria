import time
import pandas as pd
pd.set_option("display.precision", 6)

def mochila_gulosa(tamanho_mochila, beneficios, custos):

    custos_beneficios = []

    for i in range(len(beneficios)):
        if custos[i] == 0: 
            custos_beneficios.append(float('inf'))
        else:
            custos_beneficios.append(beneficios[i]/custos[i])
    
    elementos = zip(range(len(beneficios)), beneficios, custos, custos_beneficios)

    elementos_ordenados = sorted(elementos, key = lambda x: x[3], reverse=True)

    espaco_disponivel = tamanho_mochila
    i = 0
    items = []
    valor_total = 0

    while(espaco_disponivel >= 0 and i < len(elementos_ordenados)):
        if(elementos_ordenados[i][2] <= espaco_disponivel):
            items.append(elementos_ordenados[i][0]+1)
            valor_total += elementos_ordenados[i][1]
            espaco_disponivel -= elementos_ordenados[i][2]
        i += 1
        
    return valor_total, items

def mochila_dinamica(tamanho_mochila, beneficios, custos):
    matriz = []
    for i in range(len(beneficios)+1):
        temp = []
        for j in range(tamanho_mochila+1):
            temp.append(0)
        matriz.append(temp)
        
    for i in range(1, len(beneficios)+1):
        for j in range(1, tamanho_mochila+1):
            if custos[i-1] > j: # nao cabe na mochila
                matriz[i][j] = matriz[i-1][j]
            elif matriz[i][j-1] <= matriz[i-1][j-custos[i-1]]+beneficios[i-1]:
                matriz[i][j] = max(matriz[i-1][j-custos[i-1]]+beneficios[i-1], matriz[i-1][j])
            else:
                matriz[i][j] = max(matriz[i][j-1], matriz[i-1][j])
                    
    valor_total = matriz[-1][-1]
    i = len(beneficios)
    j = tamanho_mochila
    items = []
    
    while(matriz[i][j] != 0):
        if matriz[i-1][j] == matriz[i][j]:
            i -= 1
        else:
            items.append(i)
            j -= custos[i-1]
            i -= 1
    
    return valor_total, items[::-1]

def abrir_arquivo(tamanho_conjunto):
    arquivo = open("Entradas/Mochila"+str(tamanho_conjunto)+".txt", "r")
    linha_index = 0
    for linha in arquivo:
        if linha_index == 0:
            tamanho_mochila = int(linha)
            linha_index += 1
        elif linha_index == 1:
            beneficios = [int(beneficio) for beneficio in linha.split("\t")[:-1]]
            linha_index += 1
        else:
            custos = [int(custo) for custo in linha.split("\t")[:-1]]

    return tamanho_mochila, beneficios, custos

tamanhos_conjuntos = [10, 50, 100, 200, 300, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000]

for tamanho_conjunto in tamanhos_conjuntos:
    print(f"Tamanho {tamanho_conjunto}")
    tamanho_mochila, beneficios, custos = abrir_arquivo(tamanho_conjunto)
    tempo_gulosa = 0
    tempo_dinamica = 0

    for i in range(3):
        print("-"*5+f"i: {i}"+"-"*5)
        t0g = time.time()
        valor_gulosa, items = mochila_gulosa(tamanho_mochila, beneficios, custos)
        t1g = time.time()
        tempo_gulosa += t1g-t0g
        print(f"Gulosa: {t1g-t0g} segundos\nBenefício: {valor_gulosa}", end='\n\n')
        #print(f"Items: {items}")
        
        t0d = time.time()
        valor_dinamica, items = mochila_dinamica(tamanho_mochila, beneficios, custos)
        t1d = time.time()
        tempo_dinamica = t1d-t0d
        print(f"Dinâmica: {t1d-t0d} segundos\nBenefício: {int(valor_dinamica)}")
        #print(f"Items: {items}")

    results = pd.DataFrame({
            'Tamanho': [tamanho_conjunto],
            'Media Tempo Gulosa': [(tempo_gulosa/3)],
            'Beneficio Gulosa': [valor_gulosa],
            'Tamanho Tabela (MxN):': [(tamanho_conjunto+1)*(tamanho_mochila+1)],
            'Media Tempo Dinamica': [tempo_dinamica/3],
            'Media Tempo Dinamica/Milhao celulas': [(tempo_dinamica/3)/(((tamanho_conjunto+1)*(tamanho_mochila+1))/1000000)],
            'Beneficio Dinamica': [valor_dinamica]
        })
    if tamanho_conjunto==10:
        results.to_csv("Resultados.csv",index=False)
    else:
        file_df = pd.read_csv("Resultados.csv")
        file_df = pd.concat([file_df,results], ignore_index=True)
        file_df.to_csv("Resultados.csv",index=False)
    
    print("-"*10)


