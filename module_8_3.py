class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__validate_vin(vin)
        self.__numbers = self.__validate_numbers(numbers)

    def __validate_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number

    def __validate_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return numbers

try:
    first = Car('Model1', 1000000, 'f123dj')
    print(f'{first.model} успешно создан')
except (IncorrectVinNumber, IncorrectCarNumbers) as exc:
    print(exc)

try:
    second = Car('Model2', 300, 'т001тр')
    print(f'{second.model} успешно создан')
except (IncorrectVinNumber, IncorrectCarNumbers) as exc:
    print(exc)

try:
    third = Car('Model3', 2020202, 'нет номера')
    print(f'{third.model} успешно создан')
except (IncorrectVinNumber, IncorrectCarNumbers) as exc:
    print(exc)
