from accessories import Accessories
from insurencerecords import InsuranceRecords
from insurencer import Insured


databaze = {}
pokracovat = True
evidence = InsuranceRecords(databaze)
doplnky = Accessories()
while pokracovat:
    print("------------------------------------------")
    print("Evidence pojištěných")
    print("------------------------------------------ \n")
    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    while True:
        try:
            volba = int(input())
            break
        except ValueError:
            print("Prosím zadejte číslo.")

    if volba == 1:
        jmeno = input("Zadejte jméno pojištěného: \n").strip().title()
        prijmeni = input("Zadejte příjmení: \n").strip().title()
        tel = input("Zadejte telefonní číslo: \n")
        vek = input("Zadejte věk: \n")
        pojistitel = Insured(jmeno, prijmeni, tel, vek)
        evidence.add(pojistitel)
        print("Data byla uložena. Pokračujte libovolnou klávesou \n")
        input()
        doplnky.clear_screen()
    elif volba == 2:
        print(evidence.reader())
        print("Pokračujte libovolnou klávesou... \n")
        input()
        doplnky.clear_screen()
    elif volba == 3:
        jmeno = input("Zadejte jméno pojištěného: \n").strip().title()
        prijmeni = input("Zadejte příjmení pojištěného: \n").strip().title()
        insured_finder = Insured(jmeno, prijmeni, "", "")
        evidence.id_finder(insured_finder)
        if evidence.id_finder(insured_finder) == None:
            print("Pojištěnec nebyl nalezen \n")
        else:
            print(evidence.id_finder(insured_finder))
        print("Pokračujte libovolnou klávesou... \n")
        input()
        doplnky.clear_screen()
    elif volba == 4:
        doplnky.clear_screen()
        pokracovat = False