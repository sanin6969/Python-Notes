# class fruit:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def display(self):
#         print(f'the fruit is {self.name} and the color of the fruit is {self.color}')        
        
# apple=fruit('apple','red')
# kiwi=fruit('kiwi','brown')
# apple.display()        
# kiwi.display()

# class student:
#     def __init__(self):
#         self.name='sanin'
#         self.age=20
#         self.place='vengara'
#     def display(self):
#         print(f'My name is {self.name} and my age is {self.age} and my place is {self.place}')
        
        
# sanin=student()
# sanin.display()

# a=10
# b=19
# class sum:
#     def find_sum(self):
#         global a,b 
#         print(a+b)
# d=sum()
# d.find_sum()

class teacher:
  cars=0
  def __init__(self,name,age,children=0):
        self.name=name
        self.age=age
        self.children=children
        
  def details(self):
      print(f'name of teacher is {self.name} and the age is {self.age} No.of childern she has is {self.children} and no.of cars is {teacher.cars}')
      
      
obj1=teacher('jiya',34)
obj2=teacher('beee',27)
obj1.children=20
obj1.__class__.cars=20 # Accessing the class variable through the class itself
obj1.details()
    
