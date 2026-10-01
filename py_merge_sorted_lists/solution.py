def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []

    for lista in lists:
        result += lista

    return sorted(result)

