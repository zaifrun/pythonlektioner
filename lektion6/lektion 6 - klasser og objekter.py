""" Denne indeholder eksempel kode fra lektion 6 - klasser og funktioner"""

########Her er vores Dyr klasse
class Dyr():
    def __init__(self, navn = "", alder = 0):
        self.navn = navn
        self.alder = alder

    def printnavn(self):
        print("Mit navn er "+self.navn)

    def tostring(self):
        s = self.navn + " er "+str(self.alder)+" år"
        return s

dyr1 = Dyr("fido",20)
dyr2 = Dyr("Snaky",10)
dyr1.printnavn()
print(dyr1.tostring())
print(dyr2.tostring())


class Hund(Dyr):
    def __init__(self,navn="",alder = 0,vaccineret = True):
        super().__init__(navn, alder)
        self.vaccineret = vaccineret

    def tostring(self):
        if self.vaccineret:
            s = self.navn + " er "+str(self.alder)+" år og er vaccineret (Hund)"
        else:
            s = self.navn + " er "+str(self.alder)+" år og er ikke vaccineret (Hund)"
        return s

class Fugl(Dyr):
    def __init__(self,navn="",alder = 0,kanflyve = True):
        super().__init__(navn, alder)
        self.kanflyve = kanflyve
        self.hastighed = 0

    def flyv(self):
        self.hastighed = 50

    def tostring(self):
        if self.kanflyve:
            s = super().tostring()+" og kan flyve (Fugl)"
        else:
            s = super().tostring()+" og kan ikke flyve (Fugl)"
        return s

struds = Fugl("struds",3,False)
falk = Fugl("falk",2,True)
fido = Hund("Fido",2,True)
print(struds.tostring())
print(falk.tostring())
print(fido.tostring())

#######Udskrive en liste med forskellige slags dyr########
print("###########Dyre liste##################")
liste = [dyr1,dyr2,struds,falk,fido]
for dyr in liste:
    print(dyr.tostring())

print("struds hastighed : "+ str(struds.hastighed))
struds.flyv()
print("struds hastighed : "+str(struds.hastighed))

#nedenunder vil ikke virke.....hvorfor ikke?
#dyr1.flyv
help(object)
#help(str)



