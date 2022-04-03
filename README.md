# M2.951 - Pràctica 1: Web scraping

### 0. Introducció.

Aquest repositori conté la solució de la
**Pràctica 1: Web scraping** de l'assignatura M2.951 -
Tipologia i cicle de vida de les dades del Màster
Universitari en Ciència de Dades de la Universitat
Oberta de Catalunya.

El codi que conté aquest repositori ha estat desenvolupat
pels alumnes **Alexandre Vidal de Palol** i **Adrián Alonso Gonzalo**
(alexvidi i idriskameni en GitHub respectivament).

El codi que conté el repositori té com a objectiu 
descarregar una sèrie de conjunts de dades (o *datasets*)
de la pàgina oficial de la *National Basketball Association*,
també coneguda com a *NBA*. Dos dels conjunts de dades contenen
dades sobre la classificació (o *standings*) dels equips
de les conferències est i oest en la temporada actual.
Els altres dos conjunts de dades contenen el llistat de jugadors
que cadascun d'aquests equips té, així com algunes estadístiques
dels mateixos durant la temporada actual.

### 1. Context.

Els alumnes involucrats en la creació d'aquest repositori han
recollit aquesta informació amb la intenció de mostrar com es 
podrien recollir una sèrie de conjunts de dades relacionats amb
la *NBA* per després poder crear un **model de dades del tipus
entitat-relació** que posteriorment pugui **ser explotat per analistes
de dades** als quals els interessi fer anàlisis sobre aquest camp.

Tot i que en aquest repositori només ens hem centrat en els *standings* 
i en la llista de jugadors per equip, la web de la *NBA* també conté altres
dades ìnteressants com: estadístiques més detallades de cada jugador
o resultats de partits de temporades passades. Seguint el mateix mètode
aplicat en l'extracció dels conjunts proporcionats en aquest repositori,
els interessats podrien seguir descarregant diferents conjunts de dades
per completar i finalitzar el model de dades (nosaltres hem fet dos exemples com
a demostració de que això és possible).

La creació d'un model de dades del tipus entitat-relació permetria
als analistes de dades d'empreses relacionades amb l'*NBA* prendre
decisions basades en dades. Aquest model podria ajudar a identificar
els millors jugadors per equips, els equips que poden tenir opcions a
guanyar la lliga, etc.

En resum, el repositori proporciona conjunts de dades que tenen la
intenció de ser útils en la possible creació d'un model de dades del
tipus entitat-relació per la posterior explotació de les mateixes per
l'extracció de coneixement (basat en dades) en l'àmbit de l'*NBA*.

### 2. Títols dels conjunts de dades. 

En el repositori s'extreuen 4 conjunts de dades:

- **web-scraping-nba/docs/standings/<ins>nba_standing_east_conference.csv</ins>**:
classificació dels equips de la conferència 'EAST' de l'*NBA*
en el moment de l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.

- **web-scraping-nba/docs/standings/<ins>nba_standing_west_conference.csv</ins>**:
classificació dels equips de la conferència 'WEST' de l'*NBA*
en el moment de l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.

- **web-scraping-nba/docs/players/<ins>nba_players_statics_0.csv</ins>**:
llistat i estadístiques de la temporada dels jugadors de cada equip de la conferència 'EAST' i 'WEST' de l'*NBA* en el moment de
l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.  

- **web-scraping-nba/docs/players/<ins>nba_players_statics_1.csv</ins>**:
llistat i informació biogràfica dels jugadors de cada equip de la conferència 'EAST' i 'WEST' de l'*NBA* en el moment de
l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.  

- **
### 3. Descripció del dataset. 

- ####nba_standing_conference_0

    El dataset mostra les dades de la classificació dels 15 equips de la Conferència Est de la primera lliga americana de bàsquet de l'NBA. La taula està ordenada des de l'equip que té la màxima puntuació fins al que té menys punts. Altres dades que mostra la taula són per exemple els partits guanyats a casa o a fora, entre d'altres.

- ####nba_players_statics_0
    
    El dataset mostra les dades de la classificació dels 15 equips de la Conferència Oest de la primera lliga americana de bàsquet de l'NBA. La taula està ordenada des de l'equip que té la màxima puntuació fins al que té menys punts. Altres dades que mostra la taula són per exemple els partits guanyats a casa o a fora, entre d'altres.

- ####nba_players_statics_1.

    El conjunt de dades llista cadascun dels jugadors de cada equip de l'NBA on en les diverses columnes s'observen estadístiques tècniques de la temporada actual.

- ####nba_standing_conference_1

    El conjunt de dades llista cadascun dels jugadors de cada equip de l'NBA on en les diverses columnes mostren dades biogràfiques com altura, pes, data de naixement, entre d'altres.

### 4. Representació gràfica.

![](C:\Users\alexv\PycharmProjects\web-scraping-nba\charts and statics\duesConferències.PNG)

![](C:\Users\alexv\PycharmProjects\web-scraping-nba\charts and statics\nba_dades_biogràfiques_jugadors.PNG)

<img src="C:\Users\alexv\PycharmProjects\web-scraping-nba\charts and statics\dades_equips-logos-conferència.PNG"/>

![](C:\Users\alexv\PycharmProjects\web-scraping-nba\charts and statics\dades_jugadors.PNG)
### 5. Contingut. 

### 6. Agraïments.

### 7. Inspiració. 

### 8. Llicència. 

### 9. Codi. 

### 10. Dataset (Zenodo). 

### 11. Vídeo.