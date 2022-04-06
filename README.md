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
descarregar una sèrie de 6 conjunts de dades (o *datasets*)
de la pàgina oficial de la *National Basketball Association*,
també coneguda com a *NBA*. Dos dels conjunts de dades contenen
dades sobre la classificació (o *standings*) dels equips
de les conferències est i oest en la temporada actual.
Altres dos conjunts de dades contenen el llistat de jugadors
que cadascun d'aquests equips té, així com algunes estadístiques
 biogràfiques d'aquests. 
I els dos datasets restants mostren una taula amb informació sobre estadístiques 
dels partits de cada jugador en cada conferència.

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
per completar i finalitzar el model de dades (nosaltres hem fet tres exemples com
a demostració que això és possible).

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

En el repositori s'extreuen 6 conjunts de dades:

#### 2.1. teams_standing_eastern_conference i teams_standing_western_conference
- **web-scraping-nba/docs/teams_standings/<ins>teams_standing_eastern_conference.csv</ins>**:
classificació dels equips de la conferència 'EAST' de l'*NBA*
en el moment de l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.

- **web-scraping-nba/docs/teams_standings/<ins>teams_standing_western_conference.csv</ins>**:
classificació dels equips de la conferència 'WEST' de l'*NBA*
en el moment de l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.

#### 2.2. players_stats_eastern_conference i players_stats_western_conference
- **web-scraping-nba/docs/players_stats/<ins>players_stats_eastern_conference.csv</ins>**:
llistat i estadístiques de la temporada dels jugadors de cada equip de la conferència 'EAST' de l'*NBA* en el moment de
l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.  

- **web-scraping-nba/docs/players_stats/<ins>players_stats_western_conference.csv</ins>**:
llistat i estadístiques de la temporada dels jugadors de cada equip de la conferència 'WEST' de l'*NBA* en el moment de
l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.  

#### 2.3. players_list_eastern_conference i players_list_western_conference
- **web-scraping-nba/docs/players_list/<ins>players_list_eastern_conference.csv</ins>**:
llistat i informació biogràfica dels jugadors de cada equip de la conferència 'EAST' i de l'*NBA* en el moment de
l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.  

- **web-scraping-nba/docs/players_list/<ins>players_list_western_conference..csv</ins>**:
llistat i informació biogràfica dels jugadors de cada equip de la conferència 'WEST' de l'*NBA* en el moment de
l'execució del fitxer 'web-scraping-nba/src/web-scraping-nba/web_scraping_nba.py'.


### 3. Descripció del dataset. 

#### 3.1. teams_standing_eastern_conference i teams_standing_western_conference
- El dataset mostra les dades de la classificació dels 15 equips de la conferència 'EAST' i 'WEST' (respectivament) de la
primera lliga americana de bàsquet de l'NBA. La taula està ordenada des de l'equip que té la màxima puntuació fins al
que té menys punts. Altres dades que mostra la taula són per exemple els partits guanyats a casa o a fora, entre
d'altres.
    
#### 3.2. players_stats_eastern_conference i players_stats_western_conference
- El conjunt de dades llista cadascun dels jugadors de cada equip de la conferència 'EAST' i 'WEST' (respectivament) de
l'NBA on en les diverses columnes s'observen estadístiques tècniques de la temporada actual.

#### 3.3. players_list_eastern_conference i players_list_western_conference
- El conjunt de dades llista cadascun dels jugadors de cada equip de l'NBA de la conferència 'EAST' i 'WEST' (respectivament) 
on en les diverses columnes mostren dades biogràfiques com altura, pes, data de naixement, entre d'altres.

### 4. Representació gràfica.

#### 4.1. teams_standing_eastern_conference i teams_standing_western_conference
Exemple visual dels datasets **teams_standing_eastern_conference.csv** i **teams_standing_eastern_conference.csv** on mostra el mapa dels EEUU dividit entre les dues conferències de la lliga NBA amb la ubicació de cada equip
![Representació gràfica sobre diverses dades biogràfiques dels jugador](https://github.com/idriskameni/web-scraping-nba/blob/main/images/visual_map_conference.jpg)

#### 4.2. players_stats_eastern_conference i players_stats_western_conference
- Exemple gràfic dels datasets **players_stats_eastern_conference** i **players_stats_western_conference** que representa una comparativa sobre diverses variables estadístiques de diferents jugadors.
![Representació gràfica sobre diverses dades biogràfiques dels jugador](https://github.com/idriskameni/web-scraping-nba/blob/main/images/Representació_Gràfica_Statics_Players.png)

#### 4.3. players_list_eastern_conference i players_list_western_conference
- Exemple gràfic dels datasets **players_list_eastern_conference** i **players_list_western_conference** on es mostra informació visual sobre dades biogràfiques dels jugadors.
![Representació gràfica sobre diverses dades biogràfiques dels jugador](https://github.com/idriskameni/web-scraping-nba/blob/main/images/nba_dades_biogràfiques_jugadors.PNG)


### 5. Contingut.

#### 5.1. teams_standing_eastern_conference i teams_standing_western_conference

Camps i descripció:

  - Clasif - Numero en el ranking de la lliga
  - Nombre - Nom de l'equip
  - Nombre.1 - Abreviació nom de l'equip
  - V - victories
  - D - derrotes
  - % - tant per cent de victories sobre les derrotes
  - DIF - diferència respecte a l'anterior
  - CONF - valors respecte equips conferència
  - DIV - valors estadístics
  - Local - partits guanyats a casa
  - Visitante - partits guanyats a fora
  - 10 últimos - punts dels deu últims partits
  - Racha - partits guanyats consecutius
  - FP - valors estadístics
  - PA - valors estadístics
  - DIF.2 - diferència entre FP i PA
  - Conference - a quina conferència pertany l'equip

#### 5.2. players_stats_eastern_conference i players_stats_western_conference

Camps i descripció:
  
  - B - punts totals anotats
  - GS - jocs començats
  - PPP - mitjana de punts per partit
  - REPP - ratio de punts 
  - APP - ratio de passades per partit
  - MPP - ratio assistències de punts per partit
  - EFI - valor respecte a l'eficiència 
  - %TC - tant per cent tirs a canasta
  - %3P - tant per cent de triples
  - %TL - tant per cent de tirs lliure
  - OFE - valor estadístic respecte ofensiva
  - DEF - valor estadístic respecte a defensa
  - ROPP - mitjana sobre valor estadístic entre ofensiva i defensiva
  - TPP - mitjana estadística en quan a bloquejos
  - PÉR - valors respecte torns de sortida al camp
  - FP - mitjana de faltes per partit
  - Team - Equip al qual juga 
  - Conference - Conferència que juga

#### 5.3. players_list_eastern_conference i players_list_western_conference

Camps i descripció:

  - Nombre - Nom del jugador
  - Pos. - Posició que juga al camp
  - Altura - Alçada del jugador
  - Peso - Pes del jugador
  - Numero - número de camiseta
  - Fecha de nacimiento - Data de naixament
  - Exp - Anys a l'NBA
  - Antes de la NBA - Equip al qual jugava anterior a l'NBA
  - País - Nacionalitat del jugador
  - Team - Equip actual del jugador
  - Conference - Conferència a la qual juga


### 6. Agraïments.

### 7. Inspiració. 

El bàsquet és un esport més complicat d'analitzar que el baseball, pel simple fet d'estar en moviment constant i tenir més 
factors que afecten els números. Al bàsquet, la principal evolució sorgeix en què els fins ara elements bàsics d'anàlisi (percentatge de tir, anotació, 
rebot… per citar-ne alguns) segueixen tenint significat, és clar, però ja està del tot estesa allà la idea que no capten el dibuix complet del que ha passat. 
Cal anar més enllà.

Als Estats Units, són els amants més grans de les estadístiques en l'esport i això es reflecteix en tots els seus grans esports. 
El bàsquet no és una excepció, ia l'NBA, les estadístiques es tracten a tots els nivells. I és que analitzant les estadístiques, pots arribar a treure'n moltes conclusions sobre com s'ha desenvolupat un 
determinat partit, i quins jugadors han estat més encertats i en quins aspectes del joc.
Tanmateix, els cossos tècnics dels equips de l'NBA i de la Lliga Endesa tenen especialistes en estadístiques i en obtenir 
informació valuosa dels números.
Un altre punt molt rellevant és respecte el negoci de les apostes, les quals també tenen en l'estadística la millor font 
d'informació per realitzar els seus pronòstics a la lliga nord-americana de bàsquet NBA i poder aspirar a anticipar algun resultat llegint de manera adequada dades numèriques.

### 8. Llicència. 

### 9. Codi. 

### 10. Dataset (Zenodo). 

### 11. Vídeo.