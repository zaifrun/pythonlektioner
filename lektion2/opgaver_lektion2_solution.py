""" Denne python fil er en eksempel løsning på opgaverne fra
lektion 2. Der kan være andre varianter at løse opgaverne på, men dette
er mit bud"""


#opgave 1
print("#######Opgave 1 løsning##########")
forfattere = ["Asimov", "Dostojevski", "Philip k. Dick", "Pushkin", "Tolkien"]
for forfatter in forfattere:
    print(forfatter)

#opgave 2
print("#######Opgave 2 løsning##########")

forfattere.append("H.C. Andersen")
for forfatter in forfattere:
    print(forfatter)
del forfattere[1]
for forfatter in forfattere:
    print(forfatter)

#opgave 3
print("########Opgave 3 løsning##########")
antal = len(forfattere)
print("antallet af forfattere er : "+str(antal))

#opgave 4
print("#######Opgave 4 løsning##########")
forfattere.reverse()
for forfatter in forfattere:
    print(forfatter)



#opgave 5
print("#######Opgave 5 løsning########")
tal_liste = range(1,11)
for tal in tal_liste:
    print(tal)
nyliste = range(3,100,3)
for tal in nyliste:
    print(tal)

#opgave 6
from statistics import mean
print("#########Opgave 6 løsning##########")
print ("minimum: "+str(min(nyliste)))
print ("max: "+str(max(nyliste)))
print ("sum: "+str(sum(nyliste)))
avg = sum(nyliste)/len(nyliste)
print("average: "+str(avg))
print("mean: "+str(mean(nyliste)))
sum = 0
for tal in nyliste:
    sum = sum + tal
gennemSnit = sum/len(nyliste)
print("mit manuelle gennemsnit "+str(gennemSnit))


#opgave 7
print("#######Opgave 7 løsning##########")
print(forfattere[0:3])
print(forfattere[3:5])


#opgave 8
print("#########Opgave 8 løsning#########")

kopi = forfattere[:]
kopi.append("Shakespeare")
print(kopi)
print(forfattere)


#opgave 9
print("#########Opgave 9 løsning#########")
familie = ("Marianne","Peter","Tao")
#linjen nedenunder vil ikke virke og du får en warning i pycharm.
#familie[0] = "Claus"


