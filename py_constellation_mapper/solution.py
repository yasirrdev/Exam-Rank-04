def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = [["."] * dim for _ in range(dim)]

    for row, col in stars:
        if 0 <= row < dim and 0 <= col < dim:
            grid[row][col] = "*"

    return ["".join(row) for row in grid]


if __name__ == "__main__":

    tests = [
        (
            [(0, 0), (1, 1), (2, 2)],
            3,
            ["*..", ".*.", "..*"]
        ),
        (
            [(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)],
            3,
            [".*.", "***", ".*."]
        ),
        (
            [],
            2,
            ["..", ".."]
        ),
        (
            [(0, 0), (0, 0), (1, 1)],
            2,
            ["*.", ".*"]
        ),
        (
            [(0, 0), (5, 5)],
            3,
            ["*..", "...", "..."]
        ),
        (
            [(1, 0), (1, 1), (1, 2)],
            3,
            ["...", "***", "..."]
        ),
    ]

    for stars, dim, expected in tests:
        result = constellation_mapper(stars, dim)

        print(f"Input:    {stars}, dim={dim}")
        print(f"Result:   {result}")
        print(f"Expected: {expected}")
        print(f"OK:       {result == expected}")
        print("-" * 40)
