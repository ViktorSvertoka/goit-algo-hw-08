import heapq


def min_cost_to_connect_cables(cable_lengths):

    # Ініціалізуємо купу
    heapq.heapify(cable_lengths)

    # Визначаємо загальні витрати
    total_cost = 0

    # Поки в купі більше одного кабеля
    while len(cable_lengths) > 1:
        # Вибираємо два найменших елементи
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Додаємо витрати на з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель до купи
        heapq.heappush(cable_lengths, cost)

        # Друк проміжних результатів
        print(
            f"Об'єднання кабелів {first} та {second} з витратами {cost}. Загальні витрати: {total_cost}"
        )
        print(f"Поточний стан купи: {cable_lengths}")

    return total_cost


if __name__ == "__main__":
    cable_lengths = [7, 1, 6, 4]
    min_cost = min_cost_to_connect_cables(cable_lengths)
    print("Мінімальні витрати на об'єднання кабелів:", min_cost)
