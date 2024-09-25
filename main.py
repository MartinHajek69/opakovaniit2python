#modul ktery nam dokaze davat nahodne cisla
import random
# 1,2, promene se jmenem a prijmenim
jmeno = "Martin"
Prijmeni = "Hájek"
# 3, vypise jmeno a prijmeni
print(jmeno)
print(Prijmeni)
# 4, napisete svuj vek a vypise ho to
vek = int(input("Zadejte věk: "))
print("Váš věk", vek)
# 5, vypise to pocet pismen ve jmene a prijmeni
print("Počet písmen ve jméně:")
print(len(jmeno))
print("Počet písmen ve Příjmení:")
print(len(Prijmeni))
print("-------------------------")
# 6, promena s hodnotou 6
hodnota = 6
# 7,8, cyklus ktery se opakuje 5x pokazde pricte 3 k cislu 6 na konci to vypise vyslednou hodnotu
for i in range(5):
    hodnota += 3
    print(hodnota)
print("vysledna hodnota je 21")

# 10, promena ktera vylosuje nahodne cislo od 1 do 10 a pak ho vypise
nahoda = random.randint(1, 10)
print("nahodna hodnota:")
print(nahoda)
