def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []

    for lista in lists:
        new = []
        i = j = 0

        while i < len(result) and j < len(lista):
            if result[i] <= lista[j]:
                new.append(result[i])
                i += 1
            else:
                new.append(lista[j])
                j += 1

        new += result[i:]
        new += lista[j:]
        result = new
    return result


if __name__ == "__main__":
    tests = [
        ([[1, 4], [2, 3], [5]], [1, 2, 3, 4, 5]),
        ([[1, 1], [1, 2]], [1, 1, 1, 2]),
        ([[], [2, 4], [1, 3]], [1, 2, 3, 4]),
        ([], []),
        ([[7]], [7]),
        ([[1, 3, 5], [2, 4, 6]], [1, 2, 3, 4, 5, 6]),
    ]

    for lists, expected in tests:
        result = merge_sorted_lists(lists)
        print(f"{lists}")
        print(f"Result:   {result}")
        print(f"Expected: {expected}")
        print("-" * 30)
