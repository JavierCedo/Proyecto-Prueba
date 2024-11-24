import pandas as pd
import kaggle
import os
import random
import matplotlib.pyplot as plt
from tabulate import tabulate
import webbrowser

''' ## Configurar Kaggle
os.environ['KAGGLE_USERNAME'] = 'javiercedo115'
os.environ['KAGGLE_KEY'] = '70489924770b5b49f1db3a893bf8839a'
dataset = 'singhnavjot2062001/11000-medicine-details'
kaggle.api.dataset_download_files(dataset, path='.', unzip=True)
dataset = 'ujjwalaggarwal402/medicine-dataset'
kaggle.api.dataset_download_files(dataset, path='.', unzip=True)
'''

os.environ['KAGGLE_USERNAME'] = 'javiercedo115'
os.environ['KAGGLE_KEY'] = '70489924770b5b49f1db3a893bf8839a'
dataset = 'shudhanshusingh/az-medicine-dataset-of-india'
kaggle.api.dataset_download_files(dataset, path='.', unzip=True)

''' ## Cosas a hacer
 Separar "Medicine Name" en tres columnas, Nombre, cantidad, presentacion, imagen del medicamento.
 Separar "Composicion" en dos columnas, nombre_comp, cantidad_comp.
 Hacer graficas Usos, Efectos secundarios, "Excellent Review %,Average Review %,Poor Review %", monufactura.
 Recomendacion por componetes y usos.
'''


###############         Base de datos          #################








''' #Componentes Medicine_Details.csv
data = pd.read_csv("Medicine_Details.csv", index_col=False)

# Función para separar los componentes y sub-separar en nombre y cantidad
def separar_componentes(row):
    componentes = row['Composition'].split(' + ')
    for i, componente in enumerate(componentes):
        if ' (' in componente and componente.endswith(')'):
            nombre, cantidad = componente.rsplit(' (', 1)
            cantidad = cantidad.rstrip(')')
        else:
            nombre = componente
            cantidad = ''
        row[f'nombre_{i+1}'] = nombre
        row[f'cantidad_{i+1}'] = cantidad
    return row

df = data.apply(separar_componentes, axis=1)

df = df.fillna('')

columnas_intercaladas = []
max_componentes = max(int(col.split('_')[1]) for col in df.columns if col.startswith('nombre_'))

for i in range(1, max_componentes + 1):
    columnas_intercaladas.append(f'nombre_{i}')
    columnas_intercaladas.append(f'cantidad_{i}')

componentes = df[columnas_intercaladas]

from tabulate import tabulate

# Mostrar los nombres de las columnas con tabulate
print(tabulate(componentes.head(5)))
'''






''' ## Graficas
# Definición de la función para graficar gráficos circulares simplificados
def plot_top_pie_chart(data, column, top_n=10):
    top_data = data[column].value_counts().nlargest(top_n)
    plt.figure(figsize=(8, 6))
    top_data.plot.pie(autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.axis('equal')  # Para que el gráfico sea un círculo
    plt.title(f'Top {top_n} en {column}')
    plt.show()

# Graficar Uses (gráfico circular simplificado)
if 'Uses' in data.columns:
    plot_top_pie_chart(data, 'Uses')
else:
    print("La columna 'Uses' no se encuentra en el DataFrame.")

# Graficar Side_effects (gráfico circular simplificado)
if 'Side_effects' in data.columns:
    plot_top_pie_chart(data, 'Side_effects')
else:
    print("La columna 'Side_effects' no se encuentra en el DataFrame.")

# Graficar Reseñas (gráfico circular simplificado)
review_columns = ['Excellent Review %', 'Average Review %', 'Poor Review %']
if all(col in data.columns for col in review_columns):
    plt.figure(figsize=(8, 6))
    mean_reviews = data[review_columns].mean()
    top_reviews = mean_reviews.nlargest(3)
    top_reviews.plot.pie(autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.axis('equal')
    plt.title('Reseñas Promedio')
    plt.show()
else:
    print("Una o más columnas de reseñas no se encuentran en el DataFrame.")

# Graficar Manufacturer (gráfico circular simplificado)
if 'Manufacturer' in data.columns:
    plot_top_pie_chart(data, 'Manufacturer')
else:
    print("La columna 'Manufacturer' no se encuentra en el DataFrame.")
'''

''' ## Imagen
# Función para buscar el URL de la imagen del medicamento principal
def buscar_imagen_medicamento(nombre_medicamento):
    medicamento = data[data['Nombre'].str.contains(nombre_medicamento, na=False, case=False)]
    if not medicamento.empty:
        return medicamento.iloc[0]['Image URL']  # Retorna el URL de la imagen del primer medicamento encontrado
    return None

# Ejemplo de uso de la función de búsqueda
medicamento_principal = 'Paracetamol'  # Cambia esto por el medicamento que desees buscar
url_imagen = buscar_imagen_medicamento(medicamento_principal)

# Abrir el URL de la imagen en el navegador
if url_imagen:
    print(f"Abrir URL de la imagen para '{medicamento_principal}': {url_imagen}")
else:
    print(f"No se encontró imagen para el medicamento '{medicamento_principal}'.")
'''






'''

### Farmacias Ficticias

df1 = df.sample(n=len(df)//3, replace=True)
df2 = df.sample(n=len(df)//3, replace=True)
df3 = df.sample(n=len(df)//3, replace=True)

df1 = df1.drop_duplicates(subset=['Nombre', 'Dosis', 'Presentacion', 'Composition'])
df2 = df2.drop_duplicates(subset=['Nombre', 'Dosis', 'Presentacion', 'Composition'])
df3 = df3.drop_duplicates(subset=['Nombre', 'Dosis', 'Presentacion', 'Composition'])

df1 = df1.set_index('Nombre')
df2 = df2.set_index('Nombre')
df3 = df3.set_index('Nombre')

#print(tabulate(df1.info()))

list_farms = {'Farmacia1':df1, 'Farmacia2':df2, 'Farmacia3':df3}


###############         Codigo          ################

# Entrada de datos (falta arreglar para la interfaz)

       Med = input("Medicamento a buscar:").capitalize()

##Me dicamentos que han dado problemas y con lo que se estudian diferentes casos

med = "Azithral"

## Almacenar datos de los resultado de busqueda

farm_esta_med = {}
farm_y_comp = {}
farm_no_med = {}
far_med_sml = {}

## Donde esta el medicamento, sus componentes y donde no esta el medicamento

for nom_farm, df_farm in list_farms.items():
    if med in df_farm.index:
        comp = df_farm.loc[med, "Composition"]
        if type(comp) == pd.core.series.Series:
            for idx, val in comp.items():
                farm_y_comp[nom_farm] = val
                farm_esta_med[nom_farm] = f"Esta {med}"
        else:
            farm_y_comp[nom_farm] = comp
            farm_esta_med[nom_farm] = f"Esta {med}"
            
    else:
        farm_no_med[nom_farm] = f"No esta {med}"
        
for nom_farm, df_farm in list_farms.items():
    for farm, comp in farm_y_comp.items():
        ###                         Hacer bucle para comp que va a ser una lista ya hacer lo mismo para hacer la comparacion y buscar en el df.
        valor = comp
        columna = 'Composition'
        indice = df_farm.index[df_farm[columna] == valor]
        indice = pd.Series(indice)
        #print(comp, "a buecar en", nom_farm )
        #print("lista similares", indice)
        lista = []
        for idx, val in indice.items():
            if str(med) != str(val):
                lista.append(val)
                far_med_sml[nom_farm] = lista

print("Medicamento a buscar:", med)
print("En que farmacia esta")
print(farm_esta_med)
print("componestes por farmacia")
print(farm_y_comp)
print("En que farmacia no esta")
print(farm_no_med)
print("Similares")
print(far_med_sml)
'''