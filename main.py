import random
jmeno = "Martin"
Prijmeni = "Hajek"

print(jmeno)
print(Prijmeni)

vek = int(input("Zadejte věk: "))
print("Váš věk", vek)
print("Počet písmen ve jméně:")
print(len(jmeno))
print("Počet písmen ve Příjmení:")
print(len(Prijmeni))
print("-------------------------")

hodnota = 6

for i in range(5):
    hodnota += 3
    print(hodnota)
print("vysledna hodnota je 21")

