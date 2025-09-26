def bubble_sort(arr, reverse=False):
    """
    Сортировка пузырьком.
    :param arr: список чисел
    :param reverse: если True — по убыванию, иначе — по возрастанию
    :return: отсортированный список
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Меняем условие в зависимости от направления
            if reverse:
                if arr[j] < arr[j + 1]:  # для убывания: больший элемент "всплывает"
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            else:
                if arr[j] > arr[j + 1]:  # для возрастания
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
        if not swapped:
            break
    return arr


def main():
    try:
        # Запрашиваем количество чисел
        n = int(input("Введите количество чисел: "))
        if n <= 0:
            print("Количество должно быть положительным.")
            return

        numbers = []
        print(f"Введите {n} чисел (по одному на строку):")
        for _ in range(n):
            num = float(input())
            numbers.append(num)

        # Запрашиваем направление сортировки
        while True:
            direction = input("Сортировать по возрастанию или по убыванию? (введите 'в' или 'у'): ").strip().lower()
            if direction in ('в', 'возрастанию'):
                reverse = False
                break
            elif direction in ('у', 'убыванию'):
                reverse = True
                break
            else:
                print("Пожалуйста, введите 'в' для возрастания или 'у' для убывания.")

        # Сортируем
        sorted_numbers = bubble_sort(numbers, reverse=reverse)

        # Выводим результат
        order = "убыванию" if reverse else "возрастанию"
        print(f"Отсортированный список по {order}:")
        print(sorted_numbers)

    except ValueError:
        print("Ошибка: введите корректное число.")


if __name__ == "__main__":
    main()