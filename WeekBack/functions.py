# TODO arbotory positional arguments
# def Add(*numbers):
#     c=0
#     for i in numbers:
#         c+=i
#     print(c)
# Add(1,2,3)

# TODO arbotory keyword arguments
def person(**info):
    print(f'the name is :{info['name']}')
    print(f'the age is :{info['age']}')
    print(f'the place is :{info['place']}')
person(name='sanin',age=20,place='clt')