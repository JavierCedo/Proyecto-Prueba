# Aqui va el codigo de nuestro proyecto

"""
Estructura de codigo

x1) Interaccion con base de datos, como se van a leer los datos

x1.1) Generar farmacias ficticias

2) Generar una entrada para el usuario

x3) En base a la entrada buscar en la base de datos el medicamento para saber en que farmacia se encuentra

4) Con el medicamento buscar en la base de datos que otro es similar en la misma farmacia y en las otras farmacias

5) Devolver los resultados con; el medicamento requerido, similares y en que farmacia se encuestra cada medicamento

"""

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
    "Gabapentina": ["Gabapentina"],
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

# Datos de la app (Entrada)
Med ="Alprazolam" #"Amoxicilina con ácido clavulánico" # "Enalapril"
print("Medicamento a buscar:", Med)

# Almacenar datos de los resultado de busqueda
Med_bus_1 = {}
Com_bus_1 = {}

## Busqueda del medicamento en la farmacia

if Med in df:
    # Serie del medicamento "Med"
    Med_df = df[Med]

    # Indice y valor de la serie por farmacia
    for idx, val in Med_df.items():
        if pd.isnull(val):
            # Si es un valor nulo
            Med_bus_1[idx] = val
        else:
            # Si el medicamnto se encuestra
            Med_bus_1[idx] = "Esta"
            val = val.replace("[","").replace("]","").replace("'"," ").split(', ')
            Com_bus_1[idx] = val
else:
    # Si el medifamento no esta en ninguna farmacia
    print(f"El medicamento {Med} no está disponible en ninguna farmacia")


## Serie del resultado de la primera busqueda

ser_Med_bus_1 = pd.Series(Med_bus_1)
print("-"*40)
print("*En que farmacia esta el medicamento*")
print(ser_Med_bus_1.to_string())
print("-"*40)
print("*Componentes del medicamento*")
df_Com_bus_1 = pd.Series(Com_bus_1)
print(df_Com_bus_1.to_string())


## Busqueda de los componentes del medicamento en otras farmacias
# Falta Hacer la Busqueda del similar


"""

run Codigo.py:

Medicamento a buscar: Alprazolam
----------------------------------------
*En que farmacia esta el medicamento*
far1    Esta
far2    Esta
far3     NaN
----------------------------------------
*Componentes del medicamento*
far1            [ Alprazolam ]
far2    [ Alprazolam ,  Otro ]

"""