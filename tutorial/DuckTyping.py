class Animal:
    def perform(self):
        print('animal is performing')
class Human:
    def perform(self):
        print('human is performing')
                
class Circus:
    def play(self,animal:Animal):
         animal.perform()              
         
c=Circus()
c.play(Animal())  
c.play(Human())       