from matplotlib import lines
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
pd.set_option("display.precision", 8)

sizes = [10, 50, 100, 200, 300, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000]
set_names = ["Dinâmica", "Gulosa"]

# tempo gulosa pelo tam
# tempo dinamica pelo tam
# Media Tempo Dinamica/Milhao celulas por tam

csv_file = pd.read_csv("Resultados.csv") 
resultados_gulosa = csv_file["Media Tempo Gulosa"]
#print(resultados_gulosa)

resultados_dinamica = csv_file["Media Tempo Dinamica"]
tempo_dinamica_celula = csv_file["Media Tempo Dinamica/Milhao celulas"]
#print(resultados_dinamica)

df = pd.DataFrame({
    'tam': sizes,
    're_gulosa': resultados_gulosa,
    're_dinamica': resultados_dinamica,
    'tempo_celula': tempo_dinamica_celula
    })

plt.figure()
plt.title("Gulosa")
plt.xlabel("Tamanho")
plt.ylabel("Tempo (s)")
plt.plot(df['tam'], df['re_gulosa'], color='g', label='Gulosa')
plt.legend()
plt.show()

plt.figure()
plt.title("Dinâmica")
plt.xlabel("Tamanho")
plt.ylabel("Tempo (s)")
plt.plot(df['tam'], df['re_dinamica'], color='r', label='Dinâmica')
plt.legend()
plt.show()

plt.figure()
plt.title("Média Tempo Dinâmica/Milhao celulas")
plt.xlabel("Tamanho")
plt.ylabel("Tempo (s)")
plt.ylim(0, 1)
plt.plot(df['tam'], df['tempo_celula'], color='r', label='Media Tempo Dinamica/Milhao celulas')
plt.legend()
plt.show()

