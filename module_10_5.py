import time
from multiprocessing import Pool


def read_info(name):
    all_data = []  # Локальный список
    with open(name, 'r', encoding='utf-8') as file:
        while line := file.readline():
            all_data.append(line)  # Считываем строки и добавляем в список

if __name__ == '__main__':
    # Создаем список имен файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейный вызов занял: {linear_duration:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_duration = time.time() - start_time
    print(f"Многопроцессный вызов занял: {multiprocess_duration:.6f} секунд")
