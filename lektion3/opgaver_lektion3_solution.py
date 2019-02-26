""" Denne python fil er en eksempel løsning på opgaverne fra
lektion 3. Der kan være andre varianter at løse opgaverne på, men dette
er mit bud"""


#opgave 1
print("#######Opgave 1 løsning##########")
navn="martin"
if navn=="martin":
    print("sandt")
if navn!="benny":
    print("navnet er ikke benny")
minliste = ["martin","charlotte"]
if "martin" in minliste:
    print("Min liste indeholder 'martin'")
if "benny" in minliste:
    print("Min liste indeholder benny")
else:
    print("min liste indeholder ikke benny")

alder = 15
if alder>=13 and alder<=19:
    print("Du er en teengaer")
else:
    print("Du er ikke en teenager")
if alder<12 or alder>67:
    print("du er barn eller pensionist - rabat! ")
else:
    print("Du kan ikke få rabat!")
#opgave 2
print("#######Opgave 2 løsning##########")

navne = { "martin" : "knudsen" ,
          "benny" : "andersen",
          "jens" : "jensen",
          "Dorthe" : "Pilgaard",
          "Peter" : "Jul"}

print(navne)
if "martin" in navne.keys():
    print("Martin findes i ordbogen")
else:
    print("Martin findes ikke i ordbogen")

#opgave 3
print("#######Opgave 3 løsning##########")
print("###både fornavn og efternavn")

for fornavn, efternavn in navne.items():
    print(fornavn + " "+ efternavn)

print("###kun fornavne")
for fornavn in navne.keys():
    print(fornavn)

print("###kun efternavne")
for efternavn in navne.values():
    print(efternavn)
print("antal navne i listen er : "+str(len(navne)))

#opgave 4
print("#######Opgave 4 løsning##########")

navne["kurt"] = "hansen"
print("kurt tilføjet:")
print(navne)
print("peter fjernet")
del navne["Peter"]
print(navne)

#opgave 5
print("#######Opgave 5 løsning##########")

danmark = { "navn" :  "Danmark",
            "byer" : ["København","Aarhus","Odense"]}
tyskland = {"navn" : "Tyskland",
            "byer" : ["Berlin","Hamburg","Munchen"]}

lande_liste = []
lande_liste.append(danmark)
lande_liste.append(tyskland)

for land in lande_liste:
    print("Land: "+land["navn"])
    print("Største byer: ")
    for by in land["byer"]:
        print(by)

#########Opgave 6 - søgning ################
print("########## Opgave 6 løsning ##############")
lande = ["Danmark", "Tyskland", "Sverige", ""]
search = "mark"
found = False
matched = ""
if "mark" in "Danmark":
    print("mark er med i Danmark")
for land in lande:
    if search in land:
        matched = land
        found = True
if found:
    print("Fandt "+search+" i "+matched)
else:
    print("Fandt ikke "+search)

#ændring