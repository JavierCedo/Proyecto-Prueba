# Aqui va el codigo de nuestro proyecto

"""
Estructura de codigo

1) Interaccion con base de datos, como se van a leer los datos

1.1) Generar farmacias ficticias

2) Generar una entrada para el usuario

3) En base a la entrada buscar en la base de datos el medicamento

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
    "Clonazepam": ["Clonazepam"]
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
    "Gabapentina": ["Gabapentina"]
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
    "Gabapentina": ["Gabapentina"]
}

farmacias = [far1, far2, far3]
df0 = pd.DataFrame(farmacias, index= ["far1","far2","far3"])
df0.to_csv('far_fic.csv', index=False)


df = pd.read_csv('far_fic.csv')
print("DataFrame")
print(df)


# Entrada de datos
Med = "Enalapril"



# Algoritmo de busqueda

if Med in df:
    Med_df = df[Med]
    print(Med_df)
    for idx, val in Med_df.items():
        if pd.isnull(val):
            print(f"En la {idx} no se encuentra el medicamento {Med}")
        else:
            print(f"En la {idx} se encuentra el medicamento {Med} con la componentes {val[0]}")
else:
    print(f"El medicamento {Med} no está disponible en ninguna farmacia")
