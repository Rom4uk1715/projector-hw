'''
Practice

1 Write a Python class named Circle constructed by a radius 
and two methods which will compute the area and the perimeter of a circle.

2 Write a Python program to create two empty classes, Student and Marks. 
Now create some instances and check whether they are instances of the said classes or not. 
Also, check whether the said classes are subclasses of the built-in object class or not

3 A Bank

A. Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. 
A SavingsAccount object, in addition to the attributes of an Account object, 
should have an interest attribute and a method which adds interest to the account. 
A CurrentAccount object, in addition to the attributes of an Account object, 
should have an overdraft limit attribute.

B. Now create a Bank class, an object of which contains an array of Account objects. 
Accounts in the array could be instances of the Account class, the SavingsAccount class,
or the CurrentAccount class. 
Create some test accounts (some of each type).

C. Write an update method in the Bank class. 
It iterates through each account, updating it in the following ways: 
Savings accounts get interest added (via the method you already wrote); 
CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).

D. The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.

'''
# Practice Task 1 

class Circle: # Створємо новий клас для пошуку радіусу
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius* self.radius * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

probnyk1 = Circle(36)
print(f"Area = {probnyk1.area()}. Perimeter {probnyk1.perimeter()}")
