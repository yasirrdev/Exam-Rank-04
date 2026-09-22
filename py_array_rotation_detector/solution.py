def array_rotation_detector(a: list[int], b: list[int]) -> bool:

    if len(a) != len(b):
        return False
    if not a and not b:
        return True

    doble = a + a

    for i in range(len(a)):
        if doble[i: i + len(a)] == b:
            return True

    return False


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [3, 4, 1, 2], True),
        ([5, 6, 7], [7, 5, 6], True),
        ([1, 2, 3], [2, 1, 3], False),
        ([], [], True),
        ([1, 2], [1, 2, 3], False),
        ([1, 1, 2], [2, 1, 1], True),
        ([1], [1], True),
        ([1], [2], False),
    ]

    for a, b, expected in tests:
        result = array_rotation_detector(a, b)
        print(f"{a} -> {b}")
        print(f"Result: {result} | Expected: {expected}")
        print("-" * 30)
