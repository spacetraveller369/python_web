# 1) Декоратор для проверки аргументов функции: 
# Создайте декоратор, который проверяет типы аргументов функции. 
# Если тип аргумента не соответствует ожидаемому, выбрасывается исключение.

def DecoratorCheckType(OriginalFunction):
    def wrapper(*args:str):
        for arg in args:
            if not isinstance(arg, str): raise TypeError(f"Аргумент '{arg}' должен быть типа str")
        return OriginalFunction(*args)
    return wrapper
        

# 2) Декоратор для кэширования результатов: 
# Напишите декоратор, который будет кэшировать результаты функции. 
# Если функция вызывается с одинаковыми аргументами, то результат должен возвращаться из кэша, а не вызываться заново.

cache={}
def DecoratorCacheParams(cache:dict):
    def DecoratorCache(OriginalFunction):
        def wrapper(*args):
            results = []
            for arg in args:
                if arg in cache:
                    results.append(cache[arg])
                else:
                    cache[arg] = OriginalFunction(arg)
                    results.append(cache[arg])
            return results
        return wrapper
    return DecoratorCache




# 3) Декоратор для контроля доступа (логин): 
# Напишите декоратор, который проверяет, авторизован ли пользователь. 
# Если нет, выбрасывает исключение. В качестве аргумента функция будет принимать информацию о пользователе.

AuthentificatedUsers = {}


def RequireLogin(AuthentificatedUsers: dict):
    def Decorator(Func):
        def Wrapper(**kwargs):
            for Key, Value in kwargs.items():
                if Key not in AuthentificatedUsers or AuthentificatedUsers[Key] != Value:
                    raise PermissionError(f"Неверный логин или пароль для '{Key}'")
                return Func(**kwargs)
        return Wrapper
    return Decorator



# 5) Декоратор для повторного выполнения функции при исключении: 
# Создайте декоратор, который повторяет выполнение функции в случае возникновения исключения. 
# Количество попыток и интервал между попытками должны быть переданы как параметры декоратора.

def RetryOnException(MaxAttempts: int):
    def Decorator(Func):
        def Wrapper(*args, **kwargs):
            Attempt = 0
            while Attempt < MaxAttempts:
                try:
                    return Func(*args, **kwargs)
                except Exception as Error:
                    Attempt += 1
                    if Attempt >= MaxAttempts:
                        raise Error
        return Wrapper
    return Decorator


# 6) Генератор чисел Фибоначчи: Напишите генератор, который будет возвращать числа Фибоначчи. 
# Генератор должен бесконечно генерировать числа Фибоначчи, пока не будет остановлен.

def FibonacciGenerator():
    A, B = 0, 1
    while True:
        yield A
        A, B = B, A + B

# 7) Генератор чисел, делящихся на 3 или 5: 
# Напишите генератор, который будет генерировать числа, делящиеся на 3 или 5, начиная с 1 и до заданного предела.

def DivisibleByThreeOrFive(Limit: int):
    for Number in range(1, Limit + 1):
        if Number % 3 == 0 or Number % 5 == 0:
            yield Number


# 8) Напишите генератор, который вычисляет последовательность факториалов для чисел от 1 до бесконечности.

def FactorialSequence():
    Index = 1
    Result = 1
    while True:
        Result *= Index
        yield Result
        Index += 1

# 9) Напишите генератор, который возвращает только каждый n-й элемент из заданного списка.
def EveryNthElement(SourceList: list, Step: int):
    for Index in range(0, len(SourceList), Step):
        yield SourceList[Index]


# 10) Напишите замыкание, которое позволяет вызвать переданную функцию не более n раз. 
# После превышения лимита должна возвращаться ошибка или сообщение.

def LimitedCall(Function, MaxCalls: int):
    CallCount = 0
    def Wrapper(*args, **kwargs):
        nonlocal CallCount
        if CallCount >= MaxCalls:
            raise RuntimeError(f"Функция может быть вызвана не более {MaxCalls} раз")
        CallCount += 1
        return Function(*args, **kwargs)
    return Wrapper

# 11) Создайте замыкание, которое принимает список чисел и возвращает функцию, проверяющую, принадлежит ли число этому списку.

def NubmerInList(NumberList: list):
    def Checker(Value: int):
        return Value in NumberList
    return Checker

NumberList = [1,2,3]

Checker = NubmerInList(NumberList)
print(Checker(5))

# 12) Напишите замыкание, которое принимает шаблон строки и возвращает функцию, которая форматирует строку по этому шаблону.

def CreateFormatter(Template: str):
    def Formatter(**kwargs):
        return Template.format(**kwargs)
    return Formatter

# 13) Создайте замыкание, которое принимает число и возвращает разницу между этим числом и предыдущим вызовом функции.

def Difference():
    Previous = None
    def Tracker(Current: int):
        nonlocal Previous
        if Previous is None:
            Delta = 0
        else:
            Delta = Current - Previous
        Previous = Current
        return Delta
    return Tracker


# 14) Напишите замыкание, которое считает, сколько раз функция была вызвана с каждым уникальным аргументом.

def CallCounter():
    CallNumber = {}
    def Counter(Value):
        CallNumber[Value] = CallNumber.get(Value, 0) + 1
        return f"{Value} был вызван {CallNumber[Value]} раз(а)"
    return Counter