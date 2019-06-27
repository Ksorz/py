# 14.3 - Object Life Cycle
class PartyAnimal: # This is the template for making PartyAnimal objects
    x = 0 # Each PartyAnimal object has a bit of data

    def __init__(self):
        print('I am constructed')

    def party(self) : # Each PartyAnimal object has a bit of code (method)
        self.x += 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal() # Construct PartyAnimal object and store in a variable ( same as "an = list()" )
an.party() #              == PartyAnimal.party(an)    Run party() code within it
PartyAnimal.party(an) #   == an.party()               Run party() code within it
an = 42 # I am destructed 2
print('an contains',an) # an contains 42
