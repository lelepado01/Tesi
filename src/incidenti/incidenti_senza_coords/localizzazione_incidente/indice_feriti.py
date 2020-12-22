
# File usato per calcolare tabella con indici di 
# feriti per tipo di strada

import pandas as pd

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t", encoding='latin1')

incr = 'intersezione_o_non_interse3'

df = {}
for inc in data[incr].unique(): 
    df[inc] = 0

for inc, morti in zip(data[incr], data['feriti']): 
    df[inc] += morti

indice_mort = pd.Series(df.values(),index =  df.keys()).sort_index()

num_incr = data[incr].value_counts().sort_index()

mortalita = pd.DataFrame([indice_mort * 100 / num_incr], 
    index=['indice']
).transpose()

mortalita['incrocio'] = mortalita.index

import sys
sys.path.append("src")
import label_utils

mortalita['incrocio'] = label_utils.join_labels(
    mortalita['incrocio'], 
    "dataset/incidenti/istat/Classificazioni/intersezione_o_non_interse3.csv"
    )

print(mortalita)
