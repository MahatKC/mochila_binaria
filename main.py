import time


def mochila_gulosa(tamanho_mochila, beneficios, custos):

    custos_beneficios = []

    for i in range(len(beneficios)):
        custos_beneficios.append(beneficios[i]/custos[i])
    
    elementos = zip(range(len(beneficios)), beneficios, custos, custos_beneficios)

    elementos_ordenados = sorted(elementos, key = lambda x: x[3], reverse=True)

    espaco_disponivel = tamanho_mochila
    i = 0
    items = []
    valor_total = 0

    while(espaco_disponivel >= 0 and i < len(elementos_ordenados)):
        if(elementos_ordenados[i][2] <= espaco_disponivel):
            items.append([elementos_ordenados[i][0], elementos_ordenados[i][1], elementos_ordenados[i][2]])
            valor_total += elementos_ordenados[i][1]
            espaco_disponivel -= elementos_ordenados[i][2]
        i += 1
        
    return valor_total, items

#def mochila_dinamica(tamanho_mochila, beneficios, custos):

    #return valor_total, items

#tamanhos_conjuntos = [10, 50, 100, 200, 300, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000]
tamanhos_conjuntos = [10]

for tamanho_conjunto in tamanhos_conjuntos:
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
    
    t0 = time.time()
    valor_total, items = mochila_gulosa(tamanho_mochila, beneficios, custos)
    t1 = time.time()
    print(f"Gulosa: {t1-t0} segundos\nBenefício: {valor_total}")
    print(f"Items: {items}")

    #print("-"*10)

    #t0 = time.time()
    #valor_total, items = mochila_dinamica(tamanho_mochila, beneficios, custos)
    #t1 = time.time()
    #print(f"Dinâmica: {t1-t0} segundos\nBenefício: {valor_total}")


