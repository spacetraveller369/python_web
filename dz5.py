# 1. Создайте дескриптор PositiveValue, который:
# Разрешает устанавливать только положительные числа. 
# Используйте этот дескриптор в классе BankAccount для проверки баланса счета.
# Добавьте возможность создать объект BankAccount с заданным именем владельца и начальными средствами.
# Если попытаться установить отрицательное значение или ноль, выбрасывает ValueError.

class PositiveValue ():

    def __set_name__(self, owner, name):
        # Создаём уникальное имя для хранения значения
        self.private_name = f"_{name}"


    def __get__(self, obj, obj_type=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, new_value):
        if (new_value<0):
            raise ValueError("value cannot be less then zero")
        else:
            setattr(obj, self.private_name, new_value)


class Name:

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, obj, obj_type=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        setattr(obj, self.private_name, value)



class BankAccount():

    balance = PositiveValue()
    name = Name()

    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
    def check_balance (self):
        print(f'{self.name} has balance: {self.balance}')
    
max = BankAccount('Max', 10)
max.check_balance()



# 2. Создайте дескриптор LogDescriptor, который:
# Логирует каждый доступ к атрибуту, включая чтение и запись.

class LogDescriptor:

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"
        self.public_name = name

    def __get__(self, obj, obj_type=None):
        value = getattr(obj, self.private_name, None)
        print(f"[LOG] Чтение: {self.public_name} → {value}")
        return value

    def __set__(self, obj, value):
        print(f"[LOG] Запись: {self.public_name} ← {value}")
        setattr(obj, self.private_name, value)



# 3. Напишите метакласс, который не позволяет создавать классы с атрибутами, начинающимися с подчеркивания. 
# Если класс содержит такие атрибуты, метакласс должен выбрасывать исключение.
# Реализуйте метакласс, который проверяет атрибуты класса на соответствие этому ограничению.
# Напишите несколько классов с атрибутами, начинающимися с подчеркивания, и убедитесь, что будет выброшено исключение.

class NoUnderscoreAttrsMeta(type):

    def __new__(metacls, name, bases, attrs):
        for attr_name in attrs:
            if attr_name.startswith('_') and not attr_name.startswith('__'):
                raise ValueError(
                    f"Ошибка при создании класса '{name}': атрибут '{attr_name}'"
                )
        return super().__new__(metacls, name, bases, attrs)



# 4. Создайте метакласс, который автоматически добавляет в каждый класс метод hello(), который выводит строку "Hello from <имя класса>".
# Реализуйте метакласс, который добавляет метод hello() в каждый класс.
# Напишите несколько классов, использующих этот метакласс, и вызовите метод hello() для каждого класса.

class HelloMeta(type):

    def __new__(metacls, name, bases, attrs):
        def hello(self):
            print(f"Hello from {self.__class__.__name__}")
        attrs['hello'] = hello
        return super().__new__(metacls, name, bases, attrs)
    
class Alpha(metaclass=HelloMeta):

    pass

class Beta(metaclass=HelloMeta):

    def custom(self):
        return "I'm Beta"

class Gamma(metaclass=HelloMeta):

    def hello(self):  # Переопределение
        print("Custom hello from Gamma")

# 5. Напишите метакласс, который не позволяет классам наследовать другие классы, если в имени родительского класса есть подстрока "Forbidden".
# Реализуйте метакласс, который проверяет имя родительского класса и запрещает наследование от классов с подстрокой "Forbidden" в имени.
# Напишите несколько классов с этим метаклассом, и попробуйте создать класс, наследующий от запрещенного класса.


class ForbiddenMeta(type):

    def __new__(metacls, name, bases, attrs):
        for base in bases:
            if "Forbidden" in base.__name__:
                raise TypeError(
                    f"Класс '{name}' не может наследовать от '{base.__name__}'"
                )
        return super().__new__(metacls, name, bases, attrs)
    
class AllowedBase:
    pass

class GoodClass(AllowedBase, metaclass=ForbiddenMeta):
    pass

# 6. Создайте метакласс, который проверяет, что каждый атрибут класса является строкой. Если атрибут не является строкой, выбрасывайте исключение.
# Реализуйте метакласс, который проверяет тип атрибутов класса.
# Напишите класс с атрибутами разных типов (например, строками и числами) и убедитесь, что метакласс выбрасывает исключение, если тип атрибута некорректен.

class StringOnly(type):

    def __new__(mcls, name, bases, attrs):
        for attr_name, value in attrs.items():
            if attr_name.startswith("__") and attr_name.endswith("__"):
                continue
            if not isinstance(value, str):
                raise TypeError(
                    f"Ошибка: Атрибут '{attr_name}' в классе '{name}' должен быть строкой"
                )

        return super().__new__(mcls, name, bases, attrs)


class ValidClass(metaclass=StringOnly):

    pass

# 7. Создайте протокол Shape, который требует реализации метода area() для вычисления площади фигуры. 
# Реализуйте несколько классов, таких как Circle, Rectangle и Triangle, которые будут реализовывать данный протокол. 
# Напишите функцию, которая принимает объекты, реализующие протокол Shape, и выводит их площадь.
# Протокол Shape должен содержать метод area().
# Классы Circle, Rectangle и Triangle должны реализовывать метод area(), соответствующий их геометрической форме.
# Функция print_area() должна принимать объект, реализующий протокол Shape, и выводить площадь.

from typing import Protocol, runtime_checkable
import math

@runtime_checkable

class Shape(Protocol):

    def area(self):
        pass

# Класс Circle

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
# Класс Rectangle

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Класс Triangle

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def Area(shape:Shape):

    print (f'Площадь фигуры: {shape.area()}')

tr = Rectangle(10,20)
Area(tr)

# 8. Создайте протокол Serializable, который требует реализации метода serialize(). 
# Реализуйте два класса: Person и Book, 
# которые будут реализовывать этот метод для преобразования объектов в строковый формат JSON.
# Протокол Serializable должен содержать метод serialize().
# Классы Person и Book должны реализовывать метод serialize(), возвращающий строку в формате JSON.
# Напишите функцию serialize_object(), которая будет принимать объект и вызывать его метод serialize().

import json

class Serializable(Protocol):
    def serialize(self):
        pass


# Класс Person

class Person(Serializable):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def serialize(self):
        return json.dumps({
            "type": "Person",
            "name": self.name,
            "age": self.age
        }, ensure_ascii=False)


# Класс Book

class Book(Serializable):

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def serialize(self):
        return json.dumps({
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "year": self.year
        }, ensure_ascii=False)


def serialize_object(obj: Serializable):
    return obj.serialize()


p = Person("Илона", 31)
b = Book("1984", "Дж.Оруелл", 1984)

print(serialize_object(p))
print(serialize_object(b))