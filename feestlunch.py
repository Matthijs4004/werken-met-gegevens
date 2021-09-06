Croissantjes = 17
PrijsCroissant = 0.39
Stokbroden = 2
PrijsStokbrood = 2.78
Korting = 1.50

bedrag = ((Croissantjes * PrijsCroissant) + (Stokbroden * PrijsStokbrood) - Korting)

factuurtekst = "De feestlunch kost je bij de bakker " + str(bedrag) + " euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!"

print(factuurtekst)