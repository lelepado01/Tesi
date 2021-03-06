
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import istat_utils

# Liste necessarie per normalizzare dati in base al numero di giorni in un mese o in un trimestre
giorni_al_mese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
giorni_al_trimestre = [31 +28+ 31, 30+ 31+30, 31+ 31+ 30, 31+ 30+ 31]

incidenti_2010 = pd.read_csv("dataset/incidenti/istat/incidenti_2010.txt", sep="\t")
incidenti_2011 = pd.read_csv("dataset/incidenti/istat/incidenti_2011.txt", sep="\t")
incidenti_2012 = pd.read_csv("dataset/incidenti/istat/incidenti_2012.txt", sep="\t")
incidenti_2013 = pd.read_csv("dataset/incidenti/istat/incidenti_2013.txt", sep="\t")
incidenti_2014 = pd.read_csv("dataset/incidenti/istat/incidenti_2014.txt", sep="\t")
incidenti_2015 = pd.read_csv("dataset/incidenti/istat/incidenti_2015.txt", sep="\t", encoding='latin1')
incidenti_2016 = pd.read_csv("dataset/incidenti/istat/incidenti_2016.txt", sep="\t", encoding='latin1')
incidenti_2017 = pd.read_csv("dataset/incidenti/istat/incidenti_2017.txt", sep="\t", error_bad_lines=False, engine="python")
incidenti_2018 = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t", encoding='latin1')

# La funzione restituisce la provincia richiesta in ogni anno disponibile
def get_provincia(prov : int) -> pd.DataFrame: 
    aosta_2010 = istat_utils.get_trimestre(incidenti_2010[incidenti_2010['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2011 = istat_utils.get_trimestre(incidenti_2011[incidenti_2011['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2012 = istat_utils.get_trimestre(incidenti_2012[incidenti_2012['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2013 = istat_utils.get_trimestre(incidenti_2013[incidenti_2013['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2014 = incidenti_2014[incidenti_2014['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2015 = incidenti_2015[incidenti_2015['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2016 = incidenti_2016[incidenti_2016['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2017 = incidenti_2017[incidenti_2017['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2018 = incidenti_2018[incidenti_2018['provincia'] == prov]['trimestre'].value_counts().sort_index()

    return pd.DataFrame(
        [aosta_2010, aosta_2011, aosta_2012, aosta_2013, aosta_2014, aosta_2015, aosta_2016, aosta_2017, aosta_2018], 
        ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        ).transpose()

# Selezione di Provincia di Milano (15)
provs = get_provincia(15)

index = 0
for giorni in giorni_al_trimestre: 
    provs.iloc[index] /= giorni
    index += 1

plt.subplot(1,3,1)
plt.plot(provs.index, provs, markevery=0.1, linewidth=1.5)
plt.xticks([1,2,3,4])
plt.xlabel("Trimestre")
plt.ylabel("Incidenti al trimestre a Milano")
plt.tight_layout()

# Selezione di Rimini (99)
provs = get_provincia(99)

index = 0
for giorni in giorni_al_trimestre: 
    provs.iloc[index] /= giorni
    index += 1

plt.subplot(1,3,2)
plt.plot(provs.index, provs, markevery=0.1, linewidth=1.5)
plt.xticks([1,2,3,4])
plt.xlabel("Trimestre")
plt.ylabel("Incidenti al trimestre a Rimini")
plt.tight_layout()

# Selezione di Aosta (7)
provs = get_provincia(7)

index = 0
for giorni in giorni_al_trimestre: 
    provs.iloc[index] /= giorni
    index += 1

plt.subplot(1,3,3)
plt.plot(provs.index, provs, markevery=0.1, linewidth=1.5)
plt.legend(provs.columns, bbox_to_anchor=(1,1), loc="upper left")
plt.xticks([1,2,3,4])
plt.xlabel("Trimestre")
plt.ylabel("Incidenti al trimestre a Aosta")
plt.tight_layout()
plt.show()
