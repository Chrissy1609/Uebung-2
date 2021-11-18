# Name   : Christian Meier
# Klasse : ETS 2021
# Datum  : 16.11.2021               # https://www.finanzen-rechner.net/kredit/monatsrate-berechnen.html  
 
import math    
 
Krieditsumme    = int(input("Krieditsumme in € "))                                      # Wie viel Geld ich von der Bank geliehen habe
Zinsatz         = int(input("Zinsatz in % "))                                           # Wie viel Zinsen ich zu Zahlen habe in %
Jahre           = int(input("Zeit der Rate in Jahre "))                                 # Jahre die betragen um Schuldenfrei zu sein

alleMonate = Jahre   * 12                                                               # alle Monate errechnen die zu Zahlen sind
Zinsen     = Zinsatz / 100                                                              # umrechnen der Tinsen für die Formel 

monatlicheRate = Krieditsumme * (Zinsen / 12) / (1- (1+ Zinsen / 12)**-alleMonate)      # Rate zu Zahlende ist 
zahlendeRate = (math.ceil(monatlicheRate *100) / 100)                                   # Rate auf eine Zahlbare Rate runden

print(zahlendeRate, "€ die im Monat als Rate anfallen")                                 # Anzeigen wie viel ich Zahlen muss