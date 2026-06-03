#library is imported
# import time
# t=time.strftime('%H:%M:%S')
# #time is formatted as HH:MM:SS
# hour=int(time.strftime('%H'))
# #the time is given avariable
# if (hour>=0 and hour<=12):
#     print("Good Morning",hour)
# elif (hour>12 and hour<=17):
#     print("Good Afternoon",hour)
# elif (hour>17 and hour<0):
#     print("Good Night",hour) 
# letter="hey my name is {} and i am from {}"
# #fstring is used to format the string
# country="india"
# name="sachin"
# print(letter.format(name, country))
# country="india"
# name="sachin"
# print(f"hey my name {name} and i am from {country}")
# print(f"{2*30}")


# docstrings: it is str literals that appear right after the definition of a function, class or module
# def square(n):
#     '''takes in a num n, returns the square of n'''
#     return n*n
# print(square(5))
# print(square.__doc__)
# import this
# def fact(num):
#     '''finding the factorial'''
#     if (num==1 or num==0):
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact.__doc__)
# print(fact(12))
#fibonacci series
# def fibonacci_series(n):
#     a,b=0,1
#     if n<=0:
#         print("plz enter the positive integer.")
#     elif n==1:
#         print(a)
#     else:
#         print("FIBONACCI SERIES:")
#         for _ in range(n):
#             print(a,end=" ")
#             next_term=a+b
#             a,b=b,next_term
# fibonacci_series(12)
# sets:
# s={1,2,3,4}
# s2={4,2,3}
# s3=s.union(s2)
# print(s3)
# s.update(s2)
# print(s)
# s4=s.intersection(s2)
# print(s4)
# s5=s.symmetric_difference_update(s2)
# print(s5)
# s6=s.difference(s2)
# print(s6)
#isdisjoint: checks whether the two sets have relation(intersection)
# print(s.isdisjoint(s2))
#issuperset:checks if all items are present in super set
# print(s.issuperset(s2))
# dic={
#     "harr":21,
#     "abhi":22
#     }
# print(dic)
# for key in dic.keys():
#     print(dic[key])
# print(dic.items())
# for key, values in dic.items():
#     print(f"the {key} value is {values}")
# ep={222:63,224:56}
# ep1={225:69,226:99}
# ep.update(ep1)
# print(ep)
# ep1.clear()
# ep1.popitem()
# del ep1[226]
# using else with for loop
# for i in range(5):
#     print(i)
#     if i == 4:
#         break
# else:
    # print("no i")
# Exception Handling
# a=input("enter the no:")
# print(f"multiplication of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except :
#     print(f"error in {a}")
# print("out of the loop")
# print("the end")
#finally (block of code which is going to execute in any situation)
# def func():
#     try:
#         l=[1,2,3,4,5]
#         i=int(input("enter the index: " ))
#         print(l[i])
#         return 1
#     except:
#         print("some error has occured")
#         return 0
#     finally:
#         print(" i am always excuted")
# x=func()
# print(x)
# custom errors
# a=int(input("enter value between 5 and 9: "))
# if a<5 or a>9:
#     raise ValueError(" val should be b/w 5 & 9")
# else:
    # print("val lies b/w 5 & 9")
# Enumerate function
# marks=[12,52,65,88,14,86,91]
# for index, v in enumerate(marks):
#     print(index,v)
# import time
# print(dir(time))
# x=10 '''it is an global variable'''
# def my_local_var():
#     global x '''global keyword is used to acess a var globally'''
#     x=4 '''here x becomes a global var'''
#     y=5 ''' y is an local var can not be used outside of the functions'''
#     print(y)
# my_local_var()
# print(x)
# f=open('mean.py','r')
# text=f.read()
# print(text)
# f.close
# f=open('Resume.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)
# with open('resume.txt','r') as f:
#     f.seek(10)
#     data=f.read(5)
#     print(data)
# LAMBDA
# double=lambda x: x * 2
# print(double(3))
# map
# def cube(x):
#     return x**3
# num=[1,4,5,6,7]
# nl=list(map(cube,num))
# print(nl)
# # filter
# def new_filter(a):
#     return a>2
# newl=list(filter(new_filter,num))
# print(newl)
# # reduce
# from functools import reduce
# def add(x,y):
#     return x+y
# nnl=reduce(add,num)
# print(nnl)

# class person:
#     name="abhi"
#     age=21
#     def info(self):
#         print(f"{self.name} is an {self.age} years old")
# a=person()
# a.name,a.age="de",21
# print(a.name,a.age)
# a.info()

# class person:
#     def __init__(self,n,o):
#         print("Hey i am a person",n)
#         self.name=n
#         self.occ=o
#     def info(self):
#         print(f" i am {self.name} and i do {self.occ}")
# a=person("abhi","wed")
# b=person("de","fr")
# a.info()
# b.info()
# decorater

# Inheritance
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
    
#     def ShowDetails(self):
#         print(f"the name of employee: {self.id} is {self.name}")

# class programmer(Employee):
#     def showlanguage(self):
#         print("the default language is python")
# e=Employee("rohan das",420)
# e.ShowDetails()
# e2=programmer("abhi",421)
# e2.ShowDetails()
# e2.showlanguage()

# class employee:
#     def __init__(self):
#         self.__name="abhi" #by using "__" the var will be private
# a=employee()
# print(a._employee__name) #by using class and "__" we can access the var
# class math:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(math.add(6,3))

# class employee:
#     company="apple"
#     def show(self):
#         print(f"The Name is {self.name} and company is {self.company}")
#     @classmethod
#     def changecompany(cls,newcompany):
#         cls.company=newcompany

# e1=employee()
# e1.name="harry"
# e1.show()
# e1.changecompany("Tesla")
# e1.show()

# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def fromstr(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])
    
# e1=employee("Abhi",12000)
# print(e1.name)
# print(e1.salary)
# string="john-20000"
# e2=employee.fromstr(string)
# print(e2.name)
# print(e2.salary)
# print(e1.__dict__)
# print(help(employee))

# class parent():
#     def parent_method(self):
#         print("This is an parent")
# class child(parent):
#     def chlid_method(self):
#         print("This is an child")
#         super().parent_method() #super keyword is used to use the parent class in child class
# child_obj=child()
# child_obj.chlid_method()

# class shape():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x * self.y
# rec=shape(3,5)
# print(rec.area())

# class Cricle(shape):
#     def __init__(self, radius):
#         self.radius=radius
#         super().__init__(radius,radius)
#     def area(self):
#         return 3.14*super().area()
# c=Cricle(6)
# print(c.area())

# class Animal:
#     def __init__(self,name,spices):
#         self.name=name
#         self.spices=spices
#     def make_sound(self):
#         print("sound made by the animal")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,spices="Dog")
#         self.breed=breed
#     def make_sound(self):
#         print("Bark's!!")
# d=Dog("John","GERMAN SHEPERD")
# d.make_sound()
# a=Animal("john","Dog")
# a.make_sound()

# class employee:
#     def __init__(self,name):
#         self.name=name
# class dancer:
#     def __init(self,dance):
#         self.dance=dance
# class danceremployee(employee,dancer):
#     def __init__(self, dance,name):
#         self.dance=dance
#         self.name=name
# o=danceremployee("kathak","loosu")
# print(o.name,o.dance)
# print(danceremployee.mro())

# class Animals:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#     def show_details(self):
#         print(f"name:{self.name}")
#         print(f"species:{self.species}")

# class Dog(Animals):
#     def __init__(self,name,breed):
#         Animals.__init__(self,name,species="Dog")
#         self.breed=breed
#     def show_details(self):
#         Animals.show_details(self)
#         print(f"breed:{self.breed}")

# class Glodenretiver(Dog):
#     def __init__(self, name, colour):
#         Dog.__init__(self,name,breed="Gloden Retriver")
#         self.colour=colour
#     def show_details(self):
#        Dog.show_details(self)
#        print(f"colour:{self.colour}") 

# o=Glodenretiver("Tommy","Glod")
# o.show_details()
# print(Glodenretiver.mro())

# import shutil
# shutil.copy("sql.py","sql2.py")

# import requests
# response=requests.get("https://www.google.com")
# print(response.text)

# def my_generator():
#     for i in range(5):
#         yield i
# gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# import functools
# import time

# @functools.lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*5
# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print(functools._CacheInfo)