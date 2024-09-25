#modul ktery nam dokaze davat nahodne cisla
import random
#promene se jmenem a prijmenim
jmeno = "Martin"
Prijmeni = "Hájek"
#vypise jmeno a prijmeni
print(jmeno)
print(Prijmeni)
#napisete svuj vek a vypise ho to
vek = int(input("Zadejte věk: "))
print("Váš věk", vek)
#vypise to pocet pismen ve jmene a prijmeni
print("Počet písmen ve jméně:")
print(len(jmeno))
print("Počet písmen ve Příjmení:")
print(len(Prijmeni))
print("-------------------------")
#promena s hodnotou 6
hodnota = 6
#cyklus ktery se opakuje 5x pokazde pricte 3 k cislu 6 na konci to vypise vyslednou hodnotu
for i in range(5):
    hodnota += 3
    print(hodnota)
print("vysledna hodnota je 21")

#promena ktera vylosuje nahodne cislo od 1 do 10 a pak ho vypise
nahoda = random.randint(1, 10)
print("nahodna hodnota:")
print(nahoda)
