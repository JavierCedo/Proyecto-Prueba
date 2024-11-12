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
    "Alprazolam": ["Alprazolam"],
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

## DataFrame para la app (Salida)
df_app = []

## Convierte la base de tados de ejemplo en un archivo CSV
farmacias = [far1, far2, far3]
df0 = pd.DataFrame(farmacias, index= Nom_far)
df0.to_csv('far_fic.csv', index=False)

## Leer el archivo CSV con la base de datos
df = pd.read_csv('far_fic.csv')
df.index = Nom_far

# Datos de la app (Entrada)
Med = "Enalapril"

# Resultado de busqueda
res_bus = {}


# Busqueda del medicamento en la farmacia

if Med in df:
    # Serie del medicamento "Med"
    Med_df = df[Med]
    Med_df.index = Nom_far

    # Indice y valor de la serie por farmacia
    for idx, val in Med_df.items():
        if pd.isnull(val):
            # Si es un valor nulo
            res_bus[idx] = val
        else:
            # Si el medicamnto se encuestra
            res_bus[idx] = val
else:
    # Si el medifamento no esta en ninguna farmacia
    print(f"El medicamento {Med} no está disponible en ninguna farmacia")


## Serie del resultado de la primera busqueda

ser_res_bus = pd.Series(res_bus)
print(ser_res_bus)
print("-"*30)









##   ## Busqueda de los componentes del medicamento en otras farmacias
##   
##   print(res_bus)
##   
##   for i,j in res_bus.items():
##       if j == "nan":
##           pass
##       else:
##           comp = j
##           print("Componente a buscar ",comp)
##           indices = df.index[df[Med] == j].tolist()
##           print("Indice donde esta el componente ", indices)
##           pass