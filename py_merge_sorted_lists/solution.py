def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    result = []

    for lista in lists:
        result += lista

    return sorted(result)
