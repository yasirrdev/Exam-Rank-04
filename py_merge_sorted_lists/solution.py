def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []

    for lista in lists:
        result += lista

    return sorter(result)


def sorter(nums: list[int]) -> list[int]:
    result = nums[:]

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    return result
