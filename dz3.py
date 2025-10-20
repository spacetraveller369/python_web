class Book():
    def __init__(self, name, author, pages, id):
        self.__name:str = name
        self.__author:str = author
        self.__pages:int = pages
        self.__ID:int = id

    def get_information(self):
        return f'Name: {self.__name}, Author: {self.__author}, Pages: {self.__pages}, ID: {self.__ID}'
    
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID (self, value):
        self.__ID = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name (self, value):
        self.__name = value
    
class Library():
    def __init__(self):
        self.__books:list = []

    @property
    def books (self):
        return self.__books
    
    @books.setter
    def books (self, value):
        self.__books = value    



    def add_book (self, book:Book):
        self.__books.append(book)
    
    def delete_book_by_ID(self, id: int):
        original_len = len(self.books)
        self.books = [book for book in self.books if book.ID != id]
        if len(self.books) == original_len:
            print(f"Книга с ID {id} не найдена.")


    def show_info_by_name(self, name:str):
        # filtered = list(filter(lambda x: x.name == name, self.books))
        # if filtered:
        #     book = filtered[0]
        #     return book.get_information()
        # else:
        #     return f"Книга з назвою '{name}' не знайдена."

        book = next((b for b in self.books if b.name == name), None)
        if book:
            return book.get_information()
        else:
            return f"Книга с именем '{name}' не найдена."
        
##########################################################################################

class Dish:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def get_description(self) -> str:
        return f"{self.name} ({self.category}) - {self.price:.2f} грн"    


class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def remove_dish(self, dish_name: str):
        self.dishes = [dish for dish in self.dishes if dish.name != dish_name]

    def get_total(self) -> float:
        return sum(dish.price for dish in self.dishes)
    

class Restaurant:
    def __init__(self):
        self.menu = []

    def add_dish_to_menu(self, dish: Dish):
        self.menu.append(dish)

    def show_menu(self):
        for dish in self.menu:
            print(dish.get_description())
##########################################################################################


class Student():
    def __init__(self, name:str, age:int, grades:list):
        self.__name = name
        self.__age = age
        self.__grades = grades
    
    @property
    def grades(self):
        return self.__grades
    
    @property
    def age(self):
        return self.__age

    @property
    def grades(self):
        return self.__grades


    def avg_grade(self):
        return sum(self.grades)/self.grades.count
    
    def to_dict(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "grades": self.__grades
        }

    @staticmethod
    def from_dict(data: dict):
        return Student(data["name"], data["age"], data["grades"])

import json

class StudentDatabase ():
    def __init__(self, file_path):
        self.__file_path = file_path
    

    def read_students(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # data_list = []
                # for item in data:
                #     data_list.append (Student.from_dict(item))
                # return data_list
                return [Student.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def __save_students(self, students: List[Student]):
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump([s.to_dict() for s in students], f, indent=4, ensure_ascii=False)


    def add_student(self, student: Student):
        students = self.read_students()
        students.append(student)
        self.__save_students(students)

    def find_student(self, name: str):
        # students = self.read_students()
        # for student in students:
        #     if student.name == name:
        #         return student
        # return None
        return next ((student for student in self.read_students() if student.name == name))
