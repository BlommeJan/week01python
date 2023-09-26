'''
Schrijf een programma dat een kassasysteem nabootst.
• Een broek kost 70,5 euro.
• Een T-shirt kost 20,89 euro.
• Een vest kost 100,3 euro.
De gebruiker geeft per item het aantal gekochte goederen in. De computer berekent het te betalen
bedrag.
'''

print("***Welkom bij het kassasysteem***")
broek = float(70.5)
tshirt = float(20.89)
vest = float(100.3)
aantal_broek = int(input("Hoeveel broeken werden er gekocht? "))
aantal_tshirt = int(input("Hoeveel T-shirts werden er gekocht? "))
aantal_vest = int(input("Hoeveel vesten werden er gekocht? "))
eindprijs = (aantal_broek * broek) + (aantal_tshirt * tshirt) + (aantal_vest * vest)
print(f"Totaal te betalen:\n {eindprijs}")