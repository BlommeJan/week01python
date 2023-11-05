'''
Schrijf een programma dat een kassasysteem nabootst.
• Een broek kost 70,5 euro.
• Een T-shirt kost 20,89 euro.
• Een vest kost 100,3 euro.
De gebruiker geeft per item het aantal gekochte goederen in. De computer berekent het te betalen
bedrag.
'''

# Welcome message for the cash register system.
print("***Welkom bij het kassasysteem***")

# Define the prices of items as floating-point numbers.
broek = float(70.5)
tshirt = float(20.89)
vest = float(100.3)

# Ask the user to input the quantity of each item.
aantal_broek = int(input("Hoeveel broeken werden er gekocht? "))
aantal_tshirt = int(input("Hoeveel T-shirts werden er gekocht? "))
aantal_vest = int(input("Hoeveel vesten werden er gekocht? "))

# Calculate the total cost by multiplying the quantity of each item by its price and summing them up.
eindprijs = (aantal_broek * broek) + (aantal_tshirt * tshirt) + (aantal_vest * vest)

# Display the total amount to be paid.
print(f"Totaal te betalen:\n {eindprijs}")
