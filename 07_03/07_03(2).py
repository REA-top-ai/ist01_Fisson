# Функция без рекурсии
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Функция с рекурсией
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
print(factorial_iterative(7))
print(factorial_recursive(7))

# Возведение чисел в квадрат

def square_list(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

numbers = [2, 5, 8, 3, 10]
print(square_list(numbers))

