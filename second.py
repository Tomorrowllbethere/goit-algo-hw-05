import re
from typing import Callable

def generator_numbers(text:str) -> float: # створюємо функцію, яка приймає текст і редагує його
    pattern = r'\s\d+\.?\d+\s' # створюємо патерн для пошуку числових даних
    maches=re.findall(pattern, text) # записуємо знайдені дані в змінній
    number = [float(el.strip()) for el in maches] #редагуємо знайдені числа (змінюємо тип, видаляємо відступи)
    for num in number: #використовуючи цикл, повертаємо дані
        yield num

def sum_profit(text: str, func: Callable): #створюємо функцію, яка вирахує суму
    gen = generator_numbers(text) # присвоюємо функцію, яка редагує текст
    sum = 0 # створюємо змінну для суми
    for num in gen: #використовуючи цикл, рахуємо суму при кожній ітерації 
        sum += num
    return sum #повертаємо суму

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
generator_numbers(text)
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")