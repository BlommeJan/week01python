'''
Pas de uitvoer als volgt aan (let op het inspringen en de spaties):
*** welkom bij het kassa systeem ***
Hoeveel broeken werden er gekocht? 2
Hoeveel T-shirts werden er gekocht? 3
Hoeveel vesten werden er gekocht? 4
U kocht:
    Broeken: 2 stuk(s)
    T-Shirts: 3 stuk(s)
    Vesten: 4 stuk(s)
Totaal:604.87
'''

print("***Welkom bij het kassasysteem***")
broek = float(70.5)
tshirt = float(20.89)
vest = float(100.3)
aantal_broek = int(input("Hoeveel broeken werden er gekocht? "))
aantal_tshirt = int(input("Hoeveel T-shirts werden er gekocht? "))
aantal_vest = int(input("Hoeveel vesten werden er gekocht? "))
eindprijs = (aantal_broek * broek) + (aantal_tshirt * tshirt) + (aantal_vest * vest)
print(f"U kocht:\n\tBroeken: {aantal_broek} stuk(s)\n\tT-shirts: {aantal_tshirt} stuk(s)\n\tVesten: {aantal_vest} stuk(s)\nTotaal: {eindprijs}")