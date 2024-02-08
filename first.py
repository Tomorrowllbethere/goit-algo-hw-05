from collections import defaultdict

def caching_fibonacci():#створення основної функції
    cache= defaultdict(int) #ствoрення словника для зберігання кешу
    def fibonacci(n):# оголошення функції підрахунку
        if n <= 0:# перевірка умови на базові випадки
            return 0
        elif n == 1:# первірка на ще один базовий випадок
            return 1
        elif n in cache is True:# якщо дані є в словнику, тоді просто виводимо звідти
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # формула підрахунку фібоначчі і збереження значення в словнику
        return cache[n]
    return fibonacci
fib = caching_fibonacci()#присвоювання функції
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  
print(fib(15))  