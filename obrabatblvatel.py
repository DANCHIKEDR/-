"""
Модуль для ввода и обработки данных (целые числа, строки)
Используется для демонстрации работы с Git в рамках учебного проекта.
"""

def input_integers():
    """Ввод целых чисел до пустого ввода"""
    numbers = []
    print("Введите целые числа (пустая строка - завершить):")
    while True:
        val = input("> ")
        if val == "":
            break
        try:
            numbers.append(int(val))
        except ValueError:
            print("Ошибка: введите целое число или оставьте строку пустой.")
    return numbers


def input_strings():
    """Ввод строк до пустого ввода"""
    strings = []
    print("Введите строки (пустая строка - завершить):")
    while True:
        val = input("> ")
        if val == "":
            break
        strings.append(val)
    return strings


def process_numbers(nums):
    """Обработка списка чисел: сумма, количество, среднее, максимум, минимум"""
    if not nums:
        return "Нет чисел для обработки."
    return {
        "сумма": sum(nums),
        "количество": len(nums),
        "среднее": sum(nums) / len(nums),
        "максимум": max(nums),
        "минимум": min(nums)
    }


def process_strings(strs):
    """Обработка строк: объединение, самая длинная, самая короткая"""
    if not strs:
        return "Нет строк для обработки."
    concat = "".join(strs)
    longest = max(strs, key=len)
    shortest = min(strs, key=len)
    return {
        "объединённая строка": concat,
        "самая длинная": longest,
        "самая короткая": shortest
    }


def main():
    print("=== Модуль обработки данных ===")
    # Ввод чисел
    nums = input_integers()
    if nums:
        print("Результаты обработки чисел:")
        res_nums = process_numbers(nums)
        for k, v in res_nums.items():
            print(f"  {k}: {v}")
    else:
        print("Числа не введены.")

    print("\n---")

    # Ввод строк
    strs = input_strings()
    if strs:
        print("Результаты обработки строк:")
        res_strs = process_strings(strs)
        for k, v in res_strs.items():
            print(f"  {k}: {v}")
    else:
        print("Строки не введены.")


if __name__ == "__main__":
    main()