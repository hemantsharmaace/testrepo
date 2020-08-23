# class decorator_class(object):
#       def __init__(self,original_function):
#           self.original_function =  original_function
#
#       def __call__(self,*args,**kwargs):
#          print("call is executed {}".format(self.original_function.__name__))
#          return self.original_function(*args,**kwargs)
#
#
# @decorator_class
# def display():
#     print("display is executesd")
#
#
# display()
#
#
# import math
#
# class Pizza:
#     def __init__(self,radius,ingredients):
#         self.radius = radius
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return (f'Pizza({self.radius!r}, '
#                 f'{self.ingredients!r})')
#
#     def area(self):
#         return self.circle_area(self.radius)
#
#     @static_method
#     def circle_area(r):
#         return r ** 2 * math.pi


# hrs = input("Enter Hours:")
# rateperhours = input("Rate per hours: ")
# h = float(hrs)
# rph = float(rateperhours)
#
# if(hrs>40):
#     extrahours = h-40
#     #calculate hourly rate
#     hourlyrateforextrahours = float(1.5)*rph
#     calculatepayforextrahours = extrahours * hourlyrateforextrahours
#     payfor40hours = float(40)*rph
#     grosspay = float(calculatepayforextrahours)+float(payfor40hours)
#     print(grosspay)
# else:
#     grosspay = rph*h
#     print(grosspay)
#

# #score = input("enter score:")
# score = 0.85
#
# scoreuser = float(score)
#
# if(score>=0.9):
#     print("A")
# elif(score>=0.8):
#     print("B")
# elif(score>=0.7):
#     print("C")
# elif(score>=0.6):
#     print("D")
# else:
#     print("Grade out of range.")
#     exit()



n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')
