class IncorrectVinNumber(Exception):
    """Исключение для некорректного VIN номера."""

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    """Исключение для некорректных номеров автомобиля."""

    def __init__(self, message):
        self.message = message


class Car:
    """Класс, представляющий автомобиль."""

    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    @property
    def vin(self):
        """Возвращает VIN номер автомобиля."""
        return self.__vin

    @vin.setter
    def vin(self, vin_number):
        """Устанавливает VIN номер автомобиля."""
        self.__is_valid_vin(vin_number)
        self.__vin = vin_number

    @property
    def numbers(self):
        """Возвращает номера автомобиля."""
        return self.__numbers

    @numbers.setter
    def numbers(self, numbers):
        """Устанавливает номера автомобиля."""
        self.__is_valid_numbers(numbers)
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        """Проверяет корректность VIN номера."""
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        """Проверяет корректность номеров автомобиля."""
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')
try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')
try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')