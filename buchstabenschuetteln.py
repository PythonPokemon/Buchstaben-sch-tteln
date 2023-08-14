from collections import Counter

def anagramm(wort_1, wort_2):
    laenge_1 = len(wort_1)
    laenge_2 = len(wort_2)

    if laenge_1 != laenge_2:
        print("Das Wortpaar " + wort_1 + " und " + wort_2 + " ist kein Anagramm.")
    else:
        c1 = Counter(wort_1)
        c2 = Counter(wort_2)
    
    if c1 == c2:
        print("Das Wortpaar " + wort_1 + " und " + wort_2 + " ist ein Anagramm.")
    else:
        print("Das Wortpaar " + wort_1 + " und " + wort_2 + " ist kein Anagramm.")

def palindrom(wort):
    laenge = len(wort)
    i = 0
    j = int(laenge-1)
    k = "yes"

    while i < laenge/2:

        if wort[i] == wort[j]:
            i += 1
            j -= 1
        else:
            print("Das Wort " + wort + " ist kein Palindrom")
            k = "no"
            break
    
    if k == "yes":
        print("Das Wort " + wort + " ist ein Palindrom")
        
wahl = "z"

while wahl!="a" and wahl!="A" and wahl!="p" and wahl!="P" and wahl!="n" and wahl!="N":
    print ("Geben Sie bitte zwei Wörter ein:")
    wort_1 = input("1. Wort: ")
    wort_2 = input("2. Wort: ")
    print ("Was möchten Sie?")
    wahl = input("Anagram (a oder A) oder Palindrom (p oder P)")

    if wahl == "a" or wahl == "A":
        anagramm(wort_1, wort_2)

    elif wahl == "p" or wahl == "P":
        palindrom(wort_1)
        palindrom(wort_2)
    else:
        print ("Bitte wählen Sie eine der beiden Möglichkeiten!")

    wahl = input("Möchten Sie noch einen Durchgang? (j/J) oder (n/N)" )
    
    