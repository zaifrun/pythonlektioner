""" Denne indeholder eksempel kode fra lektion 5 - funktioner.
Det er normalt god skik at definere alle sine funktioner øverst i en fil eller
i en seperat fil"""

import tools as t

#en funktion med en parameter (som skal angives)
def hej(navn):
    print("Hej "+navn+" og velkommen til programmet!")


#vi kan definere funktioner med flere parametre og også med default værdier
#her er der to parametre, som begge har en default værdi - dvs. de er optional parameters.
def beskriv_dyr(navn="",race=""):
    print ("Dit dyr er en/et "+race+" og hedder "+navn)

# vi kan også definere en retur værdi
def ret_linje(x):
    return 2*x+1


def greet_people(names):
    for name in names:
        print("Hej "+name)

def greet_people_modify(names):
    names.append("test")

# Bemærk *
def list_cities(*cities):
    for city in cities:
        print(city)


#linjen nedenunder giver en fejl - hvorfor?
#hej()
hej("martin")
beskriv_dyr("Willie","spækhugger")
#bemærk at rækkefølgen af parametre er vigtige - så koden nedenunder gør noget andet:
beskriv_dyr("spækhugger","willie")
beskriv_dyr("kat")
beskriv_dyr(race="kat")

print(ret_linje(2))

venner = ["Jens","Bo","Karin"]
# et eksempel på en funktion som tager en liste (af strings)
greet_people(venner)
### hvad med linjen nedenunder
##greet_people(2)

# pas på med funktioner - de kan modificerer listen!!!
print(venner)
#greet_people_modify(venner)
print(venner)

#nogle gange ønsker vi at en funktion kan modficere en listen, andre gange ikke.
#hvis du vil være sikker på at listen ikke modificeres så kan du sende en kopi med:

greet_people_modify(venner[:])
print(venner)

print("************* Funktion med vilkårligt antal parametre ****************")
list_cities("København")
list_cities("Aarhus","København")
#Vi kan også have en funktion som modtager et vilkårligt antal parametre

t.hejsa("martin")