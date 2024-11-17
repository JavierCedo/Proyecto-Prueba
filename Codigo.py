import pandas as pd

# Base de datos
    
Farmacia1 = {
    "Paracetamol": ["Paracetamol"],
    "Ibuprofeno": ["Ibuprofeno"],
    "Aspirina": ["Ácido acetilsalicílico"],
    "Amoxicilina": ["Amoxicilina"],
    "Diclofenaco": ["Diclofenaco sódico"],
    "Loratadina": ["Loratadina"],
    "Omeprazol": ["Omeprazol"],
    "Metformina": ["Metformina"],
    "Simvastatina": ["Simvastatina"],
    "Atorvastatina": ["Atorvastatina"],
    "Enalapril": ["Enalapril maleato"],
    "Losartán": ["Losartán potásico"],
    "Amlodipino": ["Amlodipino besilato"],
    "Furosemida": ["Furosemida"],
    "Levotiroxina": ["Levotiroxina sódica"],
    "Alprazolam": ["Alprazolam"],
    "Sertralina": ["Sertralina"],
    "Venlafaxina": ["Venlafaxina"],
    "Diazepam": ["Diazepam"],
    "Clonazepam": ["Clonazepam"],
    "Acetaminofen": ["Acetaminofen"],
    "Amoxicilina con ácido clavulánico": ["Amoxicilina", "Ácido clavulánico", "Javi er"],
} 
    
Farmacia2 = {
    "Paracetamol": ["Paracetamol"],
    "Ibuprofeno": ["Ibuprofeno"],
    "Naproxeno": ["Naproxeno"],
    "Amoxicilina con ácido clavulánico": ["Amoxicilina", "Ácido clavulánico"],
    "Diclofenaco sódico": ["Diclofenaco sódico"],
    "Cetirizina": ["Cetirizina"],
    "Famotidina": ["Famotidina"],
    "Metformina clorhidrato": ["Metformina"],
    "Rosuvastatina": ["Rosuvastatina"],
    "Atorvastatina cálcica": ["Atorvastatina"],
    "Lisinopril": ["Lisinopril"],
    "Valsartán": ["Valsartán"],
    "Amlodipino besilato": ["Amlodipino"],
    "Hidroclorotiazida": ["Hidroclorotiazida"],
    "Levotiroxina sódica": ["Levotiroxina"],
    "Alprazolam": ["Alprazolam", "Otro"],
    "Citalopram": ["Citalopram"],
    "Venlafaxina": ["Venlafaxina"],
    "Diazepam": ["Diazepam"],
    "Gabapentina": ["Gabapentina"],
    "Diazepam": ["Enalapril maleato"],
} 

Farmacia3 = {
    "Paracetamol": ["Paracetamol"],
    "Ibuprofeno": ["Ibuprofeno"],
    "Naproxeno sódico": ["Naproxeno"],
    "Diclofenaco potásico": ["Diclofenaco"],
    "Cetirizina": ["Cetirizina"],
    "Famotidina": ["Famotidina"],
    "Metformina clorhidrato": ["Metformina"],
    "Rosuvastatina cálcica": ["Rosuvastatina"],
    "Atorvastatina cálcica": ["Atorvastatina"],
    "Lisinopril": ["Lisinopril"],
    "Valsartán": ["Valsartán"],
    "Amlodipino besilato": ["Amlodipino"],
    "Hidroclorotiazida": ["Hidroclorotiazida"],
    "Levotiroxina sódica": ["Levotiroxina"],
    "Sertralina": ["Sertralina", "Otro"],
    "Venlafaxina": ["Venlafaxina"],
    "Olanzapina": ["Olanzapina"],
    "Carbamazepina": ["Ácido clavulánico"],
    "Gabapentina": ["Gabapentina", "Javi er"],
    "Diazepam": ["Enalapril maleato"],
}


## Nombres de las farmacias

Nom_far = ["Farmacia1","Farmacia2","Farmacia3"]


## Convierte la base de tados de ejemplo en un archivo CSV

farmacias = [Farmacia1, Farmacia2, Farmacia3]
df0 = pd.DataFrame(farmacias, index= Nom_far)
df0.to_csv('far_fic.csv', index=False)


## Leer el archivo CSV con la base de datos

df = pd.read_csv('far_fic.csv')
df.index = Nom_far


## Entrada de datos

#       Med = input("Medicamento a buscar:").capitalize()

#Me dicamentos que han dado problemas y con lo que se estudian diferentes casos

Med = "Enalapril"
#Med = "asdasd"
#Med = "Alprazolam"
#Med = "Aspirina"
#Med = "Amoxicilina con ácido clavulánico"
#Med = "Paracetamol"

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


if bool(Med_sim_bus_2):
    pass
else:
    if bool(similar_med):
        pass
    else:
        Med_sim_bus_2 = "No hace falta"
        similar_med = "No hace falta"

ser_Med_sim_bus_2 = pd.Series(Med_sim_bus_2)


## Búsqueda de un medicamento similar en farmacias donde no está el original

nan_indices= ser_Med_sim_bus_2[pd.isnull(ser_Med_sim_bus_2)].index 

for idx_far in nan_indices: 
    for idx, val in df_Com_bus_1.items(): 
        for comp in val:
            comp = comp.replace("'", "").strip().split(",")
            for sub_comp in comp:
                valores_indice = df.loc[idx_far].to_list()
                for i in valores_indice:
                    if isinstance(i, str):
                        sub_comp = sub_comp.replace("'", "")
                        i = eval(i)
                        for sub_i in i:
                            if sub_i == sub_comp:
                                valor = str(i)
                                indice = idx_far
                                columna_encontrada = df.columns[(df.loc[indice] == valor)].tolist()
                                similar_med[idx_far] = columna_encontrada

if bool(similar_med):
    pass
else:
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
