def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    result = set(lists[0])

    for lista in lists[1:]:
        result &= set(lista)

    return sorted(result)
