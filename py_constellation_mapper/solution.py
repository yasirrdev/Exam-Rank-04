def constellation_mapper(stars: list[tuple[int, int]]) -> list[str]:
    if not stars:
        return []

    max_x = 0
    max_y = 0

    for x, y in stars:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    constellation = []
    fila = ["."] * (max_x + 1)

    for _ in range(max_y + 1):
        constellation.append(fila.copy())

    for x, y in stars:
        constellation[y][x] = "*"

    result = []

    for fila in constellation:
        result.append("".join(fila))

    return result


if __name__ == "__main__":
    tests = [
        [(0, 0)],
        [(0, 0), (2, 1)],
        [(1, 1), (0, 2)],
        [(2, 0), (0, 0), (1, 0)],
        []
    ]

    for stars in tests:
        print(f"Input: {stars}")
        result = constellation_mapper(stars)
        for row in result:
            print(row)
        print("-" * 20)
