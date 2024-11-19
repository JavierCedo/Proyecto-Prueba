import pandas as pd
import kaggle
import os
import random

## Configurar Kaggle
#os.environ['KAGGLE_CONFIG_DIR'] = 'C:/Users/salce/.kaggle'
#dataset = 'singhnavjot2062001/11000-medicine-details'
#kaggle.api.dataset_download_files(dataset, path='.', unzip=True)

data = pd.read_csv("Medicine_Details.csv", index_col=False)
new_df = data[["Medicine Name", "Composition"]]

df1 = new_df.sample(n=len(new_df)//2, replace=True).reset_index(drop=True)
df2 = new_df.sample(n=len(new_df)//2, replace=True).reset_index(drop=True)
df3 = new_df.sample(n=len(new_df)//2, replace=True).reset_index(drop=True)

df1['DataFrame'] = 'farmacia1'
df2['DataFrame'] = 'farmacia2'
df3['DataFrame'] = 'farmacia3'

df_combined = pd.concat([df1, df2, df3])

df = df_combined.pivot_table(index='DataFrame', columns='Medicine Name', values='Composition', aggfunc=lambda x: x.iloc[0])

print("DataFrame combinado y pivotado:")
print(df)





### Nombres de las farmacias
#
#Nom_far = ["Farmacia1","Farmacia2","Farmacia3"]
#
#
### Leer el archivo CSV con la base de datos
#
#df = pd.read_csv('Medicine_Details.csv')
#df.index = Nom_far
#
#
### Entrada de datos (falta arreglar para la interfaz)
#
##       Med = input("Medicamento a buscar:").capitalize()
#
###Me dicamentos que han dado problemas y con lo que se estudian diferentes casos
#
#Med = "Enalapril"
##Med = "asdasd"
##Med = "Alprazolam"
##Med = "Aspirina"
##Med = "Amoxicilina con ácido clavulánico"
##Med = "Paracetamol"


Med = "Anbid 500 Tablet"

print("Medicamento a buscar:", Med)


## Almacenar datos de los resultado de busqueda

Med_bus_1 = {}
Com_bus_1 = {}
Med_sim_bus_2 = {}
similar_med = {}


## Busqueda del medicamento en la farmacia y sus componentes

if Med in df:
    df_Med = df[Med]
    for idx, val in df_Med.items():
        if pd.isnull(val):
            Med_bus_1[idx] = val
            Med_sim_bus_2[idx] = val
        else:
            Med_bus_1[idx] = "Esta"
            val = val.replace("[","").replace("]","").replace("'","").split(', ')
            Com_bus_1[idx] = val
else:
    Med_bus_1 = "No se encontro medicamento"
    Com_bus_1 = "No se encontro medicamento"

ser_Med_bus_1 = pd.Series(Med_bus_1)
df_Com_bus_1 = pd.Series(Com_bus_1)


if not Med_sim_bus_2:
    if not similar_med:
        Med_sim_bus_2 = "No hace falta"
        similar_med = "No hace falta"

ser_Med_sim_bus_2 = pd.Series(Med_sim_bus_2)


## Búsqueda de un medicamento similar en farmacias donde no está el original

nan_indices= ser_Med_sim_bus_2[pd.isnull(ser_Med_sim_bus_2)].index 

for idx_far in nan_indices: 
    for idx, val in df_Com_bus_1.items(): 
        for comp in val:
            valores_indice = df.loc[idx_far].to_list()
            for i in valores_indice:
                if isinstance(i, str):
                    i = eval(i)
                    for sub_i in i:
                        if sub_i == comp:
                            valor = str(i)
                            indice = idx_far
                            columna_encontrada = df.columns[(df.loc[indice] == valor)].tolist()
                            similar_med[idx_far] = columna_encontrada

if not similar_med:
    idx_far = 0
    similar_med[idx_far] = "No se encontro similar en ninguna farmacia"

ser_similar_med = pd.Series(similar_med)


## Busqueda del medicamento en la farmacia y sus componentes

print("-"*40)
print("*En que farmacia esta el medicamento*")
print(ser_Med_bus_1.to_string())
print("-"*40)
print("*Componentes del medicamento*")
print(df_Com_bus_1.to_string())
print("-"*40)

## Busqueda de los componentes del medicamento en otras farmacias

print("*Farmacia donde no esta el medicamento*")
print(ser_Med_sim_bus_2.to_string())
print("-"*40)

## Búsqueda de un medicamento similar en farmacias donde no está el original

print("*Farmacia donde existe uno similar*")
print (ser_similar_med.to_string())


"""

*Ejemplo de salida*
run Codigo.py:

Medicamento a buscar: Enalapril
----------------------------------------
*En que farmacia esta el medicamento*
Farmacia1    Esta
Farmacia2     NaN
Farmacia3     NaN
----------------------------------------
*Componentes del medicamento*
Farmacia1    [Enalapril maleato]
----------------------------------------
*Farmacia donde no esta el medicamento*
Farmacia2   NaN
Farmacia3   NaN
----------------------------------------
*Farmacia donde existe uno similar*
Farmacia2    [Diazepam]
Farmacia3    [Diazepam]

"""
