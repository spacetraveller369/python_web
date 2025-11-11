"""
1. Создайте приложение, которое позволяет вести учет расходов. Данное приложение должно реализовывать паттерн MVC. 
Функционал:
- Возможность добавить новый расход
- Удаление существующего расхода по id
- Запрос списка расходов
- Вывод общей суммы расходов
"""

from datetime import datetime

def get_current_timestamp():
    return int(datetime.timestamp(datetime.now()))

def get_date_now():
    return str(datetime.now())

# ** MODEL **

class Expense:
    __id: int
    category: str
    amount: float
    date: str
    description: str

    def __init__(self, _category, _amount, _description):
        self.__id = get_current_timestamp()
        self.category = _category
        self.amount = float(_amount)
        self.description = _description
        self.date = get_date_now()

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return (f"Expense ID: {self.id}\n"
                f"Category: {self.category}\n"
                f"Amount: {self.amount:.2f}\n"
                f"Description: {self.description}\n"
                f"Date: {self.date}")

class Model:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def get_expense(self, id) -> Expense:
        for e in self.expenses:
            if e.id == id:
                return e
        return None

    def delete_expense(self, id):
        expense = self.get_expense(id)
        if not expense:
            return False
        self.expenses.remove(expense)
        return True

    def get_expenses(self):
        return self.expenses

    def get_total_sum(self):
        return sum(e.amount for e in self.expenses)


# ** VIEW **

class View:
    def show_menu(self):
        print("\n==== Подсчет расходов ====")
        print("1. Показать все расходы")
        print("2. Добавить новый расход")
        print("3. Удалить существующий расход по id")
        print("4. Вывод общей суммы расходов")
        print("5. Выход")
        return int(input("Выберите пункт меню (1-5): "))

    def show_message(self, message: str):
        print(message)

    def create_expense(self):
        category = input("Введите категорию: ")
        amount = input("Введите сумму: ")
        description = input("Введите описание: ")
        return Expense(category, amount, description)

    def delete_expense(self, expenses):
        self.show_expenses(expenses)
        return int(input("Введите ID расхода для удаления: "))

    def show_expenses(self, expenses):
        if not expenses:
            print("Расходы не найдены.")
            return
        for exp in expenses:
            print("-" * 30)
            print(exp)
            print("-" * 30, "\n")


# ** CONTROLLER **

class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def action_add_expense(self):
        expense = self.view.create_expense()
        self.model.add_expense(expense)
        self.view.show_message("Расход добавлен успешно!")

    def action_delete_expense(self):
        if not self.model.get_expenses():
            self.view.show_message("Расходы для удалениея не найден.")
            return
        delete_id = self.view.delete_expense(self.model.get_expenses())
        if self.model.delete_expense(delete_id):
            self.view.show_message("Расход удален успешно!")
        else:
            self.view.show_message("Расход не найден!")

    def action_show_expenses(self):
        self.view.show_expenses(self.model.get_expenses())

    def action_show_total(self):
        total = self.model.get_total_sum()
        self.view.show_message(f"Total expenses: {total:.2f}")


# ** MAIN APP **

app = Controller(Model(), View())

while True:
    result = app.view.show_menu()
    match result:
        case 1:
            app.action_show_expenses()
        case 2:
            app.action_add_expense()
        case 3:
            app.action_delete_expense()
        case 4:
            app.action_show_total()
        case 5:
            print("Exit!")
            break
        case _:
            print("Invalid menu item!")

""" 2. Создайте приложение "Книга рецептов" которое позволяет выполнять следующие операции:
- Добавление рецепта: Пользователь может добавить новый рецепт в книгу, указав название, описание, список ингредиентов и инструкцию по приготовлению.
- Удаление рецепта: Пользователь может удалить рецепт по его идентификатору.
- Редактирование рецепта: Пользователь может редактировать рецепт, изменяя название, описание, ингредиенты и инструкцию.
- Сохранение рецептов: Рецепты сохраняются в JSON-файле, чтобы информация сохранялась между запусками приложения.

Шаблоны:
1) Список всех блюд
2) Шаблон отображающий весь рецепт

При запуске приложения необходимо выгружать все рецепты
ИСПОЛЬЗОВАТЬ MVT

import json
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List

# ** Вспомогательные функции **

def get_current_timestamp():
    return int(datetime.timestamp(datetime.now()))

def load_recipes_from_file(filename="recipes.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            recipes = []
            for item in data:
                recipe = Recipe(item["name"], item["description"], item["ingredients"], item["instructions"])
                recipe._Recipe__id = item["id"]  # восстановление id
                recipes.append(recipe)
            return recipes
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_recipes_to_file(recipes, filename="recipes.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([{
            "id": r.id,
            "name": r.name,
            "description": r.description,
            "ingredients": r.ingredients,
            "instructions": r.instructions
        } for r in recipes], f, ensure_ascii=False, indent=4)


# ** MODEL **

class Recipe:
    __id: int
    name: str
    description: str
    ingredients: list
    instructions: str

    def __init__(self, name, description, ingredients, instructions):
        self.__id = get_current_timestamp()
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions

    @property
    def id(self):
        return self.__id


class RecipeModel:

    def __init__(self):
        self.recipes = load_recipes_from_file()

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)
        save_recipes_to_file(self.recipes)

    def get_recipes(self):
        return self.recipes

    def delete_recipe(self, id):
        for r in self.recipes:
            if r.id == id:
                self.recipes.remove(r)
                save_recipes_to_file(self.recipes)
                return True
        return False

    def update_recipe(self, id, new_recipe: Recipe):
        for index, recipe in enumerate(self.recipes):
            if recipe.id == id:
                new_recipe._Recipe__id = id  # сохранить старый ID
                self.recipes[index] = new_recipe
                save_recipes_to_file(self.recipes)
                return True
        return False


# ** TEMPLATE **

class RecipeTemplate(ABC):

    @abstractmethod
    def render(self, recipes: List[Recipe]):
        pass


class RecipeListTemplate(RecipeTemplate):

    """Шаблон вывода списка рецептов"""
    def render(self, recipes: List[Recipe]):
        if len(recipes) == 0:
            print("Книга рецептов пуста.")
        else:
            print("-" * 40)
            for index, r in enumerate(recipes, 1):
                print(f"{index}) {r.id} {r.name}")
            print("-" * 40, "\n")


class RecipeDetailTemplate(RecipeTemplate):

    """Шаблон вывода подробного рецепта"""
    def render(self, recipes: List[Recipe]):
        if len(recipes) == 0:
            print("Нет рецептов для отображения.")
        else:
            for r in recipes:
                print("=" * 40)
                print(f"ID: {r.id}")
                print(f"Название: {r.name}")
                print(f"Описание: {r.description}")
                print("Ингредиенты:")
                for ing in r.ingredients:
                    print(f" - {ing}")
                print(f"\nИнструкция:\n{r.instructions}")
                print("=" * 40, "\n")


# ** VIEW **

class RecipeView:
    def __init__(self, model: RecipeModel):
        self.model = model

    def render(self, template: RecipeTemplate):
        return template.render(self.model.get_recipes())


# ** ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ **

def show_menu():
    print("\n=== КНИГА РЕЦЕПТОВ ===")
    print("1) Добавить рецепт")
    print("2) Показать список рецептов")
    print("3) Показать все рецепты подробно")
    print("4) Удалить рецепт по ID")
    print("5) Редактировать рецепт по ID")
    print("6) Выйти")
    return int(input("Выберите пункт меню (1-6): "))

def create_recipe():
    name = input("Введите название рецепта: ")
    description = input("Введите краткое описание: ")
    ingredients = input("Введите ингредиенты через запятую: ").split(",")
    ingredients = [i.strip() for i in ingredients]
    instructions = input("Введите инструкцию приготовления: ")
    return Recipe(name, description, ingredients, instructions)

def update_recipe():
    print("Введите новые данные для рецепта:")
    return create_recipe()


# ** MAIN **

recipeModel = RecipeModel()
recipeView = RecipeView(recipeModel)

listTemplate = RecipeListTemplate()
detailTemplate = RecipeDetailTemplate()

while True:
    result = show_menu()

    match result:
        case 1:
            recipe = create_recipe()
            recipeView.model.add_recipe(recipe)
            print("Рецепт добавлен")
        case 2:
            recipeView.render(listTemplate)
        case 3:
            recipeView.render(detailTemplate)
        case 4:
            try:
                recipeView.render(listTemplate)
                id_to_delete = int(input("Введите ID рецепта для удаления: "))
                if recipeView.model.delete_recipe(id_to_delete):
                    print("Рецепт удалён")
                else:
                    print(" Рецепт с таким ID не найден.")
            except ValueError:
                print("Ошибка: ID должно быть числом.")
        case 5:
            try:
                recipeView.render(listTemplate)
                id_to_update = int(input("Введите ID рецепта для редактирования: "))
                new_recipe = update_recipe()
                if recipeView.model.update_recipe(id_to_update, new_recipe):
                    print("Рецепт обновлён")
                else:
                    print("Рецепт с таким ID не найден")
            except ValueError:
                print("Ошибка: ID должно быть числом")
        case 6:
            print("Выход из приложения")
            break
        case _:
            print("Неверный пункт меню") """