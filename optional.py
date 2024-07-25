import heapq


def merge_k_lists(lists):

    min_heap = []

    # Ініціалізуємо купу першими елементами з кожного списку разом з індексами списку та елемента
    for i in range(len(lists)):
        if lists[i]:  # перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    merged_list = []

    # Виконуємо витягування мінімальних елементів і додаємо нові елементи до купи
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)

        # Якщо в поточному списку є ще елементи, додаємо наступний до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged_list


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
