1.
def operation(func, x: int, y: int) -> int:
    return func(x,y)
def multiply(a, b):
    return a * b

result = operation(multiply,5,4)
print(result)
2
def my_map(func, my_list: list) -> list:
    return list(map(func, my_list))

txt =  [1, 2, 3, 4]
result = my_map(lambda x: x ** 2, txt)
print(result)




3.
def filter_even_numbers(numbers: list) -> list:
  
    return list(filter(lambda x: x % 2 != 0, numbers))

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = filter_even_numbers(numbers_list)
print(result)
4
def recursive_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * recursive_factorial(n-1)

print(recursive_factorial(5))
5
import time

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper

@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]

print(sample_func())
6
def compose(*funcs):
    def new_func(x):
        result = x
        for func in reversed(funcs):
            result = func(result)
        return result
    
    return new_func


double = lambda x: x ** 2
square = lambda x: x * 2

composed_function = compose(double, square)
result = composed_function(6)
print(result)
8
from functools import reduce

def multiply(a, b):
    return a * b

def factorial_reduce(n: int) -> int:
    result = reduce(multiply, range(1,n+1))
    return result

result = factorial_reduce(5)
print(result)


12
def recursive_reverse(my_list: list) -> list:
    if not my_list:
        return []
    else:
        return [my_list[-1]] + recursive_reverse(my_list[:-1])

alim = [1, 2, 3, 4, 5]
result = recursive_reverse(alim)
print(result)
13 
import atexit

def count_calls(func):
    
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0  
    atexit.register(lambda: print(f"{func.__name__} was called {wrapper.calls} times."))

    return wrapper

@count_calls
def test_function():
    return



test_function()
test_function()
14
from functools import reduce

def find_max(numbers: list) -> int:
    return reduce(lambda x, y: x if x > y else y, numbers)

numbers_list = [1, 2, 3, 4, 5]
result = find_max(numbers_list)
print(result)
15

def remove_elements(my_list: list, element):
    return list(filter(lambda x: x != element, my_list))

result = remove_elements([1, 2, 3, 2, 4, 2, 5], 2)
print(result)

16
def repeat(n: int):
    def repeat_string(s: str) -> str:
        return s * n

    return repeat_string


repeat_three_times = repeat(3)
result = repeat_three_times(input(""))
print(result)
17 
def recursive_sum(my_list: list) -> int:
   
   if not my_list:
        return 0
   else:
        return my_list[0] + recursive_sum(my_list[1:])
18

def add_two_lists(list1: list, list2: list) -> list:
    return list(map(lambda x, y: x + y, list1, list2))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = add_two_lists(list1, list2)

print(result)
