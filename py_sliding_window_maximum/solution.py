def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    iterations = len(nums) - k + 1

    return [max(nums[i:i + k]) for i in range(iterations)]
