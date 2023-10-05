import time


def execution_speed(func):
    """
    Декоратор, который замеряет время выполнения функции
    """
    def general(num):
        time_start = time.time()
        func(num)
        time_end = time.time()
        result = (time_end - time_start) * 1000
        print(f'Функция : {func.__name__} выполнилась за {result} мс.')
    return general


@execution_speed
def count_to_(num):
    """
    Функция для перебора значений из переданного аргумента
    """
    warehouse_of_numbers = list()
    for i in range(num):
        warehouse_of_numbers.append(i)
    print(warehouse_of_numbers)



