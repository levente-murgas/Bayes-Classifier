# Mesterséges intelligenciával a valóságért: álhír-detekció

A program a BME mesterséges intelligencia és gépi tanulás tárgyú tanulmányi versenyére készült.

## Feladat rövid leírása:

A  verseny  során  COVID-19-hez kapcsolódó rövid magyar nyelvű híreket, 
híradásokat kell binárisan igaz/hamis kategóriákba sorolni. 
A feladat megoldásához egy 2 oszlopú, 7697 sorú mátrixot biztosítunk.
A cél egy olyan mesterséges intelligencia és gépi tanuláson alapuló önálló,
internettől független (offline) futásra képes megoldás létrehozása,
amely  az adott hírben szereplő információkra,
illetve akár nyilvános tudásbázisokra és nyelvi modellekre támaszkodva
lehetővé teszi a besorolást.

## Bemeneti információk:

Az adatokat az adat.csv szöveges file tartalmazza, vessző elválasztott formában.
A file első sora az oszlopok megnevezéseit tartalmazza,
ezekután minden további sora egy hírt tartalmaz:
- **Első oszlopban** – A hír besorolása: 1 –igaz / 0 –hamis (fake).
- **Második oszlopban** – A hír szövege.

## Az elvárt predikció

Az elvárt kimeneti predikció az adott hír valóságosságát jellemző pontszám (skalár),
például valószínűség (a nagyobb érték jelzi a hír valóságosabb voltát).

## Az elvárt megoldás

A beadott megoldásnak egyszerűen futtathatónak kell lennie,
amely a bemenetként egy „test.csv” fájlt vár,
amely soronként csak az egyes híreket tartalmazza.
Kimenetként pedig egy „prediction.csv” fájlt kell létrehoznia,
amely két oszlopos formátumban soronként tartalmazza a test.csv híreit,
az első oszlopában a prediktált valószerűségi pontszám szerepel.
A futtatás ellenőrzéséhez biztosítunk egy proba.csv-t,
amely szintén csak híreket tartalmaz az egyes oszlopokban.

## Teljesítménymetrikák (a prediction.CSV alapján)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. AUPR  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. AUROC  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Bináris félreosztályozási hiba

## Megoldás

### Összefoglaló

A feladat megoldásához a naív Bayes osztályozót választottam,
ami az osztályra vonatkozó feltételes valószínűséget azt feltételezve becsüli meg,
hogy az attribútumok feltételesen függetlenek adott y osztálycímke mellett.
A korpuszban található szavak súlyozására pedig a TF-IDF módszert választottam. 
Ez a statisztikai mérőszám lehetővé teszi egy dokumentumban szereplő
kifejezés jelentőségének értékelését a gyűjteményhez vagy korpuszhoz képest.

Az elkészült prediktor az adott hírre ad egy valószínűséget,
ami azt mutatja a hír mekkora valószínűséggel álhír, azaz címkéje = 0.

### Követelmények

**Csomagok:**\
pandas, csv - csv fájl parzolására\
numpy - "seed" generálására

**Modulok:**\
word_tokenize - szavak tokenizálására
HungarianStemmer - egy magyar szótövesítő
LabelEncoder - a címkék numerikus értékké történő parzolására
TfidfVectorizer - TF-IDF algoritmus alkalmazására
model_selection - a korpusz tanítási és tesztelési halmazra való szétválasztására
naive_bayes - a használt osztályozó
