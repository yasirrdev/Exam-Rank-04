def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

    if k > len(nums):
        return []
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []

    for i in range(0, len(nums) - k + 1):
        window = nums[i: i+k]
        maxn = max(window)
        result.append(maxn)

    return result


if __name__ == "__main__":
    tests = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([9, 5, 2, 8], 2, [9, 5, 8]),
        ([4, 1], 1, [4, 1]),
        ([], 3, []),
        ([1, 2, 3], 5, []),
        ([7, 7, 7], 2, [7, 7]),
    ]

    for nums, k, expected in tests:
        result = sliding_window_maximum(nums, k)
        print(f"{nums}, k={k}")
        print(f"Result:   {result}")
        print(f"Expected: {expected}")
        print("-" * 35)
