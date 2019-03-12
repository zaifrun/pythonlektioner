""" Denne python fil er en eksempel løsning på opgaverne fra
lektion 5. Der kan være andre varianter at løse opgaverne på, men dette
er mit bud"""

###Opgave 8-3 fra bogen ########

def make_shirt(size,message):
    print("En t-shirt med størrelse "+size+ " med teksten: "+message)

make_shirt("L","Python rules")
make_shirt(message="Hej", size="XL")


#######Opgave 8-5 fra bogen ##########

def describe_city(city,country="Denmark"):
    print(city+ " is in "+country)

describe_city("Aarhus")
describe_city("N.Y","USA")
describe_city("Berlin","Germany")

######## opgave 2 ###############

def sum(numbers):
    sum = 0
    for n in numbers:
        sum+=n
    return sum

print("sum = "+str(sum([1,2,3,4])))

######### opgave 3 #############

def sum2(numbers):
    sum = 0
    for n in numbers:
        sum += n
    numbers.append(sum)

minListe = [1,2,3]
print(minListe)
sum2(minListe)
print(minListe)
sum2(minListe[:])
print(minListe)

######## opgave 4 ############
def borrowBooks(*books):
    print("Antal bøger: "+str(len(books)))
    for book in books:
        print(book)

borrowBooks("Idioten")
borrowBooks("Idioten","Forbrydelse og straf")


######## opgave 6 ################
tekst = "     Det er marts måned"
print(tekst)
print("uden leading space : "+tekst.strip())
tal = "10"
print(tal +" er digit : "+str(tal.isdigit()))
minliste = ["æbler","pærer","bananer","kokosnødder"]
print("#".join(minliste))

#### Opgave 7 #################
import matplotlib.pyplot as plt
import numpy as np

#Vi skal bare have nogle tilfælde tal.
np.random.seed(19680801)
#generer 100 x og y værdier - taget fra normalfordelingen
data = np.random.randn(2, 100)

fig, axs = plt.subplots(3, 2, figsize=(6, 6))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
axs[2, 0].scatter(x,y)
plt.show()


####Opgave 8 -  statisk type angivelse ########

print("######### Opgave 8 ############")
def kvadrat(x:float) -> str:
    return str(x*x)


print("resultatet er "+kvadrat(5.5))

from typing import List

def minsum(liste : List[int]) -> str:
    resultat = 0
    for nr in liste:
        resultat+=nr
    return str(resultat)


liste = [1.4,2,3,4]
print("summen er : "+minsum(liste))

liste2 = ["anders","martin","benny"]
#print("summen er : "+minsum(liste2))
