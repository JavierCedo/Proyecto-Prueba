import pandas as pd

# Base de datos
    
far1 = {
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
    "Amoxicilina con ácido clavulánico": ["Amoxicilina", "Ácido clavulánico", "Otro", "Otro"],
} 
    
far2 = {
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
    "Medicamento de ejemplo": ["Enalapril maleato"],
} 

far3 = {
    "Paracetamol": ["Paracetamol"],
    "Ibuprofeno": ["Ibuprofeno"],
    "Naproxeno sódico": ["Naproxeno"],
    "Amoxicilina con ácido clavulánico": ["Amoxicilina", "Ácido clavulánico"],
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
    "Sertralina": ["Sertralina"],
    "Venlafaxina": ["Venlafaxina"],
    "Olanzapina": ["Olanzapina"],
    "Carbamazepina": ["Carbamazepina"],
    "Gabapentina": ["Gabapentina", "Otro"],
    "Medicamento de ejemplo": ["Enalapril maleato"],
}

## Nombres de las farmacias
Nom_far = ["far1","far2","far3"]

## Convierte la base de tados de ejemplo en un archivo CSV
farmacias = [far1, far2, far3]
df0 = pd.DataFrame(farmacias, index= Nom_far)
df0.to_csv('far_fic.csv', index=False)

## Leer el archivo CSV con la base de datos
df = pd.read_csv('far_fic.csv')
df.index = Nom_far


## Entrada de datos

#Med = "Alprazolam"
Med = "Enalapril"
#Med = "Amoxicilina con ácido clavulánico"
print("Medicamento a buscar:", Med)

# Almacenar datos de los resultado de busqueda
Med_bus_1 = {}
Com_bus_1 = {}
Med_sim_bus_2 = {}

## Busqueda del medicamento en la farmacia

if Med in df:
    # Serie del medicamento "Med"
    df_Med = df[Med]

    # Indice y valor de la serie por farmacia
    for idx, val in df_Med.items():
        if pd.isnull(val):
            # Si es un valor nulo
            Med_bus_1[idx] = val
            Med_sim_bus_2[idx] = val
        else:
            # Si el medicamnto se encuestra
            Med_bus_1[idx] = "Esta"
            val = val.replace("[","").replace("]","").replace("'"," ").split(', ')
            Com_bus_1[idx] = val
else:
    # Si el medifamento no esta en ninguna farmacia
    print(f"El medicamento {Med} no está disponible en ninguna farmacia")


## Resultado de la busqueda del medicamento y sus componentes

ser_Med_bus_1 = pd.Series(Med_bus_1)
print("-"*40)
print("*En que farmacia esta el medicamento*")
print(ser_Med_bus_1.to_string())
print("-"*40)
print("*Componentes del medicamento*")
df_Com_bus_1 = pd.Series(Com_bus_1)
print(df_Com_bus_1.to_string())
print("-"*40)


## Busqueda de los componentes del medicamento en otras farmacias

# Serie que muestra en que farmacia no esta el medicamento
print("*Farmacia donde no esta el medicamento*")
ser_Med_sim_bus_2 = pd.Series(Med_sim_bus_2)
print(ser_Med_sim_bus_2.to_string())
print("-"*40)

nan_indices= ser_Med_sim_bus_2[pd.isnull(ser_Med_sim_bus_2)].index 

# Búsqueda de un medicamento similar en farmacias donde no está el original 
similar_meds = {}


for idx_far in nan_indices: 
    for idx, val in df_Com_bus_1.items(): 
        for comp in val: 
            valores_indice = df.loc[idx_far].to_list()
            for i in valores_indice:
                i = str(i).replace("[","").replace("]","").replace("'"," ").replace(" ", "")
                comp = comp.replace(" ", "")
                #print(i, comp)
                if i == comp:
                    #print(i,comp)
                    similar_meds[idx_far] = i
                    #print("Existe similar")
    #else:
    #    print("No existe similar")


print("*Farmacia donde existe uno similar*")
ser_similar_meds = pd.Series(similar_meds)
print (ser_similar_meds.to_string())


"""
*Ejemplo de salida*
run Codigo.py:

Medicamento a buscar: Enalapril
----------------------------------------
*En que farmacia esta el medicamento*
far1    Esta
far2     NaN
far3     NaN
----------------------------------------
*Componentes del medicamento*
far1    [ Enalapril maleato ]
----------------------------------------
*Farmacia donde no esta el medicamento*
far2   NaN
far3   NaN
----------------------------------------
*Farmacia donde existe uno similar*
far2    Enalaprilmaleato
far3    Enalaprilmaleato

"""