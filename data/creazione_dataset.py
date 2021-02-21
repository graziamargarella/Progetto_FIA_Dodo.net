import pandas as pd 
import numpy as np

#leggo il file scaricato dal database di dodo.net
df = pd.read_csv("libri.csv")
#tengo traccia a quale isbn si riferisce l'index
df.ISBN.to_csv(path_or_buf="./ISBN_index.txt")
#elimino le colonne che non ci interessano
df.drop(columns=["ISBN", "Titolo", "Copertina", "Descrizione", "Sconto", "Quantita_Stock", "Data_Inserimento"], inplace=True)

#creo il dizionario per gli autori
autori_list = df.Autore.unique().tolist()
num_list = []
for i in range(0, len(autori_list)):
    num_list.append(i)
autori_dict = dict(zip(autori_list, num_list))

#creo il dizionario per le categorie
categorie_list = df.Nome_Categoria.unique().tolist()
num_list = []
for i in range(0, len(categorie_list)):
    num_list.append(i)
categorie_dict = dict(zip(categorie_list, num_list))

#creo il dizionario per gli editori
editori_list = df.Editore.unique().tolist()
num_list = []
for i in range(0, len(editori_list)):
    num_list.append(i)
editori_dict = dict(zip(editori_list, num_list))

#replace
df.replace(to_replace=editori_dict, inplace=True)
df.replace(to_replace=autori_dict, inplace=True)
df.replace(to_replace=categorie_dict, inplace=True)

#dichiaro quali sono le nuove categorie
new_columns = "num_mi_piace", "num_acquisti", "storia_vera", "illustrato", "num_pagine", "saga"
for i in new_columns:
    df[i] = 0

#inserisco valori casuali
df.num_mi_piace = np.random.randint(0, 20, df.shape[0])
df.num_acquisti = np.random.randint(0, 50, df.shape[0])
df.storia_vera = np.random.randint(0, 2, df.shape[0])
df.illustrato = np.random.randint(0, 2, df.shape[0])
df.saga = np.random.randint(0, 2, df.shape[0])
df.num_pagine = np.random.randint(200, 1000, df.shape[0])

#creo 100 nuove righe casuali
new_df = pd.DataFrame(columns=df.columns,index=range(0,100))
new_df.Autore = np.random.randint(0, 62, new_df.shape[0])
new_df.Editore = np.random.randint(1, 27, new_df.shape[0])
new_df.Prezzo = np.random.randint(4, 50, new_df.shape[0])
new_df.Anno = np.random.randint(2008, 2021, new_df.shape[0])
new_df.Nome_Categoria = np.random.randint(0, 8, new_df.shape[0])
new_df.num_mi_piace = np.random.randint(0, 20, new_df.shape[0])
new_df.num_acquisti = np.random.randint(0, 50, new_df.shape[0])
new_df.storia_vera = np.random.randint(0, 2, new_df.shape[0])
new_df.illustrato = np.random.randint(0, 2, new_df.shape[0])
new_df.saga = np.random.randint(0, 2, new_df.shape[0])
new_df.num_pagine = np.random.randint(200, 1000, new_df.shape[0])
df = df.append(new_df, ignore_index=True)

#esporto il dataset
df.to_csv(path_or_buf="./dataset.txt")