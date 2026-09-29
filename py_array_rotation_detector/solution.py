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
