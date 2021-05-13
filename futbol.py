
from bs4 import BeautifulSoup
import requests
import pandas as pd
 
url= 'https://resultados.as.com/resultados/futbol/primera/clasificacion/' 
page= requests.get (url) 
soup= BeautifulSoup(page.content, 'html.parser') 


 #Equipos 

eq = soup.find_all('span', class_ ='nombre-equipo')
 
equipos= list()

count =0

for i in eq:
    if count < 20: 
        equipos.append(i.text)
    else:
        break

    count +=1

#print(equipos, len(equipos))


 #Puntos 

puntos = soup.find_all('td', class_ ='destacado')
 
p= list()

for i in puntos:
    if count < 20: 
        p.append(i.text)
    else:
        break

    count +=1

print(p)

# Ya tenemos los datos de los equipos y de los puntajeds.
# Ahora usamos Pandas para hacer un Dataframe (df) que es un cuadrado.

cuadricula= pd.DataFrame({'Nombres': equipos, 'Puntaje':p}, index=list(range(1,21)))

print(cuadricula)

#cuadricula.to_csv('Clasificacion.csv', index=false)