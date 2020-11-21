
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/incidenti_2018.txt", sep="\t", encoding='latin1')

incroci = 'intersezione_o_non_interse3'
morti = ['morti_entro_24_ore', 'morti_entro_30_giorni']

data['morti'] = data[morti[0]] + data[morti[1]]

df = {}
for inc in data[incroci].unique(): 
    df[inc] = 0

for inc, morti in zip(data[incroci], data['morti']): 
    df[inc] += morti

indice_mortalita = pd.Series(df.values(),index =  df.keys()).sort_index()

num_incroci = data[incroci].value_counts().sort_index()

mortalita = pd.DataFrame([indice_mortalita * 100 / num_incroci], 
    index=['indice']
).transpose()

mortalita['incrocio'] = mortalita.index

import sys
sys.path.append("src")
import label_utils

mortalita['incrocio'] = label_utils.join_labels(mortalita['incrocio'], "dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv")

mortalita.index = mortalita['incrocio']
mortalita = mortalita['indice']

mortalita = mortalita.sort_index()

mortalita.plot.barh(color = '#aa6677', width=0.9)
plt.xlabel("Indice di Mortalità per tipo di incrocio (2018)")
plt.ylabel("")
plt.tight_layout()
plt.show()