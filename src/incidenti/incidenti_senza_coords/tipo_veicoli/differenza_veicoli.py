

import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")
import label_utils

path = "dataset/incidenti/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")

autostrade_veicoli = data[data['localizzazione_incidente'] == 7]['tipo_veicolo_a']
autostrade_veicoli = label_utils.join_labels(autostrade_veicoli, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['tipo_veicolo_a']
strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['tipo_veicolo_a']
strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

# uniti = pd.DataFrame([
#    autostrade_veicoli, strade_urbane, strade_extraurbane
# ], index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']).transpose()

# uniti[uniti > 0.001].dropna().transpose().plot.barh(width=1)
# plt.xlabel("Percentuale del tipo di veicolo")
# plt.yticks()
# plt.legend(bbox_to_anchor=(1,1), loc="upper left")
# plt.tight_layout()
# plt.show()

autostrade_veicoli = autostrade_veicoli[autostrade_veicoli.index != 'Auto privata']
strade_urbane = strade_urbane[strade_urbane.index != 'Auto privata']
strade_extraurbane = strade_extraurbane[strade_extraurbane.index != 'Auto privata']

df = pd.DataFrame([
   autostrade_veicoli, strade_urbane, strade_extraurbane
], index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']).transpose().dropna().transpose()

import sys
sys.path.append('src')
import heatmap as H

fig, ax = plt.subplots()

im, cbar = H.heatmap(df, df.index, df.columns, ax=ax, cmap="YlGn", cbarlabel="Percentuale del tipo di veicolo (2018)", xticks_rotated=True)
texts = H.annotate_heatmap(im, valfmt="")

fig.tight_layout()
plt.show()