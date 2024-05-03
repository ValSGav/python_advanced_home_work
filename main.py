print("Задача 1.")
print("Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей."
"Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других."
"Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует."
"Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.")
print()

side_a = int(input("введите длину стороны a"))
side_b = int(input("введите длину стороны b"))
side_c = int(input("введите длину стороны c"))

side_a_square = side_a ** 2;
side_b_square = side_b ** 2;
side_c_square = side_c ** 2;

if (side_a > side_b+side_c
        or side_b > side_a+side_c
        or side_c > side_b+side_a):
    print("треугольника с такими сторонами не существует")
elif side_a == side_b and side_a == side_c:
    print("треуголник равносторонний")
elif (side_a_square+side_b_square == side_c_square
      or side_a_square+side_c_square == side_b_square
      or side_c_square + side_b_square == side_a_square):
    print("треуголник прямоугольный")
elif side_a != side_b and side_a !=side_c and side_b != side_c:
    print("треуголник разносторонний")
else:
    print("треуголник не попадает под отдельную классификацию")

print()
print()
print("Задача 2.")
print("Напишите код, который запрашивает число и сообщает является ли оно простым или составным. "
      "Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. "
      "Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.")

def check_prime_number(numb)->bool:
    if numb < 3:
        return True
    for i in range(2, numb):
        if numb// i == 0:
            return True
    return False


num = int(input("Введите любое не отрицательное число не больше 100_000: "))

if num in range(0, 100_001):
    print("Это простое число" if check_prime_number(num) else "Это составное число")
else:
    print("Число вне указанного диапазона")


print()
print()
print("Задача 3.")
print("Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток."
      " Программа должна подсказывать “больше” или “меньше” после каждой попытки. "
      "Для генерации случайного числа используйте код: "
      "from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)")

from random import randint

target_numb = randint(0, 1001)

for i in range(1, 11):
    try_numb = int(input("Попытка №" + str(i) + "введите число: "))
    if try_numb == target_numb:
        print("Верно! Угадали!")
        break
    else:
        print("Загаданное число больше" if try_numb< target_numb else "Загаданное число меньше")
else:
    print("Попытки закончились, Вы не угадали число.")

