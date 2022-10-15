"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if not number % i:
            return False
    return True

def filter_numbers(list_of_numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [number for number in list_of_numbers if number % 2 !=0]
    if filter_type == EVEN:
        return [number for number in list_of_numbers if number % 2 ==0]
    if filter_type == PRIME:
        return [number for number in list_of_numbers if is_prime(number)]
