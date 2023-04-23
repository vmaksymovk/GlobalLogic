słowo = input("Wprowadź słowo: ")
słowo_srodek = słowo[1:-1].lower()
słowo_wynik = słowo[0].upper() + słowo_srodek + słowo[-1].upper()
print("Słowo w formacie: ", słowo_wynik)