# Name  :   Christian Meier
# Klasse:   ETS2021
# Datum :   12.11.2021

Zahlen = []

minZahl = 0
maxZahl = 90


for i in range(maxZahl-minZahl):
    pruefZahl = (minZahl + i) % 9 == 0
