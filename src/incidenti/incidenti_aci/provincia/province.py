
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2018.csv")
fields = ['INC','FER']

df = pd.DataFrame()
for f in data['PROVINCIA'].unique():
    df = df.append(pd.DataFrame([f, data[data['PROVINCIA'] == f]['INC'].sum(), data[data['PROVINCIA'] == f]['FER'].sum()]).transpose(), ignore_index=True)

df.set_index(df[0], inplace=True)
df =  df[[1,2]]

df[1].plot(label='Feriti')
df[2].plot(label='Incidenti')
plt.xticks(rotation=90)
plt.legend()
plt.ylabel("Incidenti all'anno (2018)")
plt.xlabel("Province in Italia")
plt.tight_layout()
plt.show()
