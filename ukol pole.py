skola = ["propiska", "guma", "tužka", "sešit", "svačina", "kružítko"]
delka = len(skola)
print("Délka pole:", delka)
print("Hodnoty v poli:")
for prvek in skola:
    print(prvek)
novy_prvek = input("Zadejte nový prvek: ")
skola.append(novy_prvek)
skola.pop(1)
skola.sort()
skola.reverse()
print("Obrácené pole:")
for prvek in skola:
    print(prvek)