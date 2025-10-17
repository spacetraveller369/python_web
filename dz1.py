# 1. Створіть функцію, яка підраховує кількість цифр у числі    
def NumQuantity(number):
    return len(str(number))

# 2. Користувач вводить рядок, необхідно отримати кількість повторень кожного слова в рядку. Ігноруємо коми, крапки.
#    Вивід:
#    слово: кількість
#    і т.д.

def WordQuantity(word, string):
    words = string.split().count(word)
    print (f'{word}:{words}')

# 3. Створити список із цілих чисел. Його необхідно відфільтрувати, щоб у результаті залишилися парні числа. 
# Вивести квадрати цих чисел, використовуючи map.
def FilteredList(numlist):
    print (list(map(lambda x:x*x,list (filter(lambda n:n%2==0,numlist)))))

# 4. Створіть словник, у якому кожна пара — це студент і список його оцінок
# * Вивести по кожному студенту середній бал
# * Вивести студента з максимальною оцінкою
d = {'student1': [10, 12, 11], 'student2': [9, 8, 7], 'student3': [5, 4, 3]}
def StudentStat(dictionary):
    for student, grade in dictionary.items():
        ag = sum (grade)/len (grade)
        mg = max(grade)
        print(f"{student} : average grade = {ag}, max grade = {mg}")

# 5. Напишіть функцію, яка приймає рядок і повертає словник, де ключ — це символ рядка, а значення — кількість його повторень.
def CharFrequency(s):
    st = set(s)
    freq = {}
    for item in st:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 6. Створіть кортеж із кількох рядків і чисел. Напишіть функцію, яка повертає новий кортеж, що містить лише числа.

MixedTuple = ("hello", 42, "world", 3.14, 7, "!", -1)

def ExtractNumbers(data):
    temp = []
    for item in data:
        if isinstance(item, (int, float)):
            temp.append(item)
    return tuple(temp)

# 7. Напишіть функцію, яка приймає список рядків і повертає список, у якому рядки відсортовані за довжиною.
def SortByLength(strings):
    return sorted(strings, key=len)

# 8. Створіть словник із даними про співробітників компанії (ім’я, посада, зарплата). 
# Напишіть функцію, яка сортує співробітників за зарплатою.

employees = {
    "Марія": {"position": "Медсестра", "salary": 4000},
    "Олексій": {"position": "Адвокат", "salary": 10000},
    "Петро": {"position": "Касир", "salary": 6000},
    "Ілона": {"position": "Розробник", "salary": 18000}
}

def SortedEmployees(employees):
    sorted_items = sorted(employees.items(), key=lambda item: item[1]["salary"])
    return dict(sorted_items)

# 9. Використовуючи лямбда-вираз, створіть функцію, яка повертає найбільше з двох чисел.
MaxOfTwo = lambda x, y: max([x, y])

# 10. Напишіть функцію, яка знаходить усі унікальні елементи в списку і повертає їх у вигляді множини.
def Set(data):
    return set(data)

# 11. Створіть словник, де ключі — це числа від 1 до 10, а значення — їхні квадрати. 
# Напишіть функцію, яка знаходить суму всіх значень у словнику.

def SquaringDictionary():
    d = {}
    for i in range(1,11):
        d[i] = (i*i)
    return sum(d.values())

    
# 12. Напишіть функцію, яка приймає список чисел і повертає новий список, що містить лише ті числа, які більші за 10 і парні.
def FilteredList2(data):
    # return list (filter (lambda n: n%2==0, filter(lambda i:i>10, data)))
    # return list (filter (lambda n: n%2==0 and n>10,data))
    return [x for x in data if x > 10 and x % 2 == 0]

# 13. Створіть кортеж із кількох чисел. Напишіть функцію, яка знаходить суму всіх чисел у кортежі.
numbers = (3, 7, 2, 10, 5)
 
def TuppleSum (numbers):
    return sum(numbers)

# 14. Напишіть лямбда-функцію, яка перевіряє, чи є число додатним.
Plus = lambda x: x > 0
print(Plus(1))

NonNegative = lambda x: x >= 0

# 15. Створіть словник, у якому зберігаються імена людей і їхній вік. 
# Напишіть функцію, яка приймає вік і повертає список імен людей, старших за цей вік.
people_age = {
    "Марія": 43,
    "Олексій": 40,
    "Петро": 21,
    "Ілона": 31,
    "Софія": 5
}

def AgedList (data, age):
    l = list (filter(lambda x:x[1]>age, data.items()))
    sl = sorted(l, key = lambda item: item[1])
    return list(dict(sl).keys())
    # return [name for name, years in data.items() if years > age]

# 16. Створіть кортеж із чисел і напишіть функцію, яка знаходить найбільше і найменше значення в кортежі.
numbers = (3, 6, 19, 8, 11, 9)

def MinMax(numbers):
    return min(numbers), max(numbers)


# 17. Використовуючи лямбда-вираз і функцію filter, знайдіть усі числа, які діляться на 3, у списку чисел.
def DivisibleByThree(data):
    return list(filter(lambda x: x % 3 == 0, data))

# 18. Напишіть функцію, яка перетворює рядок у список кортежів, де кожен кортеж містить символ і його індекс у рядку.
def CharIndexTuples(text):
    return [(char, index) for index, char in enumerate(text)]

def CharIndexTuples(text):
    result = []
    for i in range(len(text)):
        result.append((text[i], i))
    return result