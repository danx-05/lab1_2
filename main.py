def bubble_sort(arr):
    """Сортировка пузырьком по возрастанию."""
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации: если за проход не было обменов — массив отсортирован
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
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
            num = float(input())  # используем float, чтобы поддерживать дробные числа
            numbers.append(num)

        # Сортируем с помощью пузырька
        sorted_numbers = bubble_sort(numbers)

        # Выводим результат
        print("Отсортированный список по возрастанию:")
        print(sorted_numbers)

    except ValueError:
        print("Ошибка: введите корректное число.")


if __name__ == "__main__":
    main()