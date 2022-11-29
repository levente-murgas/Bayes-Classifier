Követelmények:

csomagok:
pandas, csv - csv fájl parzolására
numpy - "seed" generálására

modulok:
word_tokenize - szavak tokenizálására
HungarianStemmer - egy magyar szótövesítő
LabelEncoder - a címkék numerikus értékké történő parzolására
TfidfVectorizer - TF-IDF algoritmus alkalmazására
model_selection - a korpusz tanítási és tesztelési halmazra való szétválasztására
naive_bayes - a használt osztályozó

Összefoglaló:
A feladat megoldásához a naív Bayes osztályozót választottam, ami az osztályra vonatkozó feltételes valószínűséget azt feltételezve becsüli meg,
hogy az attribútumok feltételesen függetlenek adott y osztálycímke mellett.
A korpuszban található szavak súlyozására pedig a TF-IDF módszert választottam. 
Ez a statisztikai mérőszám lehetővé teszi egy dokumentumban szereplő kifejezés jelentőségének értékelését a gyűjteményhez vagy korpuszhoz képest.

Az elkészült prediktor az adott hírre ad egy valószínűséget, ami azt mutatja a hír mekkora valószínűséggel álhír, azaz címkéje = 0.