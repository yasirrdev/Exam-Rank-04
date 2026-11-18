
import importlib.util


def load_solution(folder):
    path = f"{folder}/solution.py"

    spec = importlib.util.spec_from_file_location(folder, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def run_tests(name, function, tests):
    print(f"\n=== {name} ===")

    passed = 0

    for args, expected in tests:
        result = function(*args)

        if result == expected:
            print(f"✓ {args} -> {result}")
            passed += 1
        else:
            print(f"✗ {args}")
            print(f"  Esperado: {expected}")
            print(f"  Obtenido: {result}")

    print(f"{passed}/{len(tests)} tests OK")

    return passed == len(tests)


def main():

    exercises = [

        (
            "py_constellation_mapper",
            "constellation_mapper",
            [
                (([(0, 0), (1, 1), (2, 2)], 3), ["*..", ".*.", "..*"]),
                (([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3),
                 [".*.", "***", ".*."]),
                (([], 2), ["..", ".."]),
                (([(0, 0), (0, 0), (1, 1)], 2), ["*.", ".*"]),
                (([(0, 0), (5, 5)], 3), ["*..", "...", "..."]),
                (([(2, 0), (0, 2)], 3), ["..*", "...", "*.."]),
                (([(0, 0), (2, 2), (1, 1), (1, 1)], 3),
                 ["*..", ".*.", "..*"]),
                (([(3, 0), (-1, 1)], 3), ["...", "...", "..."]),
                (([], 0), []),
            ]
        ),

        (
            "py_list_intersection_finder",
            "list_intersection_finder",
            [
                (([[1, 2, 3], [2, 3, 4], [2, 5]],), [2]),
                (([[7, 8], [8, 7], [7, 8, 9]],), [7, 8]),
                (([[1, 2, 3]],), [1, 2, 3]),
                (([[1, 2], [3, 4]],), []),
                (([],), []),
                (([[1, 1, 2, 2], [1, 2, 2, 3]],), [1, 2]),
                (([[1, 2], [1, 2], [1, 2]],), [1, 2]),
                (([[1, 2, 3], []],), []),
                (([[0, -1, -2], [-2, 0, 5]],), [-2, 0]),
                (([[5]],), [5]),
            ]
        ),

        (
            "py_array_rotation_detector",
            "array_rotation_detector",
            [
                (([1, 2, 3, 4], [3, 4, 1, 2]), True),
                (([5, 6, 7], [7, 5, 6]), True),
                (([1, 2, 3], [2, 1, 3]), False),
                (([], []), True),
                (([1, 2], [1, 2, 3]), False),
                (([1, 2, 3], [3, 1, 2]), True),
                (([1, 1, 2], [1, 2, 1]), True),
                (([1, 1, 2], [2, 2, 1]), False),
                (([1], [1]), True),
                (([1], [2]), False),
                (([0, 0, 0], [0, 0, 0]), True),
            ]
        ),

        (
            "py_merge_sorted_lists",
            "merge_sorted_lists",
            [
                (([[1, 4], [2, 3], [5]],), [1, 2, 3, 4, 5]),
                (([[1, 1], [1, 2]],), [1, 1, 1, 2]),
                (([[], [2, 4], [1, 3]],), [1, 2, 3, 4]),
                (([],), []),
                (([[7]],), [7]),
                (([[1, 2, 3], [4, 5, 6]],), [1, 2, 3, 4, 5, 6]),
                (([[1, 3, 5], [2, 4, 6]],), [1, 2, 3, 4, 5, 6]),
                (([[1, 1, 1], [1, 1]],), [1, 1, 1, 1, 1]),
                (([[-5, -2], [-4, -3]],), [-5, -4, -3, -2]),
                (([[], [], []],), []),
                (([[1], [], [2], [], [3]],), [1, 2, 3]),
            ]
        ),

        (
            "py_package_dependency_resolver",
            "package_dependency_resolver",
            [
                (({"A": ["B"], "B": ["C"], "C": []},),
                 ["C", "B", "A"]),
                (({"app": ["core", "utils"], "core": [], "utils": []},),
                 ["core", "utils", "app"]),
                (({"A": ["B"], "B": ["A"]},), []),
                (({},), []),
                (({"A": ["X"], "B": ["A"]},), ["A", "B"]),
                (({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]},),
                 ["api", "web", "backend", "frontend"]),
                (({"A": [], "B": [], "C": [], "D": []},),
                 ["A", "B", "C", "D"]),
                (({"app": ["core"], "core": ["utils"], "utils": []},),
                 ["utils", "core", "app"]),
                (({"A": ["X"], "B": ["Y"], "X": [], "Y": []},),
                 ["X", "Y", "A", "B"]),
                (({"A": ["missing"], "B": ["A"]},), ["A", "B"]),
                (({"A": ["B"], "B": ["C"], "C": ["A"]},), []),
                (({"database": [], "api": ["database"], "web": ["api"],
                   "app": ["web"]},),
                 ["database", "api", "web", "app"]),
                (({"a": [], "bb": [], "ccc": [], "dddd": []},),
                 ["a", "bb", "ccc", "dddd"]),
            ]
        ),

        (
            "py_palindrome_partitioner",
            "palindrome_partitioner",
            [
                (("aab",), 1),
                (("racecar",), 0),
                (("abcbm",), 2),
                (("a",), 0),
                (("",), 0),
                (("banana",), 1),
                (("abc",), 2),
                (("abba",), 0),
                (("abcba",), 0),
                (("aabb",), 1),
                (("abab",), 1),
                (("abcdef",), 5),
                (("noonabbad",), 2),
                (("aaaaaa",), 0),
                (("abacdc",), 1),
            ]
        ),

        (
            "py_sliding_window_maximum",
            "sliding_window_maximum",
            [
                (([1, 3, -1, -3, 5, 3, 6, 7], 3),
                 [3, 3, 5, 5, 6, 7]),
                (([9, 5, 2, 8], 2), [9, 5, 8]),
                (([4, 1], 1), [4, 1]),
                (([], 3), []),
                (([1, 2, 3], 5), []),
                (([1, 2, 3, 4, 5], 2), [2, 3, 4, 5]),
                (([5, 4, 3, 2, 1], 3), [5, 4, 3]),
                (([2, 2, 2, 2], 2), [2, 2, 2]),
                (([-5, -2, -8, -1], 2), [-2, -2, -1]),
                (([7], 1), [7]),
                (([1, 3, 2, 5, 4], 5), [5]),
                (([1, 2, 3], 0), []),
                (([1, 2, 3], -1), []),
            ]
        ),
    ]

    total = 0
    passed = 0

    for folder, function_name, tests in exercises:
        module = load_solution(folder)
        function = getattr(module, function_name)

        if run_tests(folder, function, tests):
            passed += 1

        total += 1

    print("\n" + "=" * 40)
    print(f"RESULTADO: {passed}/{total} ejercicios completos")
    print("=" * 40)


if __name__ == "__main__":
    main()
