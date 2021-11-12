# Name  :   Christian Meier
# Klasse:   ETS2021
# Datum :   12.11.2021

Zahlen = []

minZahl = 0
maxZahl = 90


for i in range((maxZahl + 1) - minZahl):
    pruefJahr = minZahl + i
    if (pruefJahr % 9 == 0):
        Zahlen.append(pruefJahr)
        print(i)
