'''
Practice

1. Create a decorator that will check types. 
It should take a function with arguments and validate inputs with annotations.

Example:

@check_types
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)
> 3

add(1, "2")
> TypeError: Argument b must be int, not str



2.Write a decorator that will calculate the execution time of a function.
Example:
    @calculate_execution_time
    def add(a: int, b: int) -> int:
        return a + b
add(1, 2)
    > 3
    > Execution time: 0.0005 seconds
'''



# Practice Task 1 

#creating a decorator that checks type of variable.


    
def typecheker(function): # Створюємо декоратор, який додає чекер типу змінн.
    def wrapper(a, b):
        if type(a) not in (int, float):
            raise TypeError('Argument "a" must be int or float') #  raise, примусово піднімає зазначений виняток.
        if type(b) not in (int, float):
            raise TypeError('Argument "b" must be int or float')
        return function(a, b)

    return wrapper
                 
@typecheker # використовуємо наш декоратор
def add(a: int, b: int) -> int:
    return a + b

add(36,'6')




# Practice Task 2


def timechecker(func):
    import time

    def wrapper(*args, **kwargs):
        run = time.time()
        blackbox = func(*args, **kwargs)
        finish = time.time()
        print(f'Функція виконувала своє завдання протягом {float(finish - run)} seconds')
        return blackbox

    return wrapper


@timechecker
def add(a: int, b: int) -> int:
    return a + b

add(36, 6)