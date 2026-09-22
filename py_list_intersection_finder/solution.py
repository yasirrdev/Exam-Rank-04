def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    result = lists[0].copy()

    for lista in lists[1:]:
        new_result = []
        for num in result:
            if num in lista:
                new_result.append(num)
        result = new_result

    result = list(set(result))
    result.sort()
    return result


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 5]]))      # [2]
    print(list_intersection_finder([[7, 8], [8, 7], [7, 8, 9]]))        # [7,8]
    print(list_intersection_finder([[1, 2, 3]]))                    # [1,2,3]
    print(list_intersection_finder([[1, 2], [3, 4]]))                # []
    print(list_intersection_finder([]))                           # []
