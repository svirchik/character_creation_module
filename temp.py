from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculatesquareroot(number: float) -> float:
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number: float) -> None:
    if your_number <= 0:
        return
    root = calculatesquareroot(your_number)
    print("Мы вычислили квадратный корень из введённого вами числа."
          f"Это будет: {root}")


print(message)
calc(25.5)
