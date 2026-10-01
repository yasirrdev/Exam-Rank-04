def array_rotation_detector(a: list[int], b: list[int]) -> bool:
    if len(a) != len(b):
        return False

    if not a and not b:
        return True

    for _ in range(len(a)):
        if a == b:
            return True
        a = a[1:] + a[:1]
    return False
