""" Denne indeholder eksempel kode fra lektion 5 - funktioner.
Det er normalt god skik at definere alle sine funktioner øverst i en fil eller
i en seperat fil"""

import tools as mytools

#en funktion med en parameter (som skal angives)
def hej(navn):
    print("Hej "+navn+" og velkommen til programmet!")

# her er det to obligatoriske paremetre og
# en optional parameter
def print_person(navn,efternavn,alder=-1):
    if alder!=-1:
        print(navn + " " + efternavn + " er "+str(alder) + " år gammel" )
    else:
        print(navn + " " + efternavn)



#vi kan definere funktioner med flere parametre og også med default værdier
#her er der to parametre, som begge har en default værdi - dvs. de er optional parameters.
def beskriv_dyr(navn="",race=""):
    print ("Dit dyr er en/et "+race+" og hedder "+navn)

# vi kan også definere en retur værdi
def ret_linje(x):
    return 2*x+1

def increaseNumber(x):
    x += 1
    print(x)

def addToString(x):
    x = x + " Added"
    print(x)

def greet_people(names):
    for name in names:
        print("Hej "+name)

def greet_people_modify(names):
    names.append("test")

# Bemærk * tegnet.....betyder funktionen kan tage et vilkårligt antal parametre
def list_cities(*cities):
    for city in cities:
        print(city)



hej("martin")
#linjen nedenunder giver en fejl - hvorfor?
#hej()
beskriv_dyr("Willie","spækhugger")
#bemærk at rækkefølgen af parametre er vigtige - så koden nedenunder gør noget andet:
beskriv_dyr("spækhugger","willie")
beskriv_dyr("kat")
beskriv_dyr(race="kat")

print(ret_linje(2))
print("længden af martin :" + str(len("martin")))

######## print person #########
print("####### print person ########")
print_person("martin","knudsen")
print_person("martin","knudsen",40)

# hint: man kan holde ctrl knappen nede og så trykke på en
# funktion for at se input typerne og output typer.
# Virker både på ens egne funktioner og indbyggede funktioner.
venner = ["Jens","Bo","Karin"]
# et eksempel på en funktion som tager en liste (af strings)
greet_people(venner)
### hvad med linjen nedenunder
#greet_people(2)

print("####### modifikation af parametre ########")

# pas på med funktioner - de kan modificerer listen!!!
print("listen før funktionskaldet: ")
print(venner)
greet_people_modify(venner)
print("listen efter funktionskaldet: ")
print(venner)

####typer som ikke bliver ændret #########
print("####### Typer som ikke ændres #######")

mitNavn = "martin"
addToString(mitNavn)
print("Mit navn er : "+mitNavn)
mitTal = 10
increaseNumber(mitTal)
print("Mit tal er : "+ str(mitTal))
#nogle gange ønsker vi at en funktion kan modficere en listen, andre gange ikke.
#hvis du vil være sikker på at listen ikke modificeres så kan du sende en kopi med:

print("####### modifikation af parametre  - send kopi med ########")

venner = ["Jens","Bo","Karin"]
print("listen før funktionskaldet : "+str(venner))
greet_people_modify(venner[:])
print("listen efter funktionskaldet : "+str(venner))
print(venner)

print("************* Funktion med vilkårligt antal parametre ****************")
list_cities("København")
list_cities("Aarhus","København")
#Vi kan også have en funktion som modtager et vilkårligt antal parametre

#vi kan også kalde funktioner fra andre moduler
mytools.hejsa("martin")