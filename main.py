import math # пробуем коммитить

def calculate_average(numbers: list[float]) -> float | None:
    """
    Функция вычисляет среднее арифметическое чисел в списке.
    Пустой список возвращается как None.
    Результат округляется вниз до целого числа.
    """
    print("Tested by Оксана Паскида")  
    if not numbers:
        return None
    avg = sum(numbers) / len(numbers)
    return math.floor(avg)  # округляем вниз до целого
