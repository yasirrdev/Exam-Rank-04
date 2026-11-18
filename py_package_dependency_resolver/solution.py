def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    indegree = {package: 0 for package in packages}

    for package in packages:
        for dependency in packages[package]:
            if dependency in packages:
                indegree[package] += 1

    cola = sorted([package for package in packages if indegree[package] == 0],
                  key=lambda x: (len(x), x))
    result = []

    while cola:
        current = cola.pop(0)
        result.append(current)

        for package in packages:
            if current in packages[package]:
                indegree[package] -= 1
                if indegree[package] == 0:
                    cola.append(package)
                    cola.sort(key=lambda x: (len(x), x))

    return result if len(result) == len(packages) else []
