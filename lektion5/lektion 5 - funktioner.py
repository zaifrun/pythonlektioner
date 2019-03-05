""" Denne indeholder eksempel kode fra lektion 5 - funktioner.
Det er normalt god skik at definere alle sine funktioner øverst  -
måske endda i en fil, hvis de skal genbruges andre steder"""

import tools as mytools


# en funktion med en parameter (som skal angives)
def hej(navn):
    print("Hej "+navn+" og velkommen til programmet!")


# her er det to obligatoriske parametre og
# en optional parameter
def print_person(navn, efternavn="", alder=-1):
    if alder != -1:
        print(navn + " " + efternavn + " er "+str(alder) + " år gammel")
    else:
        print(navn + " " + efternavn)

#virker ikke! Der mangler jo nogle parametre
print_person()
print_person("martin")
print_person("martin","knudsen")
print_person("martin","knudsen",40)
print_person(alder=40,navn= "martin",efternavn = "knudsen")


# vi kan definere funktioner med flere parametre og også med default
# værdier.
# her er der to parametre, som begge har en default værdi -
# dvs. de er optional parameters.
def beskriv_dyr(navn="", race=""):
    print("Dit dyr er en/et "+race+" og hedder "+navn)


# vi kan også definere en retur værdi
def ret_linje(x):
    return 2*x+1


# statisk type angivelse - muligt i python 3.0+
# NB: Dette er ikke vist i bogen!!
def ret_linje_statisk(x: float) -> float:
    return 2*x + 1


def increase_number(x):
    x += 1
    print(x)


def add_to_string(x):
    x = x + " Added"
    print(x)


def greet_people(names):
    for name in names:
        print("Hej "+name)


def greet_people_modify(names):
    names.append("test")


# Bemærk * tegnet.....betyder funktionen kan tage et
# vilkårligt antal parametre
def list_cities(*cities):
    for city in cities:
        print(city)


hej("martin")
# linjen nedenunder giver en fejl - hvorfor?
# hej()
beskriv_dyr("Willie", "spækhugger")
# bemærk at rækkefølgen af parametre er vigtige -
# så koden nedenunder gør noget andet:
beskriv_dyr("spækhugger", "willie")
beskriv_dyr("kat")
beskriv_dyr(race="kat")

######### numeriske værdier til en funktion ############
print("######## numeriske værdier i en funktion #######")
print("resultatet er " + str(ret_linje(2)))
# næste linje giver en fejl - hvorfor?
print(ret_linje("benny"))

# statisk type
ret_linje_statisk("benny")
# print("resultatet er "+ ret_linje_statisk(10))
# demonstration af indbyggede funktioner
print("længden af martin :" + str(len("martin")))

######## print person #########
print("####### print person ########")
print_person("martin", "knudsen")
print_person("martin", "knudsen", 40)

# hint: man kan holde ctrl knappen nede og så trykke på en
# funktion for at se input typerne og output typer.
# Virker både på ens egne funktioner og indbyggede funktioner.
venner = ["Jens", "Bo", "Karin"]
# et eksempel på en funktion som tager en liste (af strings)
greet_people(venner)
# hvad med linjen nedenunder
venner2 = [10, 20, 30]
#dette virker ikke, fordi at listen nu indeholder tal.
#greet_people(venner2)

print("####### modifikation af parametre ########")

# pas på med funktioner - de kan modificerer listen!!!
print("listen før funktionskaldet: ")
print(venner)
greet_people_modify(venner)
print("listen efter funktionskaldet: ")
print(venner)

#### typer som ikke bliver ændret #########
print("####### Typer som ikke ændres #######")

mit_navn = "martin"
add_to_string(mit_navn)
print("Mit navn er : "+mit_navn)
mit_tal = 10
increase_number(mit_tal)
print("Mit tal er : " + str(mit_tal))
# nogle gange ønsker vi at en funktion kan modficere en listen,
# andre gange ikke.
# hvis du vil være sikker på at listen ikke modificeres så kan du
# sende en kopi med:
print("####### modifikation af parametre  - send kopi med ########")

venner = ["Jens", "Bo", "Karin"]
print("listen før funktionskaldet : "+str(venner))
greet_people_modify(venner[:])
print("listen efter funktionskaldet : "+str(venner))
print(venner)

print("************* Funktion med vilkårligt antal parametre ****************")
list_cities("København")
list_cities("Aarhus", "København")
list_cities("Aarhus", "København","Berlin","New York")
list_cities(1,23,44,45454,4545454545)

# Vi kan også have en funktion som modtager et vilkårligt
# antal parametre

# vi kan også kalde funktioner fra andre moduler
mytools.hejsa("martin")
mytools.hejsa2()
