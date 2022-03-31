import random


# Генератор квадратной матрицы заданной размерности
def generate_matrix(n):
    arr = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]
    return arr


# Вывод матрицы на экран
def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(f"{arr[i][j]:3} ", end='')
        print()
    print()


# Копирование матрицы
def copy_matrix(arr):
    n = len(arr)
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[i][j]
    return new_arr


# Расчет первого числа из уловия задачи
def get_first_num(arr, k):
    n = len(arr)
    s = 0
    for i in range(n):
        for j in range(n):
            b1 = j >= i
            b2 = j <= n - 1 - i
            b3 = j % 2 == 1
            if b1 and b2 and b3:
                if arr[i][j] > k:
                    s += 1
    return s


# Расчет второго числа из условия задачи
def get_second_num(arr):
    n = len(arr)
    s = 0
    for i in range(n):
        for j in range(n):
            b1 = j <= i
            b2 = j >= n - 1 - i
            b3 = i % 2 == 0
            if b1 and b2 and b3:
                s += arr[i][j]
    return s


# Симметрично поменять местами области 1 и 3 в заданной мтарице
def symmetric_change_1_and_3(arr):
    n = len(arr)
    for i in range(n // 2):
        for j in range(n):
            b1 = j >= i
            b2 = j <= n - 1 - i
            if b1 and b2:
                arr[i][j], arr[n - 1 - i][j] = arr[n - 1 - i][j], arr[i][j]


# Транспонирование матрицы
def transpose_matrix(arr):
    n = len(arr)
    new_arr = [[arr[j][i] for j in range(n)] for i in range(n)]
    return new_arr


# Умноение матрицы на число
def scale_matrix(arr, k):
    n = len(arr)
    new_arr = [[arr[i][j] * k for j in range(n)] for i in range(n)]
    return new_arr


# Сложение двух матриц
def add_matrices(arr1, arr2):
    n = len(arr1)
    new_arr = [[arr1[i][j] + arr2[i][j] for j in range(n)] for i in range(n)]
    return new_arr


# Умножение двух матриц
def multiply_matrices(arr1, arr2):
    n = len(arr1)
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                new_arr[i][j] += arr1[i][r] * arr2[r][j]
    return new_arr


# ---------------------------------------------------------------
#  Н А Ч А Л О     П Р О Г Р А М М Ы
# ---------------------------------------------------------------

# Цикл для ввода K
while True:
    try:
        k = int(input("Введите K:\n"))
        break
    except:
        print("Неверный ввод, нужно ввести целое число")

# Цикл для ввода N
while True:
    try:
        n = int(input("Введите размерность N матрицы A (не менее 2):\n"))
        if 2 <= n <= 100:
            break
        elif n == 1:
            print("Слишком маленькая размерность")
        elif n > 100:
            print("Слишком большая размерность")
        else:
            print("Недопустимая размерность")
    except:
        print("Неверный ввод, нужно ввести натуральное число не меньше 2")

A = generate_matrix(n)              # Генеририуем матрицу
print("\nСлучайно сгенерированная матрица A:")
print_matrix(A)                     # Выводим ее на экран

m = n // 2                          # Размерность подматриц
E = [[0] * m for _ in range(m)]     # Для всех 4х подматриц иниициализируем списки
B = [[0] * m for _ in range(m)]
D = [[0] * m for _ in range(m)]
C = [[0] * m for _ in range(m)]

# Все 4 подматрицы
for i in range(m):
    for j in range(m):
        E[i][j] = A[i][j]
        B[i][m - 1 - j] = A[i][n - 1 - j]
        D[m - 1 - i][j] = A[n - 1 - i][j]
        C[m - 1 - i][m - 1 - j] = A[n - 1 - i][n - 1 - j]

# Вывод подматриц на экран
print("\nМатрица E:")
print_matrix(E)
print("\nМатрица B:")
print_matrix(B)
print("\nМатрица D:")
print_matrix(D)
print("\nМатрица C:")
print_matrix(C)

# Для дальнейшей работы копируем матрицы
F = copy_matrix(A)
E2 = copy_matrix(E)

num1 = get_first_num(A, k)          # Первое число из условия задачи
num2 = get_second_num(A)            # Второе число из учловия задачи
print("\n\n\n")
print(f"Первое число: {num1}, второе число: {num2}")

# Сравниваем эти числа
# Первый случай
if num1 > num2:
    symmetric_change_1_and_3(E2)    # Симметрично меняем области 1 и 3 в подматрице E
    # Записываем полученную подматрицу в матрицу F
    for i in range(m):
        for j in range(m):
            F[i][j] = E2[i][j]
    print("Первое число больше, поэтому симметрично меняем области 1 и 3 в подматрице E матрицы F")
    print("Получаем следующую матрицу F:")
    print_matrix(F)
# Второй случай
else:
    # Меняем местами (несимметрично) подматрицы B и C
    for i in range(m):
        for j in range(m):
            F[i][n - 1 - j] = C[i][m - 1 - j]
            F[n - 1 - i][n - 1 - j] = B[m - 1 - i][m - 1 - j]
    print("Первое число не больше, поэтому несимметрично меняем местами подматрицы B и C матрицы F")
    print("Получаем следующую матрицу F:")
    print_matrix(F)


AF = multiply_matrices(A, F)        # Умножаем матрицы A и F
A_t = transpose_matrix(A)           # Транспонируем матрицу A
k_A_t = scale_matrix(A_t, -k)       # Умножаем транспонированную матрицу A на коэффициент -K
result = add_matrices(AF, k_A_t)    # Складываем полученные матрицы

print("Умножаем матрицы A и F")
print_matrix(AF)

print("Транспонируем матрицу A")
print_matrix(A_t)

print("Умножаем транспонированную матрицу A на коэффициент -K")
print_matrix(k_A_t)

print("Складываем полученные матрицы")
print_matrix(result)

