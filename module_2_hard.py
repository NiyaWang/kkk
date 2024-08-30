def generate_password(n):
    result = ""

    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += str(i) + str(j)

    return result


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")