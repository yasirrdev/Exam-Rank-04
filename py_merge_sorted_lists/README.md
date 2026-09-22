# 04 - py_merge_sorted_lists

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna

## Enunciado

Escribe una función que fusione varias listas de enteros **ya ordenadas** en una única lista ordenada.

La función debe:

* Recibir una lista que contiene cero o más listas de enteros.
* Todas las listas de entrada están ordenadas de menor a mayor.
* Devolver una única lista con todos los elementos, manteniendo el orden ascendente.
* Se deben conservar los elementos duplicados.
* Si la entrada está vacía, debe devolver una lista vacía.

## Prototipo

```python
def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
```

## Ejemplos

```python
merge_sorted_lists([[1, 4], [2, 3], [5]])
# [1, 2, 3, 4, 5]
```

```python
merge_sorted_lists([[1, 1], [1, 2]])
# [1, 1, 1, 2]
```

```python
merge_sorted_lists([[], [2, 4], [1, 3]])
# [1, 2, 3, 4]
```

```python
merge_sorted_lists([])
# []
```

```python
merge_sorted_lists([[7]])
# [7]
```

## Casos borde

* La lista principal puede estar vacía.
* Puede haber listas internas vacías.
* Deben conservarse los duplicados.
* La función debe **devolver** una lista de enteros; no debe imprimir nada.
