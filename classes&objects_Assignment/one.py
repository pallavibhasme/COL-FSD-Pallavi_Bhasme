# 1. Student Class with Object Creation and Object as Parameter
class Student:
    def __init__(self, name,roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
    def check_pass_fail(self):
        if self.marks >= 40:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has failed.")


s1 = Student('Pallavi', 22, 80)
s2 = Student('jk', 23, 80)

s1.display_details()
s2.check_pass_fail()


# 2. Rectangle Class with Object as Parameter
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

    def check_square(self):
        if self.length == self.breadth:
            print("The rectangle is a square.")
        else:
            print("The rectangle is not a square.")


rect1 = Rectangle(5, 10)

print(f"Area of rect1: {rect1.calculate_area()}")
print(f"Perimeter of rect1: {rect1.calculate_perimeter()}")
rect1.check_square()


# 3.	Create a class Car with attributes brand, model, and year. Add a constructor to initialize 
# these attributes and a method to display car details.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_CarDetails(self):
        print(f'Brand : {self.brand}')
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


car1 = Car("Toyota", "Corolla", 2020)

car1.display_CarDetails()

# 4. BankAccount Class with Object as Parameter

class BankAccount:
    def __init__(self, account_no, balance, account_holder):
        self.account_no = account_no
        self.balance = balance
        self.account_holder = account_holder

    def Deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def Withdraw_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Your Current Account balance is {self.balance}.")
        else:
            print("Insufficient balance amount.")


    def Display_Acc_Details(self):
        print(f"Account Number: {self.account_no}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


p1 = BankAccount(12345, 10000 , 'Pallavi')
p1.Deposit_money(500)
p1.Withdraw_money(500)
p1.Display_Acc_Details()

# 5. Inheritance: Person and Employee Class with Object as Parameter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def display_details(self):
        super().display_details()
        print(f"Salary: {self.salary}")
        print(f"Designation: {self.designation}")

    def annual_salary(self):
        return self.salary * 12

person1 = Person("John", 30)
employee1 = Employee("Alice", 28, 50000, "Engineer")
print(f"Annual Salary: {employee1.annual_salary()}")


# 6. Polymorphism: Shape, Circle, Rectangle, and Triangle Classes

class Shape:
    def area(self):
        print("Area is undefined")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Area of a Circle : {area}")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print(f"Area of a Reactangle : {area}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.heigth = height

    def area(self):
        area = 0.5 * self.base * self.height
        print(f"Area of a triangle : {area}")




circle = Circle(5)
circle.area()
rectangle = Rectangle(4, 6) 
rectangle.area() 
triangle = Triangle(5, 10) 
triangle.area()


# 7.	Create a class Counter with a static variable count to track the number of objects created for the class. Add a static method to display the count/.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @staticmethod
    def display_count():
        print(f"Number of objects created: {Counter.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()  

# 8 Engine class with attributes: horsepower and type
class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def display_engine_details(self):
        print(f"Engine Details Horsepower: {self.horsepower} HP Type: {self.engine_type}")

class Car:
    def __init__(self, brand, model, engine: Engine):
        self.brand = brand
        self.model = model
        self.engine = engine 

    def display_car_details(self):
        print(f"Car Details:  Brand: {self.brand} Model: {self.model}")
        self.engine.display_engine_details()  
engine = Engine(300, "V8")  
car = Car("Ford", "Mustang", engine)  
car.display_car_details()  



























