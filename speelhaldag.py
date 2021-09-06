ToegangsPrijs = 7.45
PrijsPer5min = 0.37

bedrag = ((ToegangsPrijs * 4) + (PrijsPer5min * 9 ))

factuurtekst = "Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar " + str(bedrag) + " euro "

print(factuurtekst)