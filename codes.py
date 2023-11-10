import math
# Shahin Zamani


class Eu:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def calculate_d(self):
        x1, y1 = self.p1
        x2, y2 = self.p2
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d


# input :
a = (5, 4)
b = (2, 2)
distance_calculator = Eu(a, b)
distance = distance_calculator.calculate_d()
print(f"The Euclidean Distance Between {a} and {b} is: {distance}")

# ***********************************************************


class Person:
    def __init__(self, name):
        self.Name = name
        self.__dict__["age"] = 25


p1 = Person("Shahin")
print(f"The Name Is: {p1.Name}")
print(f"The Age  IS: {p1.age}")

# *************************************8


def decorator(func):
    def w(text):
        lower_letter = text.lower()
        return func(lower_letter)
    return w


@decorator
def p_string(text):
    print(text)


string = 'Hi, My Name Is Shahin'
print(string)
p_string(string)

# ************************************************8


class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def __str__(self):
        return f"ISBN: {self.isbn}\Title: {self.title}\Author: {self.author}\Publisher: {self.publisher}\Pages: {self.pages}\Price: {self.price}\Copies: {self.copies}"

    def stock_in(self):
        if self.copies > 0:
            return True
        else:
            return False

    def sell(self):
        if self.copies > 1:
            self.copies -= 1
        else:
            print("Stock of this book is out.")

    @staticmethod
    def display_books(book_list):
        for book in book_list:
            print(book)
            print()

    @staticmethod
    def by_author(book_list, author_name):
        for book in book_list:
            if book.author.lower() == author_name.lower():
                print(book)
                print()


book1 = Book('957-4-36-547417-1', 'Learn Authomata',
             'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Algebra', 'Reza', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'Ali', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Reza', 'XYZ', 400, 200, 6)

book_list = [book1, book2, book3, book4]


print(book1)
print(book2)
print(book3)
print(book4)
print(book1.stock_in())  # True
print(book2.stock_in())  # True
print(book3.stock_in())  # True
print(book4.stock_in())  # True

book1.sell()
book2.sell()
book3.sell()
book4.sell()

print(book1.copies)
print(book2.copies)
print(book3.copies)
print(book4.copies)

Book.display_books(book_list)

Book.by_author(book_list, "Reza")

# ******************************************************


class fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        self.reduce()
        if self.dr < 0:
            self.nr = self.nr*-1
            self.dr = self.dr*-1

    def __str__(self):
        return (f"{self.nr}/{self.dr}")

    def __mul__(self, other):
        new_nr = self.nr*other.nr
        new_dr = self.dr*other.dr
        return fraction(new_nr, new_dr)

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s

    def reduce(self):
        common_factor = fraction.hcf(self.nr, self.dr)
        self.nr //= common_factor
        self.dr //= common_factor


ob0 = fraction(5, 10)
ob1 = fraction(-4, -6)
ob2 = fraction(2, -2)
ob3 = fraction(-4, 12)
print(ob1)
print(ob2)
print(ob3)
print(ob1*ob2)

# **************************************************************


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius is negative.")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    def area(self):
        return 3.14 * self._radius ** 2


c = Circle(2)
print(f"radius  ={c.radius}")
print(f"diameter={c.diameter}")
print(f"circum  ={c.circumference}")
print(f"area    ={c.area()}")
print()
c.radius = 3
print(f"radius  ={c.radius}")
print(f"diameter={c.diameter}")
print(f"circum  ={c.circumference}")
print(f"area    ={c.area()}")
print()

# ***********************************************************


class SalesPerson:
    total_revenue = 0
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(self.name)

    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)


s1 = SalesPerson('Babak', 25)
s2 = SalesPerson('Alireza', 22)
s3 = SalesPerson('Reza', 27)

s1.make_sale(1000)
s1.make_sale(1200)
s2.make_sale(5000)
s3.make_sale(3000)
s3.make_sale(8000)

s1.show()
s2.show()
s3.show()
print()
print("Total revenue:", SalesPerson.total_revenue)
print("Names:", SalesPerson.names)
print()

# ***************************************************


class Employee:
    domains = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        domain = email.split('@')[1]
        if domain not in Employee.domains:
            Employee.domains.append(domain)

    def display(self):
        print(self.name, self.email)


e1 = Employee('Ali', 'Ali@gmail.com')
e2 = Employee('Reza', 'Reza@yahoo.com')
e3 = Employee('Ahmad', 'Ahmad@outlook.com')
e4 = Employee('Alireza', 'Alireza@yahoo.com')
e5 = Employee('Shahin', 'Shahin@gmail.com')
e6 = Employee('Mikasa', 'Mikasa@yahoo.com')

print("Domains:", Employee.domains)

# *******************************************************


class Shahine:
    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = s

    @property
    def hours(self):
        return self._h

    @property
    def minutes(self):
        return self._m

    @property
    def seconds(self):
        return self._s

    def __eq__(self, other):
        if isinstance(other, Shahine):
            return (
                self._h == other._h
                and self._m == other._m
                and self._s == other._s
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Shahine):
            if self._h < other._h:
                return True
            elif self._h == other._h:
                if self._m < other._m:
                    return True
                elif self._m == other._m:
                    if self._s < other._s:
                        return True
        return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


t1 = Shahine(13, 10, 5)
t2 = Shahine(5, 15, 30)
t3 = Shahine(5, 15, 30)
print(t1 < t2)
print(t1 > t2)
print(t1 == t2)
print(t2 == t3)
print(t1 <= t2)
print(t1 >= t2)

# *********************************************************


class Course:
    def __init__(self, title, instructor, price, lectures, users=None, ratings=None):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = users if users is not None else []
        self.ratings = ratings if ratings is not None else []
        self.avg_rating = self.calculate_avg_rating()

    def __str__(self):
        return f"Course: {self.title}\nInstructor: {self.instructor}\nPrice: {self.price}$"

    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self, rating):
        self.ratings.append(rating)
        self.avg_rating = self.calculate_avg_rating()

    def show_details(self):
        print("Course Details:")
        print(f"Title: {self.title}")
        print(f"Instructor: {self.instructor}")
        print(f"Price: {self.price}$")
        print(f"Lectures: {self.lectures}")
        print(f"Users Enrolled: {self.users}")
        print(f"Ratings: {self.ratings}")
        print(f"Average Rating: {self.avg_rating}")

    def calculate_avg_rating(self):
        if len(self.ratings) > 0:
            return sum(self.ratings) / len(self.ratings)
        else:
            return 0


class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, video_length, users=None, ratings=None):
        super().__init__(title, instructor, price, lectures, users, ratings)
        self.video_length = video_length


class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages, users=None, ratings=None):
        super().__init__(title, instructor, price, lectures, users, ratings)
        self.pages = pages


course1 = Course("Python Basics", "Ali Doe", 49.99, 10)
course1.new_user_enrolled("AliMohammad")
course1.new_user_enrolled("Babak")
course1.received_a_rating(4)
course1.received_a_rating(5)
course1.show_details()
video_course1 = VideoCourse(
    "Web Programming", "Jane Smith", 99.99, 20, "3 hours")
video_course1.new_user_enrolled("Charlie")
video_course1.show_details()
pdf_course1 = PdfCourse("Data Science", "Elliy Aliana", 79.99, 15, 100)
pdf_course1.new_user_enrolled("Jafar")
pdf_course1.show_details()
print()

# ***************************************************


class Mother:
    def cook(self):
        print('Can Bake Cake')


class Father:
    def cook(self):
        print('Can Cook Eggs')


class Daughter(Father, Mother):
    pass


class Son(Mother, Father):
    def cook(self):
        super().cook()
        print('Can cook butter chicken')


d = Daughter()
s = Son()

d.cook()
print()
s.cook()
