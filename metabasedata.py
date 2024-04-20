import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datos
data = {
    'Pais': ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Ecuador'],
    'Compras_2019': [100, 150, 80, 120, 90],
    'Compras_2020': [120, 160, 90, 130, 100],
    'Compras_2021': [130, 170, 100, 140, 110]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir los datos en un formato adecuado para Seaborn
df_melted = pd.melt(df, id_vars=['Pais'], var_name='Año', value_name='Total_Compras')

# Filtrar solo los países de Sudamérica
paises_sudamerica = ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Ecuador']
df_sudamerica = df_melted[df_melted['Pais'].isin(paises_sudamerica)]

# Gráficos en filas
st.set_option('deprecation.showPyplotGlobalUse', False)

## Gráfico de barras
st.write("## Gráfico de Barras")
plt.figure(figsize=(10, 6))
barplot = sns.barplot(data=df_sudamerica, x='Pais', y='Total_Compras', hue='Año')
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 5), 
                   textcoords = 'offset points')
plt.title('Número de Compras por Año y País (Sudamérica)')
plt.xlabel('País')
plt.ylabel('Total de Compras')
plt.xticks(rotation=45)
plt.legend(title='Año', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()  
st.pyplot()

## Tabla utilizando Seaborn (heatmap)
st.write("## Tabla de Datos: Número de Compras por País y Año")
plt.figure(figsize=(8, 4))
sns.heatmap(df.set_index('Pais'), annot=True, cmap='Blues', fmt='g', cbar=False)
plt.title('Tabla de Datos: Número de Compras por País y Año')
plt.xlabel('Año')
plt.ylabel('País')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
st.pyplot()

## Otra tabla más compleja (promedio de compras por país) utilizando Seaborn
st.write("## Promedio de Compras por País")
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Pais', y=df.drop('Pais', axis=1).mean(axis=1), hue='Pais', dodge=False)
plt.title('Promedio de Compras por País')
plt.xlabel('País')
plt.ylabel('Promedio de Compras')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot()

## Gráfico de líneas: Evolución de las compras a lo largo de los años para cada país
st.write("## Evolución de las Compras por Año y País (Sudamérica)")
plt.figure(figsize=(10, 6))
for pais in paises_sudamerica:
    plt.plot(df.columns[1:], df[df['Pais'] == pais].iloc[0, 1:], label=pais)
plt.title('Evolución de las Compras por Año y País (Sudamérica)')
plt.xlabel('Año')
plt.ylabel('Total de Compras')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
st.pyplot()

## Gráfico de dispersión: Relación entre las compras de diferentes años
st.write("## Relación entre las Compras de Diferentes Años")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df.drop('Pais', axis=1).melt(), x='variable', y='value', hue='variable')
plt.title('Relación entre las Compras de Diferentes Años')
plt.xlabel('Año')
plt.ylabel('Total de Compras')
plt.xticks(rotation=45)
plt.legend(title='Año')
plt.tight_layout()
st.pyplot()

## Histograma: Distribución de las compras en un año específico (por ejemplo, 2021)
st.write("## Distribución de las Compras en 2021 (Sudamérica)")
plt.figure(figsize=(8, 6))
sns.histplot(data=df_sudamerica, x='Total_Compras', bins=10, kde=True)
plt.title('Distribución de las Compras en 2021 (Sudamérica)')
plt.xlabel('Total de Compras')
plt.ylabel('Frecuencia')
plt.tight_layout()
st.pyplot()

## Gráfico de violín: Comparación de la distribución de las compras entre diferentes años
st.write("## Comparación de la Distribución de Compras entre Años")
plt.figure(figsize=(10, 6))
sns.violinplot(data=df.drop('Pais', axis=1).melt(), x='variable', y='value')
plt.title('Comparación de la Distribución de Compras entre Años')
plt.xlabel('Año')
plt.ylabel('Total de Compras')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot()
