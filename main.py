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


num = int(input("введите любое не отрицательное число не больше 100_000: "))
