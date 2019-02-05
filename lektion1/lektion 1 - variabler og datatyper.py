""" Denne fil indeholder eksempel kode på emner fra lektion 1 omkring
    variabler og datatyper """

print("lektion 1 - variabler og datatyper")

# variabler - brug lower case generelt - underscore kan bruges - brug IKKE æøå som variabel navne
hilsen = "Hej med jer!"
lordag = "lørdag"
hilsen_til_alle = "Hilsen til hele verden herfra EAAA"
hilsenTilAlle = "Hilsen....."
print(hilsen)
print(lordag)

#strings - definition og konkatenation. New lines i strings.

#metoder på strings

message = "hej med dig"
print(message)
navn = "Martin"
efterNavn = "Knudsen"
fuldtNavn = navn+" "+efterNavn
print(fuldtNavn)
#CTRL-Space er nyttigt for code completion


#Integers og Floats - brug af str() funktionen til konvertering

yndlingsTal = 10
etNytTal = 20
sum = yndlingsTal+etNytTal
strYndlingsTal = str(yndlingsTal)
sum2 = "mit yndlingstal er: " + strYndlingsTal
print("mit yndlingstal er stadigvæk "+strYndlingsTal)
print(sum2)
#eksempel på type error - int og string

point = 9.5
print(" Du fik "+str(point)+" point i konkurrencen")

# matematik med +,-,*,/ i python, samt power **
produkt = etNytTal*yndlingsTal
produkt2 = 2**4
print(produkt)

# multi-line kommentar med 3 x "