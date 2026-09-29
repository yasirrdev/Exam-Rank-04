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
