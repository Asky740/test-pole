zbozi = ["Banan", "Jablko", "Hruska", "Pomeranc", "Jahoda"]
kosik = []

def vypis_pole(prvek):
    for x in range(len(prvek)): 
        print(f"{x+1}: {prvek[x]}")

def nadpis_zbozi():
    print(" ")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print(" ")
    print("                          Zbývající zboží:")
    print(" ")

def nadpis_kosik():
    print(" ")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print(" ")
    print("                              Váš košík:")
    print(" ")

print(" ")
print("Dobrý den, Vítejte v obchodě Potraviny.")
print("Zadejte číslo nebo název produktu, který chcete z nabídky přidat do košíku.")
print("Zadáním příkazu *konec* ukončíte nákup.")

while len(zbozi) > 0:
    nadpis_zbozi()
    vypis_pole(zbozi)
    nadpis_kosik()
    vypis_pole(kosik)
    print(" ")

    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print(" ")
    prikaz = input("Zadejte název zboží nebo příkaz: ")
    print(" ")
    print(" ")
    print(" ")

    if prikaz == "Banan":
        kosik.append(prikaz)
        zbozi.remove(prikaz)

    elif prikaz == "Jablko":
        kosik.append(prikaz)
        zbozi.remove(prikaz)

    elif prikaz == "Hruska":
        kosik.append(prikaz)
        zbozi.remove(prikaz)

    elif prikaz == "Pomeranc":
        kosik.append(prikaz)
        zbozi.remove(prikaz)

    elif prikaz == "Jahoda":
        kosik.append(prikaz)
        zbozi.remove(prikaz)

    elif prikaz == "1":
        kosik.append("Banan")
        zbozi.remove("Banan")

    elif prikaz == "2":
        kosik.append("Jablko")
        zbozi.remove("Jablko")

    elif prikaz == "3":
        kosik.append("Hruska")
        zbozi.remove("Hruska")

    elif prikaz == "4":
        kosik.append("Pomeranc")
        zbozi.remove("Pomeranc")

    elif prikaz == "5":
        kosik.append("Jahoda")
        zbozi.remove("Jahoda")
    
    elif prikaz == "konec":
        break

    else:
        print("tf bro")

print(" ")
print(" ")
print(" ")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print(" ")
print("Zboží zaplaceno, děkujeme za nákup!")
print(" ")

