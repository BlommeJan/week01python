# Om de prijs van een woning te bepalen, telt men de prijs van de bouwgrond en de eigenlijke bouw op.
# Het btw-tarief op dit totaal is 21 %.
# Je vraagt aan de gebruiker de prijs van de bouwgrond en de prijs van het gebouw.
# Je toont het totaal te betalen bedrag.
# Prijs van de bouwgrond? 125000
# Prijs van het gebouw? 180000
# De totale kostprijs van het project is: 369050.0

bouwgrond = float(input("Prijs van de bouwgrond? "))
gebouw = float(input("Prijs van de gebouw? "))
prijs_met_btw = (bouwgrond + gebouw) * 1.21
print(f"De totale kostprijs van het project is: {prijs_met_btw}")