# Apagar warnings en importacion de datos
import warnings
warnings.simplefilter('ignore', FutureWarning)

# Importa la libreria pandas
from pandas import *

# Importa matplot
import matplotlib.pyplot as plt

# Lee los datos desde archivo excel
#data = read_excel('POP_TOT_2018_ALL.xls', sheet_name=0, skiprows=3)

# Descarga la información directamente desde el sitio web
#con el comando sheet_name, seleccionamos la hoja del excel que vamos a trabajar
#con el comando skiprows, indicamos cuando saltos vamos a hacer y desde ese punto mostrar la informacion
data = read_excel('API_SP.POP.TOTL_DS2_en_excel_v2_2163395.xls', sheet_name=0, skiprows=3)
data
print (data)
wait = input("PRESS ENTER TO CONTINUE.")

# Crea un dataframe vacio
#en este dataframe se van mostrar las columnas que vamos a ir agregando de la variable data
dfp = DataFrame()
dfp

# Al dataframe vacio se le agrega la columna Country Name
#dfp['nombre que va tener la coloumna'] = data['nombre de la columna donde se van a copiar los datos']
dfp['Country Name'] = data['Country Name']
dfp
print (dfp)
wait = input("PRESS ENTER TO CONTINUE.")

# Se agrega la columan del año 2018
#dfp['nombre que va tener la coloumna'] = data['nombre de la columna donde se van a copiar los datos']
dfp['Population'] = data['2018']
dfp
print (dfp)
wait = input("PRESS ENTER TO CONTINUE.")





# Lee los datos desde archivo excel
# data = read_excel('GDP_TOT_2018_ALL.xls', sheet_name=0, skiprows=3)

# Descarga la información directamente desde el sitio web
#con el comando sheet_name, seleccionamos la hoja del excel que vamos a trabajar
#con el comando skiprows, indicamos cuando saltos vamos a hacer y desde ese punto mostrar la informacion

#data = read_excel('http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=excel', sheet_name=0, skiprows=3)
data = read_excel('API_NY.GDP.MKTP.CD_DS2_en_excel_v2_2163433.xls', sheet_name=0, skiprows=3)
data
print(data)
wait = input("PRESS ENTER TO CONTINUE.")

# Crea un dataframe vacio
#en este dataframe se van mostrar las columnas que vamos a ir agregando de la variable data
dfg = DataFrame()
dfg

# Al dataframe vacio se le agrega la columna Country Name
#dfg['nombre que va tener la coloumna'] = data['nombre de la columna donde se van a copiar los datos']
dfg['Country Name'] = data['Country Name']
dfg

# Se agrega la columan del año 2018
#dfg['nombre que va tener la coloumna'] = data['nombre de la columna donde se van a copiar los datos']
dfg['GDP'] = data['2018']
dfg
print (dfg)
wait = input("PRESS ENTER TO CONTINUE.")


# Merge data
#on: columnas (nombres) a las que unirse. Debe encontrarse en los objetos DataFrame izquierdo y derecho.
dfm = merge(dfp,dfg,on='Country Name')
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")


# New column
#vamos agregar una nueva columna en base al calculo ip mediante una division
#al mismo tiempo le decimos con cuantos decimales vamos a trabajar, en este caso es con 2
ip = round(dfm['GDP']/dfm['Population'],2)
dfm['GDP per capita'] = ip
dfm
print(dfm)
wait = input("PRESS ENTER TO CONTINUE.")


# Update a column (Population in thousands)
#actualizamos la columna population con todos sus valores divididos entre 100 y restringido a 2 decimales
dfm['Population'] = round(dfm['Population'] / 100, 2)
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")

# Update a column (GDP in million)
#actualizamos la columna GDP con todos sus valores divididos entre 1000000 y restringido a 2 decimales
dfm['GDP'] = round(dfm['GDP'] / 1000000, 2)
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")

# Fillig NaN
#llenamos los valores vacios de dfm y le damos el valor de 0
dfm = dfm.fillna(value=0)
dfm
print (dfm)
wait = input("PRESS ENTER TO CONTINUE.")

############################################################################
#
# Alternativas para filtrar las filas
#
############################################################################

#=================================================
# Primer alternativa para eliminar filas
# Eliminación de las filas por número de su indice
#dff = dfm.drop([257,93,179,196,101,138,154,100,61,247,63,168,140,71,59,228,66,60,
#                137,132,234,126,229,151,238,202,62,5,102,239,215,213,34,189,105,
#                72,203,96,133,103,134,216,181])
#
# Top 20 de las economias del mundo
#dff.sort_values('GDP',ascending=False).head(10)

#==================================================
# Segunda alternativa de eliminación de filas
# Se redefine el index del data frame

dfm.set_index('Country Name',inplace=True)

# Delete rows
#mediante el .drop se van a eliminar todas las filas que tengan los siguientes nombres.
dff = dfm.drop(['World',
'High income',
'OECD members',
'Post-demographic dividend',
'IDA & IBRD total',
'Low & middle income',
'Middle income',
'IBRD only',
'East Asia & Pacific',
'Upper middle income',
'Europe & Central Asia',
'North America',
'Late-demographic dividend',
'European Union',
'East Asia & Pacific (excluding high income)',
'East Asia & Pacific (IDA & IBRD countries)',
'Euro area',
'Early-demographic dividend',
'Lower middle income',
'Latin America & Caribbean',
'Latin America & Caribbean (excluding high income)',
'Europe & Central Asia (IDA & IBRD countries)',
'Middle East & North Africa',
'South Asia',
'South Asia (IDA & IBRD)',
'Europe & Central Asia (excluding high income)',
'Arab World',
'IDA total',
'Latin America & the Caribbean (IDA & IBRD countries)',
'Sub-Saharan Africa (IDA & IBRD countries)',
'Sub-Saharan Africa',
'Sub-Saharan Africa (excluding high income)',
'Central Europe and the Baltics',
'Pre-demographic dividend',
'IDA only',
'Least developed countries: UN classification',
'IDA blend',
'Fragile and conflict affected situations',
'Heavily indebted poor countries (HIPC)',
'Low income',
'Small states',
'Other small states'])

# Top 10 de las economias del mundo
dff.sort_values('GDP',ascending=False).head(10)

# Graficar
ax = dff.sort_values('GDP',ascending=False).head(10).plot.bar()
plt.show()

# Resumen estadístico
print (dff.describe())
wait = input("PRESS ENTER TO CONTINUE.")