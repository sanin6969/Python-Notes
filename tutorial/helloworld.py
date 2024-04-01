# if 5>2:
#  print('5 is greater')


# TODO  type of commenst
#  """
#  fytvftfvtyfd
#  """
#  #if 6>3:
#   #print('6 is greater')
 
# TODO variable declaring
#  x=5
#  X=20
#  y='sanin'
#  z=str('sundaran')
#  Z=int(1)
#  print(x,y,z,Z)

# TODO  type of
#  print(type(z))


#                                            TODO: STRINGS



# TODO  multiline string
#  a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# TODO  string array
# a='sanin'
# print(a[0])


#TODO  loop of string
# for x in "sanin":
#  print(x)

# TODO length in string
# a='muhammed sanin'
# print(len(a))

# TODO check string / if
# a='my name is muhammed sanin'
# print('sani' in a)
# if 'sania' in  a :
#  print('yes,sani is present')

#TODO   not condition
# if 'bucky' not in a:
    # print('bucky not present in a' )
 
#TODO   string slice
# b='sanin'
# print(b[1:5])

# TODO uppercase and lowercase
# a='saNiN'
# print(a.upper())
# print(a.lower())

# TODO remove space
# a='  bucky  '
# print(a.strip())

# TODO replace string
# a='sanny'
# print(a.replace('a','u'))

# TODO split method
# a='sanin here'
# print(a.split(','))

# TODO string concat
# a='sanin'
# b='here'
# c=a+" "+b
# print(c)

#  TODO Format string
# name='sanin'
# age=26
# amount=20
# price =100
# text='i am {0} and am {1} years old i have {3} of phones and it cost {2}rupees'
# print(text.format(name,age,amount,price))

# TODO escape characters
# a='\'SUKUNA\' is the villain of JJK'
# print(a)

# TODO \n
# A='YUJI ITTADORi \n is the main characetr'
# print(A)

# TODO \t
# b='GOJO\tSATURU'
# print(b)

#                                     TODO: OPERATORS


#       TODO logical operators
# Logical operators are used to combine conditional statements:

# TODO and
# a=5
# print(a>3 and a<10 )

# TODO or
# a=5
# print(a>30 or a<10 )

# TODO or
# a=5
# print(not(a>30 or a<10 ))


#       TODO identity operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

# TODO is
# a=['sanin']
# b=['sanin']
# c=a
# print(a is c)
# print(c is b)
# print(a==b)

# TODO is not
# a=['sanin']
# b=['sanin']
# c=a
# print(a is not c)
# print(c is not b)
# print(a!=b)


#       TODO membership  operators
# Membership operators are used to test if a sequence is presented in an object:

# TODO in
# x='am a banana'
# print( 'am' in x)

# TODO not in
# x='am a potato'   
# print('potto' not in x)

#       TODO Bitwise Operators
# Bitwise operators are used to compare (binary) numbers


#                                   TODO:  Python Conditions and If statements

#       TODO IF
# a=10
# b=20
# if a<b:
#     print('b is greater')
    
#       TODO ELIF 
# a=10
# b=100
# if a<b:
#     print('b is greater')
# elif a==b:
#     print('a and b are equal')

#       TODO else
# a=200
# b=29
# if a<b:
#     print("b is greater")
# else:
#     print('a is greater')

# TODO simple method
# print('b is greater') if a<b else print('a is greater')

# TODO The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

# a=10
# b=20
# if a<b:
#     pass

# TODO  =  and or not is nested if

#                                                TODO: LOOPS

#       TODO while lopps
# i=1
# while i<=6:
#     print(i)
#     i+=1
    
# TODO Break statement
# i=1
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1
 
# TODO continue Statement
# i=1
# while i<6:
#     print(i)
#     if 1==4:
#         continue
#     i+=1

# TODO else statement
# i=1
# while i<6:
#     print(i)
#     i+=1
# else:
#     print('i is no longer less than 6')

#       TODO For Loops 
# aot=['eren','mikasa','armin','levi']
# for x in aot:
    # print(x)

# TODO Break
# aot=['eren','mikasa','armin','levi']
# for a in aot:
#     print(a)
#     if a=='mikasa':
#         break

# TODO Range
# for x in range(10):
#     print(x)

# TODO else in for loop
# for x in range(10):
#     print(x)
# else:
#     print('finished')

# for x in range(6):
#     if x ==7:break
#     print (x)
# else:
#     print('finished')    

# TODO nested for loops
# aot =['eren','mikasa','armin']
# jjk=['yuji','gojo','sukuna']
# for x in aot:
#     for y in jjk:
#         print(x,y)


#                                               TODO: LISTS
# 
# mylist=['apple','banana','cherry']
#       TODO length of lists
# print(len(mylist))
# TODO type
# print(type (mylist))

# TODO list constructor
# lists=list(('apple','banana','mango'))
# print(lists[1])

#       TODO change list item

# list =['eren','mikasa','erwin','armin','sasha','berthold']
# list[0]='gojo'
# list[2:4]=['gojo','sukuna','yoji','megumi']
# print(list)
#       TODO insert item
# lists =['eren','mikasa','erwin','armin','sasha','berthold']
# lists.insert(2,'toji')
# print(lists)

# TODO append item  #item pushed to the last
# lists =['eren','mikasa','erwin','armin','sasha','berthold']
# lists.append('toji')
# print(lists)

# TODO extend list
# lists =['eren','mikasa','erwin']
# lists2=['armin','sasha','berthold']
# lists.extend(lists2)
# print(lists)

# TODO add any literals
# lists =['eren','mikasa','erwin','armin','sasha','berthold']
# name='sanin'
# tuples=('toji','sukuna')
# lists.extend(tuples)
# lists.extend(name)
# print(lists)

#        TODO remove item
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# lists.remove('eren')#removes only th efirst occurance
# print(lists)

# TODO pop #remove specified index   #without index it removes the last one
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# lists.pop(1)
# lists.pop()
# print(lists)

# TODO del  # can remove the whole lists and its memory
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# del lists[0]
# print(lists)
# del lists
# print(lists)  #removes the whole memory

# TODO clear # The list still remains, but it has no content.
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# lists.clear()
# print(lists)

#           TODO loop through the lists
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# for x in lists:
    # print(x)
    
# TODO loop through index
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# for x in range(len(lists)):
#     print(lists[x])

# TODO while loop in lists  
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# i=0
# while i<len(lists):
#     print(lists[i])
#     i+=1

#                   TODO List comprehension     FIXME: List comprehension offers a shorter syntax 
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# [print(x) for x in lists]

# TODO to new list
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# newLists=[]
# for x in lists:
#     if 'a' in x :
#      newLists.append(x) 
# print(newLists)

# TODO simplified method   
# lists =['eren','mikasa','erwin','armin','sasha','berthold']
# newList=[x for x in lists if 'e' in x]
# print(newList)

# TODO stntax newlist = [expression for item in iterable if condition == True]

# TODO add any iterables
# new=[x for x in range(10)]
# print(new)

#  with condition

# new=[x for x in range(10) if x>5]
# print(new)

# TODO expressions
# lists =['eren','mikasa','erwin','armin','sasha','berthold']
# new=[x.upper() for x in lists]
# print(new)
# hello=['hello' for i in lists]
# print(hello)

#       TODO list sort
# lists =['eren','mikasa','erwin','armin','sasha','berthold']
# lists.sort()
# print(lists)

# number=[1,4,7,3,78,5,3]
# number.sort()
# print(number)

# sorting in reverse(descending)
# lists =['eren','mikasa','erwin','armin','sasha','berthold']
# lists.sort(reverse=True)
# print(lists)
# number=[1,4,7,3,78,5,3]
# number.sort(reverse=True)
# print(number)

# TODO copy lists
# lists=[1,8,3,7,5]
# newLists=lists.copy()
# lists.sort()
# newLists2=list(lists)
# print(newLists2)

# TODO list append
# lists=[1,2,3,4,5]
# Lists=['a','b','c']
# for x in Lists:
#     lists.append(x)
# print(lists)

# TODO list extend
# lists=[1,2,3,4,5]
# Lists=['a','b','c','d']
# lists.extend(Lists)
# print(lists)

# TODO count
# lists =['eren','mikasa','erwin','armin','sasha','berthold','eren']
# print(lists.count('eren'))

#                                              TODO: TUPLE
# Tuple items are ordered, unchangeable, and allow duplicate values.
# tuples=('hi','hello','world')
# print(tuples)

# TODO insert item to tuple
# tuples=('toji','sukuna','gojo')
# y=list(tuples)
# y[0]='tanjiro'
# tuples=tuple(y)
# print(tuples)

# using append
# tuples=('toji','sukuna','gojo')
# y=list(tuples)
# y.append('maki')
# tuples=tuple(y)
# print(tuples)

#add another tuple
# tuples=('toji','sukuna','gojo')
# y=('maki',)
# tuples += y
# print(tuples) 

# TODO remove an item from tuple
# tuples=('toji','sukuna','gojo')
# y=list(tuples)
# y.remove('toji')
# tuples=tuple(y)
# print(tuples)

#           TODO unpacking Tuples
# tuples=('toji','eren','tanjiro')
# (jjk,aot,ds)=tuples
# print(jjk)

# TODO Asterick *
# tuples=('toji','eren','tanjiro','nezuko','zenisthu')
# (jjk,aot,*ds)=tuples
# print(jjk)
# print(ds)


# TODO loop in Tuples
# tuples=('toji','eren','tanjiro','nezuko','zenisthu')
# for x in tuples:
#     print(x)
# Loop through index
# tuples=('toji','eren','tanjiro','nezuko','zenisthu')
# for x in range(len(tuples)):
#     print(tuples[x])
    
#  while loops
# tuples=('toji','eren','tanjiro','nezuko','zenisthu')
# x=0
# while x < len(tuples):
#     print(tuples[x])
#     x+=1

# TODO join of tuples
# tuples=('toji','eren','tanjiro')
# tuples2=('inosuke','nezuko','zenisthu')
# print(tuples+tuples2)

# TODO multiples of tuple
# tuples=('toji','eren','tanjiro')
# print(tuples*2)


#                                               TODO: SETS
# sets={'bucky','steve','ironman','wanda'}
# print(sets)

# TODO add item to sets
# sets={'bucky','steve','ironman','wanda'}
# sets.add('thor')
# print(sets)

# TODO update sets
# marel={'bucky','steve','ironman','wanda'}
# dc={'joker','harley','deadshot','superman'}
# marel.update(dc)
# print(marel)

# TODO remove
# marvel={'bucky','steve','ironman','wanda'}
# marvel.remove('buckya')
# print(marvel)

# TODO discard
# marvel={'bucky','steve','ironman','wanda'}
# marvel.discard('bucky')
# print(marvel)

# TODO pop clear  del
# marvel={'bucky','steve','ironman','wanda'}
# x=marvel.pop()
# print(x)
# print(marvel)
# z= marvel.clear()
# # del marvel
# print(z)

# TODO intersection_update() keep only the items that are present in both sets.
# marvel={'bucky','steve','ironman','wanda'}
# marv={'bucky','captain','rdj','witch'}
# marvel.intersection_update(marv)
# print(marvel)

# TODO symmetric_difference_update() keep only the elements that are NOT present in both sets.
# marvel={'bucky','steve','ironman','wanda'}
# marv={'bucky','captain','rdj','witch'}
# marvel.symmetric_difference(marv)
# print(marvel)

#                                       TODO: DICT (Dictionary)

# ditcs={'name':'sanin',
#        'age':20,
#        'place':'nyc'
#        }
# print(ditcs)
# print(ditcs['place'])
# names=dict([('sanin','abcd'),('bucky','fgajh')])

# TODO updating dict
# ditcs={'name':'sanin',
#        'age':20,
#        'place':'nyc'
#        }
# ditcs['name']='bucky'
# ditcs.update({'place':'new york'})
# print(ditcs)

# TODO get method
# anime={'aot':'eren',
#        'jjk':'sukuna',
#        'demonslayer':'tanjiro',
#        'deathnote':'kira'
#        }
# x=anime.get('jjk')
# print(x)

# TODO acces keys
# anime={'aot':'eren',
#        'jjk':'sukuna',
#        'demonslayer':'tanjiro',
#        'deathnote':'kira'
#        }
# x=anime.keys()
# print(x)

# TODO to acces values
# anime={'aot':'eren',
#        'jjk':'sukuna',
#        'demonslayer':'tanjiro',
#        'deathnote':'kira'
#        }
# x=anime.values()
# print(x)

# TODO Items
# anime={'aot':'eren',
#        'jjk':'sukuna',
#        'demonslayer':'tanjiro',
#        'deathnote':'kira'
    #    }
# print(anime.items())

# TODO remove elemnt in dict
# anime={'aot':'eren',
#        'jjk':'sukuna',
#        'demonslayer':'tanjiro',
#        'deathnote':'kira'
#        }
# anime.pop('jjk')
# anime.popitem()
# print(anime)

# TODO clear del del[]

# TODO for loop
# anime={'aot':'eren',
#        'jjk':'sukuna',
#        'demonslayer':'tanjiro',
#        'deathnote':'kira'
#        }
# TODO get keys
# for x in anime:
#     print(x)
    
#TODO  get values
# for y in anime:
#     print(anime[y]) 
    
# for v in anime.values():
    # print(v)   
#TODO get keys an d values 
# for k,v in anime.items():
#     print(k,v)

# TODO copy dictionary
# anime={'aot':'eren',
#        'jjk':'sukuna',
#        'demonslayer':'tanjiro',
#        'deathnote':'kira'
#        }
# movies = anime.copy()
# films=dict(anime)
# # print(movies)
# print(films)

# TODO nested dictionary
# anime_movies={
#     'anime1':{
#         'name':'attack on titan',
#         'actor':'eren yeager'
#     },
#     'anime2':{
#         'name':'jujutsu kaisen',
#         'actor':'ryomen sukuna'
#     },
#     'anime3':{
#         'name':'demon slayer',
#         'actor':'tanjiro'
#     }
# }
# print(anime_movies)
# Acces them by
# print(anime_movies['anime2']['actor'])


#                                       TODO: PYTHON FUNCTION
# def greet():
#     print('hellooo guys')
#     print('goood mooorning')
# greet()    


# def myfunction(name):
#     age=10
#     place='abc'
#     print(f'hi  {name} age is {age} place is {place}')   
# myfunction('sanin')

# TODO Recursion
# def evennums(num):
#     print(num)
#     if num==2:
#         return num
#     else:
#         return evennums(num-2)
# evennums(8)    

# TODO Lambda
# fistName=lambda fn,ln:print(fn+' '+ln)

# fistName('muhammed' ,'sanin')

# TODO Decorators
# def my_decorator(func):
#     def wrapper():
#         print('this is wrapper')
#         func()
#         print('this is func')
#     return wrapper

# @my_decorator
# def say_hello():
#     print('hello guys')        

# say_hello()

#  TODO Iterators
# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)
# print(next(my_iter))  # Output: 1
# print(next(my_iter))  # Output: 2
# print(next(my_iter))  # Output: 2
# print(next(my_iter))  # Output: 2



#                                    TODO: PYTHON MODULES
# Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application
# import module1
# module1.checkposorneg(29)

# TODO impoort only the needed function
# from module1 import checkposorneg
# checkposorneg(19)

# TODO import as another name
# import module1 as mod
# mod.checkposorneg(1)

# TODO from module1 import checkposorneg as check
# check(20)

# TODO Inbuild modules
# import platform
# print(platform.processor())
# print(platform.python_compiler())

# import calendar
# print(calendar.firstweekday())

#                                                   TODO: exception Handling
# while True:
#     try:
#         a=int(input('enter first number'))
#         b=int(input('enter second number'))
#         c=int(a/b)
#         print(c)
#     except:
#         print('enetr valid input only')  
#     else:
#         print(c)
#         break
            
#     finally:
#         print('code is finished')    
    
    
#                                                   TODO: OOOOOOPS
#TODO  example 1
# class empolyees:
#     company_name='abcd technologies'
#     company_locaton='calicut'
#     def __init__(self,id,name,salary):
#         self.emp_id=id
#         self.emp_name=name
#         self.emp_salary=salary
#     def get_details(self):
#           print(self.emp_id,self.emp_name,self.emp_salary)  
        
# obj1=empolyees(101,'sanin',100000)
# obj2=empolyees(102,'bucky',250000)   
# obj1.get_details()     
# obj2.get_details


# TODO example 2
# class Student:
#     school_name='abc hss'
#     def __init__(self,Stu_no,Stu_name,Stu_class):
#         self.student_no=Stu_no
#         self.student_name=Stu_name
#         self.student_class=Stu_class
        
#     def display_details(self):
#         print(f'name:{self.student_name}\t roll number:{self.student_no}\tclass:{self.student_class}\t school:{Student.school_name}')
        
#     def set_marks(self,phy,che,mat,cs):
#         self.physics=phy
#         self.chemistry=che
#         self.maths=mat
#         self.computer_science=cs     
#         print(f'physics:{self.physics}\nchemistry:{self.chemistry}\nmaths:{self.maths}\ncomputer-science:{self.computer_science}')
        
#     def get_average(self):
#         return(self.physics+self.chemistry+self.maths+self.computer_science)/4    
                     
# student1=Student(1,'sanin',10)
# student1.display_details()  
# student1.set_marks(10,15,20,30)    
# print('average marks:',student1.get_average())

# print('-----------------------------------------------')

# srtudent2=Student(2,'bucky',8)
# srtudent2.display_details()
# srtudent2.set_marks(30,56,79,200)
# print('average mark:',srtudent2.get_average())

# class methods FIXME: DOUBTT
# class Student:
#     school_name='abc hss'
#     def __init__(self,Stu_no,Stu_name,Stu_class):
#         self.student_no=Stu_no
#         self.student_name=Stu_name
#         self.student_class=Stu_class
        
#     def display_details(self):
#         print(f'name:{self.student_name}\t roll number:{self.student_no}\tclass:{self.student_class}\t school:{Student.school_name}')
        
    
#     def get_school(self):
#         print('school Name :',self.school_name)    
           
# Student.get_school()        

# TODO Class methods and static methods
# class Student:
#     school_name='abc hss'
#     def __init__(self,Stu_no,Stu_name,Stu_class):
#         self.student_no=Stu_no
#         self.student_name=Stu_name
#         self.student_class=Stu_class
        
#     def display_details(self):
#         print(f'name:{self.student_name}\t roll number:{self.student_no}\tclass:{self.student_class}\t school:{Student.school_name}')
        
#     # class methods    
#     @classmethod 
#     def get_school(cls):
#         print('school Name :',cls.school_name)  
        
#     # static methods   
#     @staticmethod
#     def about_us():
#         print('this school is the best among others')    
        
# Student.get_school() 
# Student.about_us()       

# TODO sequence item as instance variable
# class Student:
#     def __init__(self,id,name,marks:dict):
#         self.Student_id=id-
#         self.student_name=name
#         self.student_marks=marks
        
#     def display_details(self):
#         print(f'NAME:{self.student_name}\t ROLL NO :{self.Student_id}')
            
#     def mark_percent(self):
#         total=0
#         for i in self.student_marks.values():
#             total+=i
#             per=(total/400)*100
#         print('percentage of mark is :',per)        
# s1=Student(1,'sanin',{'phy':67,'che':78,'mat':90})           
# s1.display_details()
# s1.mark_percent() 

# TODO  object of a class is an another object of a class
# class Company:
#     def __init__(self,Name,Dir,Loc,Gm):
#         self.Company_name=Name
#         self.Company_Director=Dir
#         self.Company_location=Loc
#         self.company_GManager=Gm
        
# class Employee:
#     def __init__(self,emp_name,emp_id,emp_age,emp_company=Company):
#         self.employee_name=emp_name
#         self.employe_id=emp_id
#         self.employee_age=emp_age
#         self.employee_company=emp_company
        
#     def Print_details(self):
#         print(f'Employ Nmae:{self.employee_name}'
#             f'\nEmploye id:{self.employe_id}'
#             f'\nEmploye age:{self.employee_age}'
#             f'\nEmploye Company:{self.employee_company.Company_name}'
#             f'\nDirector Name:{self.employee_company.Company_Director}')    
        
# c1=Company('Bridgeon','anas','calicut','udaif')
# e1=Employee('sanin',1001,20,c1)        
# e1.Print_details()

# TODO map 
# def square_root (num):
#     return int(num**(1/2))

# square_root(16)
# lists=[9,16,25,49,100,121,1]

# print(list(map(square_root,lists)))

# print(list(map(lambda x:int(x**(1/2)),lists)))

# TODO filter
# lists=[9,16,25,49,100,121,1]
# print(list(map(lambda x : x%2==1,lists)))

# TODO reduce
# lists=[1,2,3,4,5,6,7,8,9]
# from functools import reduce
# print(reduce(lambda x,y:x+y,lists))

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side ** 2

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius ** 2
# square = Square(5)
# print(square.area())

# circle = Circle(3)
# print(circle.area())

# TODO acces specifiers
# class student:
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self._age=age
#         self.__rollno=rollno
#     def display(self):
#         print(self.name)
# # def showData():
# #     print(s1._age)        
# # showData()
# student('sanin',20,101)
# # print(dir(s1))
# # s1.display()
# print(student.display())


# class A:
#     def __init__(self,name,age):
#         self.__name=name
#         self.age=age
        
#     def display(self):
#         print(self.__name)
             
# s1=A('sanin',20)
# print(s1.age)
# s1.display()
# # print(s1.__name)
# print(s1._A__name)
