# 1. Создайте базовый класс Engine, который будет отвечать за управление двигателем
#  Базовый класс Engine 

""" 
class Engine:

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


# Базовый класс Vehicle

class Vehicle:

    def __init__(self, max_speed,**kwargs):
        self.__max_speed = max_speed
        super().__init__(**kwargs)


    @property
    def max_speed(self):
        return self.__max_speed

    def drive(self):
        print(f"Driving at maximum speed of {self.max_speed}")


# Класс Car, наследующий Engine и Vehicle

class Car(Engine, Vehicle):

    def __init__(self, model, max_speed, **kwargs):
    
        # Vehicle.__init__(self, max_speed) нельзя, т.к. производные классы будут использовать несколько раз один и тот же конструктор
        # super().__init__(max_speed=max_speed) нельзя, передадутся в конструктор к Engine, который не ждет такого параметра
        self.model = model
        super().__init__(max_speed=max_speed, **kwargs) #чтобы передать дальше по цепочке аргументы **kwargs



    def drive(self):
    
        print(f"Car {self.model} is driving at {self.max_speed}")


# Класс Boat, наследующий Engine и Vehicle

class Boat(Engine, Vehicle):

    def __init__(self, boat_type, max_speed, **kwargs):
        self.type = boat_type
        super().__init__(max_speed=max_speed, **kwargs)


    def drive(self):
    
        print(f"Boat of type {self.type} is sailing at {self.max_speed}")


# Класс AmphibiousVehicle, наследующий Car и Boat

class AmphibiousVehicle(Car, Boat):

    def __init__(self, model, boat_type, max_speed, is_on_land, **kwargs):
        self.is_on_land = is_on_land
        super().__init__(model=model, boat_type=boat_type, max_speed=max_speed, **kwargs)


    def drive(self):
    
        if self.is_on_land:
            print(f"Car {self.model} is driving at {self.max_speed}")
        else:
            print(f"Boat of type {self.type} is sailing at {self.max_speed}") """

#2. Создайте класс Library, который будет представлять библиотеку. Библиотека должна содержать список книг. Для работы с объектами этого класса реализуйте перегрузку операторов.
#Для книги тоже создаём класс, перегрузить строковое представление(str). Для книги реализовать операторы сравнения по количеству страниц
#Реализовать property для полей Книги.

""" class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Свойства (property)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    # Строковое представление
    def __str__(self):
        return f"«{self.title}» — {self.author} ({self.pages} стр.)"

    # Операторы сравнения по кол-ву страниц
    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    # Оператор +=
    def __iadd__(self, book):
        self.add_book(book)
        return self

    # Оператор -=
    def __isub__(self, book):
        self.remove_book(book)
        return self

    # Проверка наличия книги
    def __contains__(self, book):
        return book in self.books

    # Количество книг
    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Библиотека «{self.name}» содержит {len(self)} книг(и)." """

# 3. Напишите класс-декоратор, который кеширует результаты методов класса, используя аргументы метода в качестве ключа для кеша. Если метод вызывается с теми же аргументами, возвращайте уже вычисленный результат из кеша. 
# Если нет — вычисляйте и сохраняйте результат в кеш.

""" class CacheDecorator:

    def __init__(self, cls):
        self.cls = cls
        self._cache = {}

    def __call__(self, *args, **kwargs):
        obj = self.cls(*args, **kwargs)

        original_method = obj.calculate

        def wrapper(*m_args, **m_kwargs):
            key = (m_args, tuple(sorted(m_kwargs.items())))
            if key not in self._cache:
                self._cache[key] = original_method(*m_args, **m_kwargs)
            return self._cache[key]

        obj.calculate = wrapper
        return obj """

