def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    result = set(lists[0])

    for lista in lists[1:]:
        result &= set(lista)

    return sorted(result)


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 5]]))      # [2]
    print(list_intersection_finder([[7, 8], [8, 7], [7, 8, 9]]))        # [7,8]
    print(list_intersection_finder([[1, 2, 3]]))                    # [1,2,3]
    print(list_intersection_finder([[1, 2], [3, 4]]))                # []
    print(list_intersection_finder([]))                           # []
