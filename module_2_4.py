numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # простые числа делится только на себя и на 1
not_primes = [] # не простые числа
for i in numbers:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                not_primes.append(i)
                break
        else:
            primes.append(i)
print(primes)
print(not_primes)
