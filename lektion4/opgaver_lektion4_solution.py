""" Denne python fil er en eksempel løsning på opgaverne fra
lektion 4.
Der kan være andre varianter eller udvidelser at løse opgaverne på,
men dette er mit bud"""

##### Opgave 1 ##############

print("######### opgave 1 ##########")
car = input("Hvilke slags bil vil du leje?")
print("Lad mig se om jeg kan finde en "+car)

antal = int(input("Hvor mange skal spise her?"))
if antal > 8:
    print("I er mange, så I må lige vente på et stort bord")
else:
    print("Fint, vi har et ledigt bord nu")


###### Opgave 2 ###########
print("########### opgave 2 ############")
samlet_pris = 0
print("#####Velkommen til BioCity ###########")
print("Indtast q for at afslutte")
while True:
    alder = input("Hvad er næste persons alder?")
    if alder == 'q':
        break
    alder = int(alder)
    if alder < 3:
        print("biletten er gratis")
    elif 3 <= alder <= 12:
        print("billetten koster 10 dollars")
        samlet_pris += 10
    else:
        print("billetten koster 15 dollars")
        samlet_pris += 15
print("samlet pris bliver så: "+str(samlet_pris))
# indsætter en tom linje
print()



###### Opgave 3 ###########
print("#########Opgave 3 ##########")
pakkeliste = []
ting = 0
print("########### Velkommen til pakkelisten #############")
print("Du kan altid quitte ved at indtaste 'q'")
while ting < 5:
    nye_ting = input("Hvad vil du sætte på pakkelisten?")
    if nye_ting == 'q':
        break
    else:
        pakkeliste.append(nye_ting)
        ting += 1
print("Din pakkeliste indeholder:")
for item in pakkeliste:
    print(item)


###### Opgave 4 ############
print("########Opgave 4 ###############")
print("*********Velkommen til ordbogsprogrammet*************")
mereInput = True
ordbog = {"farvel": "goodbye",
          "mor": "mother",
          "far": "dad"}
while mereInput:
    dansk = input("Indtast dansk ord:")
    engelsk = input("Indtast engelsk oversættelse:")
    if dansk == "q" or engelsk == "q":
        mereInput = False
    else:
        ordbog[dansk] = engelsk

for dansk, engelsk in ordbog.items():
    print(dansk + " -> "+engelsk)

#########Opgave 5 #######################
print("########## Opgave 5 ###########")
print("Tak, nu kan du bruge ordbogen!")
mereInput = True
while mereInput:
    ordet = input("Indtast ord du gerne vil have oversæt fra dansk til engelsk")
    if ordet in ordbog.keys():
        print("på engelsk: "+ordbog[ordet])
    else:
        if ordet == "q":
            break
        print("Vi kan ikke finde dette ord i ordbogen")
print("Tak for at bruge ordbogen, vi ses!")

############Opgave 6 ##############
print("########Opgave 6 ###############")
engelsk_dansk = {}
for key, value in ordbog.items():
    engelsk_dansk[value] = key
print(engelsk_dansk)
mereInput = True
while mereInput:
    ordet = input("Indtast ord du gerne vil have oversæt fra engelsk til dansk")
    if ordet in engelsk_dansk.keys():
        print("på dansk: "+engelsk_dansk[ordet])
    else:
        if ordet == "q":
            break
        print("Vi kan ikke finde dette ord i ordbogen")
print("Tak for at bruge ordbogen, vi ses!")

###### Opgave 7 #############
print("####### Opgave 7 #########")

# for loop
for x in range(0, 11):
    print(x)

# tilsvarende while loop
print("for løkke til en while løkke")
x = 0
while x < 11:
    print(x)
    x += 1

print("while løkke til en for løkke")
# en while løkke
tal = [20, 30, 40, 50, 60, 70]
index = 0
while tal[index] < 50:
    print(tal[index])
    index += 1

for nr in tal:
    if nr < 50:
        print(nr)
    else:
        break


# Vi kan faktisk godt lave en uendelig løkke i python
#  med en for loop

"""
import itertools
for i in itertools.count():
    print("uendelig løkke")
"""

