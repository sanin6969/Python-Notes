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

# class teacher:
#   cars=0
#   def __init__(self,name,age,children=0):
#         self.name=name
#         self.age=age
#         self.children=children
        
#   def details(self):
#       print(f'name of teacher is {self.name} and the age is {self.age} No.of childern she has is {self.children} and no.of cars is {self.cars}')
      
      
# obj1=teacher('jiya',34)
# obj2=teacher('beee',27)
# obj1.children=20
# obj1.cars=20
# # obj1.__class__.cars=20 # Accessing the class variable through the class its                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            elf
# obj1.details()
# obj2.details()


# TODO: find the area and circumferance of circle using oops
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#         self.area=3.14**self.radius
#         self.Circumferance=2*3.14*self.radius
#     def display(self):
#         print(f'The area is {self.area} and circumferance is {self.Circumferance}')
# c1=Circle(5)
# c1.display()


#                                                    TODO: INHERITANCE
# class Human:
#     def __init__(self,heart) -> None:
#         self.eyes=2
#         self.heart=heart
        
#     def work(self):
#         print('i can work')
        
#     def sleep(self):
#         print('i need to sleep')
        
# class Male(Human):
#     def __init__(self,name,heart):
#         self.name=name
#         super().__init__(heart)
    
#     def work(self):
#      print('i can code tooo')#method over riding
     
#     def display(self):
#         self.work()
#         super().work()
        
#         print(f'male have {self.eyes} number of eyes')
#         print(f'nam eof the male is {self.name}')
#         print(f'number of heart {self.heart}')
        
# male1=Male('bucky',1)
# male1.display()

# TODO: multiple inheritance
# class Human:
#     def __init__(self,age) -> None:
#         self.num_of_eye=2
#         self.age=age
        
#     def work(self):
#         print('i can work')
        
# class male:
#     def __init__(self,name):
#         self.name=name
        
#     def work(self):
#         print('i can code')
        
# class boy(Human,male):
#     def __init__(self,hobby,name,age):
#         self.hobby=hobby
#         male.__init__(self,name)
#         Human.__init__(self,age)
        
#     def display(self):
#         male.work(boy1)
#         print(f'name is {self.name} and has {self.num_of_eye} eyes and age is {self.age} hobby is watching {self.hobby}')
    
# boy1=boy('anime','sanin',20)
# boy1.display()

# TODO: multilevel inheritance
# class Human:
#     def __init__(self,name):
#         self.name=name
#     def work(self):
#         print('i can work')
        
# class Male(Human):
#     def __init__(self,age):
#         self.age=age
#     def sleep(self):
#         print('i can sleep')
#     def work(self):
#         print('i can learn')
    
# class boy(Male):
#     def __init__(self,name, age):
#         Human.__init__(self,name)
#         Male.__init__(self,age)
        
#     def work(self):
#         Human.work(self)
#         super().work()
#         print('i can code')
        
#     def display(self):
#         print(f'the name is {self.name} and age is {self.age} ')
        
# sanin=boy('bucky',20)
# sanin.display()

#                                                       TODO:   ABSTRACTON
# from abc import ABC,abstractclassmethod
# class Vehicle(ABC):
    
#     def __init__(self,n):
#         self.tyres=n
        
#     @abstractclassmethod
#     def start(self):
#         pass    
    
#     def display(self):
#         print('hello from vehicle class')   
        
# class scooter(Vehicle):
#     def __init__(self, n):
#         super().__init__(n)
#     def Print(self):
#         print(f'no of tyres in scooter is {self.tyres}') 
#     def start(self):
#         print('scooter is starting')
# s=scooter(2)
# s.Print()

#                                                      TODO: access specifiers

# class Student:
#     def __init__(self,name,age,number):
#         self.name=name
#         self._age=age
#         self.__number=number
        
#     def get_number(self):
#         return self.__number
    
#     def set_number(self,num):
#         self.__number=num
    
    
#     def Display(self):
#         print(f'name= {self.name} \nage= {self._age} \nnumber= {self.__number}')
        
# class school(Student):
#     def Display(self):
#         print(f'name= {self.name} \nage= {self._age} \nnumber={self.__number}')
        
# s1=Student('sanin',20,12345678)
# # s1.Display()
# # print(s1.__number)
# s2=school('sanin',20,1234345678909876543456787654)
# # s2.Display()
# # print(s2.__number)

# # TODO Name mangling
# a=s1._Student__number
# # print(a)
# s1._Student__number=1209876546754732
# # s1.Display()

# # TODO get and set
# s1.set_number(29)
# print(s1.get_number())

# method over riding
# class A:
#     def display(self):
#         print('hello am A')
# class B(A):
#     def display(self):
#         print('hello am B')
#         A.display(self)
#         super().display()
        
# a1=B()
# a1.display()

# method overloading
# class Calculator:
#     def Add(a,b,c=0):
#         return a+b+c
    
# num1=Calculator
# print(num1.Add(12,1))