#This lesson is from "Learning Python" Book
#SUPER class/ Parent class

from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __str__(self):
    #     return f'[Name: {self.name} => Pay:{self.pay}]'

#Subclass 
class Manager(Person):
    def give_raise(self, percent, bonus=0.1):
        #This is the good way of doing it, there is also a bad way see Page#654
        #2 ways of calling class methods:
        #1) instance.method(args)   2)class.method(instance, args...)
        Person.give_raise(self, percent + bonus)


#Run below statments only when running directly from this file
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=20000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.2)
    print(sue.pay)
    print(sue)
    print('\n')

    tom = Manager('Tom Jones', 'mgr', 5000)
    tom.give_raise(0.10)
    print(tom.last_name())
    print(tom)

    print('\n --All three together-- ')
    for item in (bob, sue, tom):
        item.give_raise(0.1)
        print(item)









    


