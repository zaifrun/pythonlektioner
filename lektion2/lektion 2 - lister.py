""" Denne indeholder eksempel kode fra lektion 2 - arbejde med lister"""

print("lektion 2 - lister")

#definition af en liste

minliste = []

navne = ["Martin", "benny"]
talliste = [10, 20, 30, 40]


#udskrivning af lister
print(minliste)
print(navne)
print(talliste)
#tilgå enkelte elementer - med [] notation

#modificer elementer
navne[1] = "Keld"

#tilføje nye elementer til slutningen - med append
navne.append("Kurt")

#tilføje elementer et sted i listen med insert
navne.insert(1, "Rasmus")
print(navne)

#slet elementer med del kommandoen - del list[2]
del navne[-1]  # fjerner Kurt.
midten = len(navne)//2

print("Midten er "+str(midten))
#remove by value med remove("navn")
navne.append("Rasmus")
print(navne)
navne.remove("Rasmus")
print(navne)

#sortering af lister - med list.sort() (ændrer listen) og sorted(list) (ændrer ikke listen)
#navne.sort()
print("sorteret liste:  "+str(sorted(navne)))
print(navne)
#længden af en liste med len

#reverse af en liste med list.reverse() - ændrer på listen.
navne.reverse()
print(navne)
#index -1 - bruges til sidste element
#print( navne[-1] )
lengde = len(navne)-1
print(navne[lengde])


#looping through a list
print("######## bil listen herfra##########")
cars = ["Porsche","Hyundai","BMW"]
for bil in cars:
    print(bil)

print("\nslut på løkke")


# numeriske lister - bemærk sidste index kommer IKKE med

sum = 0
for x in range(1, 5):
    sum = sum + x
    print(x)
print("summen er "+str(sum))

# definer en liste med tal


tal = list(range(1, 30))
tal2 = [1, 2, 3, 4, 5]
print(tal)
print(tal2)

#tuppel
min_liste = (1, 2, 3)   # vi bruger () og ikke []
#nedenstående giver en fejl!!
# min_liste[0] = 10


