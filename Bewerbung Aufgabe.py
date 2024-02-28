import pandas as pd
import matplotlib.pyplot as plt
#matplotlib was imported for the plotting task at the end



#1
fn="2024-02-22 Data Bewerbungsaufgabe.csv"
df=pd.read_csv(fn,delimiter=';',index_col=None)
df
# the delimiter ';' was defined because the default setup is ','
#didnt specify an index column because no column could be used as an index

df=df.rename(columns={'generator:source':'Energiequelle'})
df=df.rename(columns={'generator:output':'Leistung in KW'})
del df['wkt_geom']
df.head()


#2
df_sorted = df.sort_values(by='Energiequelle')

df_sorted.head()

#3

df_sorted['Leistung in KW'] = df_sorted['Leistung in KW'].replace('yes', 600)
df_sorted.head()

#4

df_cleaned=df_sorted.dropna(subset=['Leistung in KW'])
df_cleaned



#5
#first a list of powerplant types is created through unique function
Quellen = df_cleaned['Energiequelle'].unique()
print(Quellen)

#a loop was created to create subseet dataframes for every powerplant type

for quelle in Quellen:
    globals()[f'df_{quelle}'] = df_cleaned[df_cleaned['Energiequelle'] == quelle].copy()
    
    

#6

#bar chart was used because I found it was the most suitable to visualise this relationship 

df_gas['Leistung in KW'] = pd.to_numeric(df_gas['Leistung in KW'], errors='coerce')


plt.bar(range(len(df_gas)),df_gas['Leistung in KW'])
plt.xlabel('Gasanlagen')
plt.ylabel('Leistung in KW ')
plt.title('Gasanlagen vs Leistung in KW')
plt.show()
plt.savefig('Gasanlagen.png') 