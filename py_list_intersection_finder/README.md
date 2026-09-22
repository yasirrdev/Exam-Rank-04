# 02 - py_list_intersection_finder

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna

## Enunciado

Escribe una función que encuentre los elementos comunes presentes en **todas** las listas recibidas.

La función debe:

* Recibir una lista que contiene una o más listas de enteros.
* Devolver una lista con los elementos que aparecen en **todas** las listas.
* Cada elemento debe aparecer **una sola vez** en el resultado.
* El orden del resultado debe ser **ascendente**.
* Si la entrada está vacía, debe devolver una lista vacía.

## Prototipo

```python
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
```

## Ejemplos

```python
list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 5]])
# [2]
```

```python
list_intersection_finder([[7, 8], [8, 7], [7, 8, 9]])
# [7, 8]
```

```python
list_intersection_finder([[1, 2, 3]])
# [1, 2, 3]
```

```python
list_intersection_finder([[1, 2], [3, 4]])
# []
```

```python
list_intersection_finder([])
# []
```

## Casos borde

* La lista principal puede estar vacía.
* Puede haber listas con elementos repetidos.
* El resultado no debe contener duplicados.
* La función debe **devolver** una lista de enteros; no debe imprimir nada.
