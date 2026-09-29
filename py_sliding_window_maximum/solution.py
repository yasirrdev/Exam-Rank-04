def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    iterations = len(nums) - k + 1

    return [max(nums[i:i + k]) for i in range(iterations)]


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
