numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # простые числа делится только на себя и на 1
not_primes = []  # не простые числа
index = 0

for i in numbers:
    if i == 1:
        continue
    if i < 2:
        not_primes.append(i)
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
