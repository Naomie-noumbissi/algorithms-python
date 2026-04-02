def linera_suche(liste,x):
    for i in range(len(liste)):#alle Elemente der Liste
        if liste[i]==x:
            return i #gedunden in der Position i
    return -1 #Nicht gefunden
liste=["orange","banane","citron", "oeuf"]
position=linera_suche(liste,"banane")
print("Das Element ist in der Position",position)

def binare_suche(elements,x):
    links=0
    recht=len(elements)-1
    while links<= recht:
        mitte=(links+recht)//2 #wir teilen die Liste
        werte=elements[mitte]
        if werte==x: #Element in der Mitte gefunden
           return f" in Position {mitte} gefunden"
        elif werte< x:
              links= mitte + 1 #weiter recht suchen
        else:
               recht=mitte-1 #weiter links suchen
    return -1 #nicht gefunden

element=[2,4,6,8,9,10]
wo=binare_suche(element,2)
print("Die elemet ist:",wo)

def bubble_sort(bubble):
    n=len(bubble)
    for i in range(n):
        for j in range(n-i-1):
            if bubble[j]>bubble[j+1]:
                bubble[j], bubble[j+1] = bubble[j+1], bubble[j] #Elemente tauschen
    return bubble
listen=[1,9,4,7,3,5,2]
print(f"Die gute Liste ist:{bubble_sort(listen)}")

def merge(links, rechts):
    ergebnis = []
    i = 0
    j = 0

    # Vergleiche Elemente beider Listen
    while i < len(links) and j < len(rechts):
        if links[i] < rechts[j]:
            ergebnis.append(links[i])
            i += 1
        else:
            ergebnis.append(rechts[j])
            j += 1

    # Restliche Elemente anhängen
    ergebnis.extend(links[i:])
    ergebnis.extend(rechts[j:])

    return ergebnis


def merge_sort(liste):
    # Basisfall: Liste mit 0 oder 1 Element ist sortiert
    if len(liste) <= 1:
        return liste

    # Liste teilen
    mitte = len(liste) // 2
    linke_haelfte = liste[:mitte]
    rechte_haelfte = liste[mitte:]

    # Rekursiv sortieren
    sortiert_links = merge_sort(linke_haelfte)
    sortiert_rechts = merge_sort(rechte_haelfte)

    # Zusammenfügen
    return merge(sortiert_links, sortiert_rechts)

    #binäre Suche.
def binare_suche(elements,x):
    links=0
    recht=len(elements)-1
    while links<= recht:
        mitte=(links+recht)//2
        werte=elements[mitte]
        if werte==x:
            return f"gefunden in Position {mitte}"
        elif werte< x:
            links= mitte + 1
        else:
            recht=mitte-1
    return -1 #nicht gefund

# Test
liste = [7, 3, 9, 2, 5, 1, 6]
print("Unsortierte Liste:", liste)

sortierte_liste = merge_sort(liste)
print("Sortierte Liste:", sortierte_liste)
n=int(input("Geben sie die gesuchte Zahl"))
print(f"Die Element ist {binare_suche(sortierte_liste,n)}")