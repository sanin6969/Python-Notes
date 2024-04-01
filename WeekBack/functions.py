# TODO arbotory positional arguments
# def Add(*numbers):
#     c=0
#     for i in numbers:
#         c+=i
#     print(c)
# Add(1,2,3)

# TODO arbotory keyword arguments
# def person(**info):
#     print(f'the name is :{info['name']}')
#     print(f'the age is :{info['age']}')
#     print(f'the place is :{info['place']}')
# person(name='sanin',age=20,place='clt')

# TODO: recursion

# def Even_nums(num):
#     print(num)
#     if num==1:
#         return num 
#     else:
#         Even_nums(num-1)
        
# Even_nums(8)

# TODO anounyms functions
# a=lambda x:print(5*x)
# # a()
# b=lambda x,y:print(x+y)
# # b(1,2)
# c=lambda z,w:print(z,w)
# c('muhd','sanin')

# TODO decorators 
# def areaof_circle(r):
#     return 3.14**r

# def radius100(x):
#     def area(r):
#         if r>100:
#             r=100
#         return x(r)
#     return area
# a=radius100(areaof_circle)
# print(a(102))      
    
# TODO generators
# def gen1():
#     for i in range(10):
#         yield print(i)
# y=gen1()
# next(y)
# next(y)
# next(y)
# for i in y :
#     i

# def gen2():
#     yield 10
#     yield 20
#     yield 30
# x=gen2()
# print(next(x))

# TODO iterators
# nums=[1,2,3,4,5,6,7,8,9]
# i=iter(nums)
# print(i.__next__())
# print(i.__next__())