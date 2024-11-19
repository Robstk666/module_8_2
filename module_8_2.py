def personal_sum(numbers):
    result = 0  # Сумма чисел
    incorrect_data = 0  # Счётчик некорректных данных

    for item in numbers:
        if isinstance(item, (int, float)):
            result += item
        else:
            incorrect_data += 1  # Увеличиваем счётчик некорректных данных
            print(f"Некорректный тип данных для подсчёта суммы - {item}")

    return result, incorrect_data


def calculate_average(numbers):
    try:
        iter(numbers)  # Проверяем, является ли numbers итерируемым
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

    total_items = len(numbers)

    if total_items == 0:
        return 0

    # Используем personal_sum для подсчёта суммы
    result, incorrect_data = personal_sum(numbers)

    valid_count = total_items - incorrect_data

    if valid_count == 0:
        return 0

    return result / valid_count


# Примеры вызова функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Каждый символ строки обрабатывается отдельно
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Некорректные данные учитываются
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Только корректные данные
        