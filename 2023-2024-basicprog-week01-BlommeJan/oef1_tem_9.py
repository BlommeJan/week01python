#1 Print je naam, voornaam en e-mail af, telkens op een nieuwe lijn
'''
print("Blomme\nJan\nJan.Blomme@student.howest.be")
'''
#2 Ga na hoe je ook een enkel/dubbel aanhalingstekens, tab, return/enter binnen een tekst kan gebruiken.
#Print volgende tekst af door één lijn code te gebruiken:
'''
print("Labo Basic Programming,\n\t Labo week 1\n\t\tKennismaking met \"Python\",\n\t\tWerken met variabelen.\n Labo Basic Programming,\n\tLabo week 2")
'''
#3 Vraag aan de gebruiker naam, voornaam en leeftijd op. Print nadien in omgekeerde volgorde alles op één lijn af.
#Gebruik hiervoor de formated-string.
'''
naam = input("geef je naam: ")
vnaam = input("geef je voornaam: ")
leeftijd = input("geef je leeftijd: ")
print(f"{leeftijd} {vnaam} {naam}")
'''
#4 Vraag aan de gebruiker de basis en de hoogte van een driehoek op.
#Bereken nadien de oppervlakte en print deze nadien af
'''
basis = float(input("Geef de basis van de driehoek op: "))
hoogte = float(input("Geef de hoogte van de driehoek op: "))
opp = (basis * hoogte)/2
print(f"De oppervlakte bedraagt: {opp}")
'''
#5 Vraag aan de gebruiker het aantal dagen, uren, minuten en seconden op.
# Bepaal het totale aantal seconden.
'''
dagen = int(input("geef het aantal dagen op: "))
uren = int(input("geef het aantal uren op: "))
min = int(input("geef het aantal minuten op: "))
sec = int(input("geef het aantal seconden op: "))
totsec = (dagen * 86400) + (uren * 3600) + (min * 60) + sec
print(f"het totale aantal seconden is: {totsec}")
'''
#6 Vraag aan de gebruiker een aantal seconden op.
# Zet dit aantal om in dagen, uren, minuten en seconden.
'''
totsec = int(input("geef een aantal seconden op: "))
dag = int((totsec - (totsec%86400))/86400)
d_rest = totsec%86400
uur = int((d_rest - (d_rest%3600))/3600)
u_rest = d_rest%3600
min = int((u_rest - (u_rest%60))/60)
m_rest = u_rest%60
sec = int((m_rest - (m_rest%1))/1)
print(f"{dag}:{uur}:{min}:{sec}")
'''
#7 Vraag aan de gebruiker een int-getal n op. Bereken de volgende som: n + nn + nnn.
# Print het resultaat af.
'''
m = (input("geef een getal op: "))
n = int(m)
nn = int(m+m)
nnn = int(m+m+m)
print(n+nn+nnn)
'''
#8 Vraag aan de gebruiker twee int-getallen (gehele getallen) op.
# Bereken nu volgend resultaat: (x + y) * (x + y).
# Print het resultaat af.
'''
getal_x = int(input("geef getal x op: "))
getal_y = int(input("geef getal y op: "))
resultaat = (getal_x + getal_y) * (getal_x + getal_y)
print(f"({getal_x} + {getal_y}) ^ 2 = {resultaat}")
'''
#9 Laat Python de documentatie uitprinten van een aantal ingebouwde commando’s zoals ‘input’, ‘int’, ‘print’
'''
print(input.__doc__)
print("\n--------------------------------\n")
print(int.__doc__)
print("\n--------------------------------\n")
print(print.__doc__)
'''
