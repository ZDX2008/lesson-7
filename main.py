# # Task 3
# NumberSequence3=[11,15,19,23,27,31,35,39,43,47,51]
# NewNumberSequence3=[]

# for pos in range(1,11,2):
# 	NewNumberSequence3.append(NumberSequence3[pos])
# print(NewNumberSequence3)

# # Task 4
# NumberSequence4=[21, 30, 39, 48, 57, 66, 75, 84, 93] 
# NewNumberSequence4=[]

# for pos in range(1,11,1): 
# 	NewNumberSequence4.append(NumberSequence4[pos])
# print(NewNumberSequence4)


# # Task 5

# NumberSequence5=[21,30,39,48,57,66,75,84,93] 
# NewNumberSequence5=[]

# for pos in range(0,9,1): 
# 	NewNumberSequence5.append(NumberSequence5[pos])
# print(NewNumberSequence5) 

# # Task 8
# data="Robert,27"
# name=data[:-3]
# age=data[-2:]
# print("Welcome",name)
# print("Your age is",age)

# # Task 9
# data="Lily,A"
# studentName=data[:-2]
# className=data[-1:]
# print("Name:",studentName)
# print("Class:",className)

# # Task 10
# data="Banana,100"
# fruit=data[:-2]
# quantity=data[:50]
# print("Name:",fruit)
# print("Quantity:",quantity)

# Task 11
# data="Books,2359"
# item=data[:-5]
# quantity=data[-4:]
# print("Item:",item)
# print("Quantity:",quantity)

# Task 12
# data=["Apple 8","Orange 2","Pear 4","Grapes 5"]

# def getName(x):
#   return x[:-2]

# def getAmount(x):
#   return x[-1:]

# fruitname=[]
# fruitamount=[]

# for i in data:
#     fruitname.append(getName(i))
#     fruitamount.append(getAmount(i))

# print(fruitname)
# print(fruitamount)

# Task 13
# data = ['Ben 80','Alex 70','James 55']

# def getName(x):
#     return x[:-2] 

# def getScore(x):
#     return x[-2:]

# name = []
# score = []

# for i in data:
#   name.append(getName(i))
#   score.append(getScore(i))

# print(name)
# print(score)

# Task 14

# data = ['Apple 5','Banana 3','Cherry 8']

# def getName(x):
#     return x[:-2] 

# def getScore(x):
#     return x[-2:]

# name = []
# score = []

# for i in data:
#   name.append(getName(i))
#   score.append(getScore(i))
# t = 0
# for i in score:
#   t += int(i)

# print(name)
# print(t)


# Task 15

# data = ['Apple 20','Banana 30','Cherry 10']

# def getName(x):
#     return x[:-2] 

# def getScore(x):
#     return x[-2:]

# name = []
# score = []

# for i in data:
#   name.append(getName(i))
#   score.append(getScore(i))

# t = 540
# for i in score:
#   t += int(i)

# print(name)
# print(t)

# Task 16a
# size=[3,6,4]
# price=[36,72,56]
# pricepersqcm=[]

# for i in range(3):
#    area = size[i] * size[i]
#    pricepersqcm.append(price[i]/area)
   
# print(pricepersqcm)

# Task 16b
# size=[3,6,4]
# price=[36,72,56]
# quantity = [5,10,2]
# pricepersqcm=[]
# total=0

# for i in range(3):
#   total+=price[i]*quantity[i]
   
   
# print(total)

#Task17
# rawscore=[15,50,100,75,5,150,50]
# Percentagescore=[]


# for i in range(7):
#   total = 0
#   percentage = rawscore

# task 18
def farmer(price,years):
    Total=0
    for farmer in range(1,15,5):
        Total+=500*farmer
    print("he earn",Total)
  
farmer(1000,15)
farmer(950,10)
farmer(1050,5)

#task 19

# print("For Company","Johan will need to pay $","in the month of",)