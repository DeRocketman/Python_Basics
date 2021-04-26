# Shebang, oder auch Magicline genannt macht eine direkte Ausführung eines Python-Skripts unter Linux möglich
# Der zweite ausdruck ist noch besser geeignet, da sie vom tatsächlichen Installationsort von Python unabhängig ist

# !/usr/bin/python
# !/usr/bin/env python

# und es muss die Executable-Flag gesetzt sein mit (Ohne Kommentar)
# chmod +x dateiname

# Das 1. Programm:
# Initialisierung die funktion random.randint wählt eine zufällige Zahl zwischen den angegebenen Werten
import random

geheimnis = random.randint(1, 1000000)
versuch = -1
zaehler = 0

# Es folgt eine while Schleife mit Schleifenkopf und Schleifenrumpf bzw Schleifenkörper
# Entscheidend ist die Einrückung.
while versuch == geheimnis:
    versuch = int(input("Raten Sie: "))

    if versuch < geheimnis:
        print("Zu klein")
    if versuch > geheimnis:
        print("Zu groß")

    zaehler = zaehler + 1

if zaehler == 1:
    print("WOW beim 1. Versuch gleich getroffen. Schon mal an Lottospielen gedacht?")
else:
    print("Supidupi, Sie haben es in", zaehler, "Versuchen geschafft! Unfassbar!")

# Ein Bot soll mal raten :-)

print("Nun bin ich, der Rate-Bot, mal dran:")
zaehler2 = 0
geheimnis2 = int(input("Gib eine Zahl ein, die ich erraten soll "))
obereSchranke = int(input("Gib eine Zahl als obere Begrenzung ein(Muss größer oder gleich der gesuchten Zahl sein!) "))
untereSchranke = 1
versuch2 = obereSchranke
print("Gut, nun geht es los. Ich suche eine Zahl zwischen:", untereSchranke, " und ", obereSchranke)

while versuch2 != geheimnis2:
    print("Ich nehme: ", versuch2)

    if versuch2 < geheimnis2:
        print("Zu klein")
        untereSchranke = versuch2
        if (untereSchranke + obereSchranke) % 2 == 0:
            versuch2 = (obereSchranke + untereSchranke) / 2
        else:
            versuch2 = (obereSchranke + untereSchranke + 1) / 2
    if versuch2 > geheimnis2:
        print("Zu groß")
        obereSchranke = versuch2
        if (untereSchranke + obereSchranke) % 2 == 0:
            versuch2 = (obereSchranke + untereSchranke) / 2
        else:
            versuch2 = (obereSchranke + untereSchranke + 1) / 2

    if versuch2 == 2:
        versuch2 = 1
    zaehler2 = zaehler2 + 1

if zaehler2 == 1:
    print("WOW beim 1. Versuch gleich getroffen. Ich sollte mal Lotto spielen. Aber mit welchen Zahlen?")
else:
    print("Supidupi, ich haben es in", zaehler2, "Versuchen geschafft! Unfassbar!")

# for - Schleife
x = ["Python", "Java", "JavaScript"]

for w in x:
    print(w)
print("FERTIG")

# for - Schleife als Zählschleife
for i in range(5):
    print(i)


# zählt von 0-5, auch möglich start und ende oder mit Schrittgröße range(start, ende, schritt)

# Funktionen mit keyword def (definition) und Funktionsbezeichnung
def funk():
    for j in range(0, 20):
        print(j)


# Funktionen mit Parameter

def funkParam(n, m, s):
    for p in range(n, m, s):
        print(p)


# Funktionsaufruf
funk()
funkParam(0, 10000000, 2)
