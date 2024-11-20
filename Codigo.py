import pandas as pd
import kaggle
import os
import random
import matplotlib.pyplot as plt
from tabulate import tabulate
import webbrowser


''' ## Ejemplo base de datos

Nombre                Dosis    Presentacion     Nombres_componentes                      cantidades_componentes

Avastin               400mg    Injection        [Bevacizumab]                            [400mg]
Augmentin             625      Duo Tablet       [Amoxycillin, Clavulanic Acid]           [500mg, 125mg]
Azithral              500      Tablet           [Azithromycin]                           [500mg]
Ascoril               LS       Syrup            [Ambroxol, Levosalbutamol, Guaifenesin]  [30mg/5ml, 1mg/5ml, 50mg/5ml]
Aciloc                150      Tablet           [Ranitidine]]                            [150mg]
Allegra               120mg    Tablet           [Fexofenadine]                           [120mg]
Avil                  25       Tablet           [Pheniramine]                            [25mg]
Aricep                5        Tablet           [Donepezil]                              [5mg]

'''


''' ## Configurar Kaggle
os.environ['KAGGLE_CONFIG_DIR'] = 'C:/Users/salce/.kaggle'
dataset = 'singhnavjot2062001/11000-medicine-details'
kaggle.api.dataset_download_files(dataset, path='.', unzip=True)
'''

''' ## Cosas a hacer
 Separar "Medicine Name" en tres columnas, Nombre, cantidad, presentacion, imagen del medicamento.
 Separar "Composicion" en dos columnas, nombre_comp, cantidad_comp.
 Hacer graficas Usos, Efectos secundarios, "Excellent Review %,Average Review %,Poor Review %", monufactura.
 Recomendacion por componetes y usos.
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

###############         Base de datos          ################

# Cargar los datos
data = pd.read_csv("Medicine_Details.csv", index_col=False)

# Limpiar espacios en blanco en los nombres de las columnas
data.columns = data.columns.str.strip()

# arreglar
# Función para separar nombre, dosis y presentación
def separar_nombre_dosis_presentacion(medicamento):
    partes = medicamento.split()
    if len(partes) < 2:
        return pd.Series([medicamento, None, None])  # Devuelve el nombre y None para dosis y presentación
    
    # La última parte es la presentación, la penúltima es la dosis
    presentacion = partes[-1]
    dosis = partes[-2]
    
    # El resto es el nombre
    nombre = ' '.join(partes[:-2])
    
    # Si la presentación tiene más de una palabra (ejemplo: "Nasal Spray")
    if len(partes) > 3:
        presentacion = ' '.join(partes[-2:])
        dosis = partes[-3]
    
    return pd.Series([nombre, dosis, presentacion])

# Aplicar la función de separación
data[['Nombre', 'Dosis', 'Presentacion']] = data['Medicine Name'].apply(separar_nombre_dosis_presentacion)


# Arreglar
# Separar "Composition" en dos columnas: nombre_comp, cantidad_comp
data[['nombre_comp', 'cantidad_comp']] = data['Composition'].str.split('+', n=1, expand=True)

# Eliminar filas donde 'Nombre' esté vacío
data = data[data['Nombre'].notnull() & (data['Nombre'] != '')]


# Verlo
#       # Eliminar duplicados
#       data = data.drop_duplicates(subset=['Nombre', 'Uses'])


df = data[['Nombre', 'Dosis', 'Presentacion', 'Composition']].set_index('Nombre')

#print(tabulate(df.head(20)))

### Farmacias Ficticias

df1 = df.sample(n=len(df)//3, replace=True)
df2 = df.sample(n=len(df)//3, replace=True)
df3 = df.sample(n=len(df)//3, replace=True)

#print(df1.head(10))

list_farms = {'Farmacia1':df1, 'Farmacia2':df2, 'Farmacia3':df3}



###############         Codigo          ################

'''
# Entrada de datos (falta arreglar para la interfaz)

       Med = input("Medicamento a buscar:").capitalize()
'''

##Me dicamentos que han dado problemas y con lo que se estudian diferentes casos

med = "Nexpro"

#print("Medicamento a buscar:", med)

## Almacenar datos de los resultado de busqueda
farm_esta_med = {}
farm_y_comp = {}
farm_no_med = {}


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

print(farm_esta_med)
print(farm_y_comp)
print(farm_no_med)

far_med_sml = {}

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
                lista.append(val)
                far_med_sml[nom_farm] = lista

print(far_med_sml)





###############         Codigo antiguo          ################

'''
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

'''