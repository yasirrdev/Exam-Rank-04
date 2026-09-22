def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:

    constellation = []

    for _ in range(dim):
        constellation.append(["."] * dim)

    for row, col in stars:
        if 0 <= row < dim and 0 <= col < dim:
            constellation[row][col] = "*"

    result = []

    for fila in constellation:
        result.append("".join(fila))

    return result


if __name__ == "__main__":

    print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))

    print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))

    print(constellation_mapper([(0, 0), (5, 5)], 3))

    print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))
