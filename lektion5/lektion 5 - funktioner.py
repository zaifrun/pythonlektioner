""" Denne indeholder eksempel kode fra lektion 5 - funktioner.
Det er normalt god skik at definere alle sine funktioner øverst i en fil eller
i en seperat fil"""

#en funktion med en parameter (som skal angives)
def hej(navn):
    print("Hej "+navn+" og velkommen til programmet!")

#vi kan definere funktioner med flere parametre og også med default værdier
#her er der to parametre, som begge har en default værdi
def beskriv_dyr(navn="",race=""):
    print ("Dit dyr er en/et "+race+" og hedder "+navn)

# vi kan også definere en retur værdi
def ret_linje(x):
    return 2*x+1


def greet_people(names):
    for name in names:
        print("Hej "+name)

#linjen nedenunder giver en fejl
#hej()
hej("martin")
beskriv_dyr("Willie","spækhugger")

#bemærk at rækkefølgen af parametre er vigtige.
beskriv_dyr("kat")
beskriv_dyr(race="kat")

print(ret_linje(2))

venner = ["Jens","Bo","Karin"]
greet_people(venner)

