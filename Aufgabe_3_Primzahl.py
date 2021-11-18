# Name   : Christian Meier
# Klasse : ETS2021
# Datum  : 16.11.2021

minZahl = int(input("Anfang der Liste "))                                           # unter Zahl zum Prüfen
maxZahl = int(input("Ende der Liste "))                                             # obere Zahl zum Prüfen                                                                      
primZahl = []                                                                       # Liste der Primzahlen 

for kantidat in range(minZahl, maxZahl + 1):                                        #
    is_primz = True                                                                 #
    for teiler in range(2, int(kantidat/2)+1):                                      #
        if kantidat % teiler == 0 and teiler < kantidat:                            #
            is_primz = False                                                        #
            break                                                                   #
    if is_primz and kantidat > 1:                                                   #
        primZahl.append(kantidat)                                                   # Primzahlen in die Liste primZahl hinzufügen
print(primZahl)                                                                     # Ausgabe der Liste der Primzahlen

