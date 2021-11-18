# Name  :   Christian Meier
# Klasse:   ETS2021
# Datum :   12.11.2021

Zahlen = []

minZahl = int(input("Untere Grenzahl "))             # Eingabe einer Zahlt
maxZahl = int(input("Obere Grenzahl "))              # Eingabe einer höeren Zahl 


for i in range(minZahl,maxZahl+1):
    if i % 9 ==0 and i > 2:
        Zahlen.append(i)
print(Zahlen)