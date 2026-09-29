def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

    if not packages:
        return []

    indegree = {package: 0 for package in packages}

    for package in packages:
        for dependency in packages[package]:
            if dependency in packages:
                indegree[package] += 1

    cola = [package for package in packages if indegree[package] == 0]
    result = []
    while cola:
        current = cola.pop(0)
        result.append(current)

        for package in packages:
            if current in packages[package]:
                indegree[package] -= 1
                if indegree[package] == 0:
                    cola.append(package)
    return result if len(result) == len(packages) else []


if __name__ == "__main__":
    tests = [
        (
            {"A": ["B"], "B": ["C"], "C": []},
            ["C", "B", "A"]
        ),
        (
            {"app": ["core", "utils"], "core": [], "utils": []},
            ["core", "utils", "app"]
        ),
        (
            {"A": ["B"], "B": ["A"]},
            []
        ),
        (
            {},
            []
        ),
        (
            {"A": ["X"], "B": ["A"]},
            ["A", "B"]
        ),
    ]

    for packages, expected in tests:
        result = package_dependency_resolver(packages)
        print(packages)
        print(f"Result:   {result}")
        print(f"Expected: {expected}")
        print("-" * 40)
