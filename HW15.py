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

    def area(self): # poshuk area func
        return self.radius* self.radius * 3.14

    def perimeter(self): # poshuk perimtr func
        return 2 * self.radius * 3.14

probnyk1 = Circle(36)
print(f"Area = {probnyk1.area()}. Perimeter {probnyk1.perimeter()}")


# Practice Task 2 
class Student:
    pass

class Marks:
    pass

uchen1 = Student()
note1 = Marks()

# Перевіряємо чи належать обєкти до вказаних класів та також чи класи є підкласами об'єкта
print(f"Is uchen1 an instance of Student class: {isinstance(uchen1, Student)}")
print(f"Is note1 an instance of Marks class: {isinstance(note1, Marks)}")
print(f"Is Student a subclass of object: {issubclass(Student, object)}")
print(f"Is Marks a subclass of object: {issubclass(Marks, object)}")


# Practice Task 3 ?????????


class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'

class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest(self):
        self.deposit(self.interest)
        print(f"Account {self.get_account_number()} has {self.get_balance()} money")


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft):
        super().__init__(balance, account_number)
        self.overdraft = overdraft

    def send_letter(self):
        if self.overdraft > self.get_balance():
            print(f"Account {self.get_account_number()} is in debt")
