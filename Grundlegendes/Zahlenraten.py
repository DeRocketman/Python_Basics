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
