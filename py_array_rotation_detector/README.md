# 03 - py_array_rotation_detector

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna

## Enunciado

Escribe una función que determine si una lista puede obtenerse mediante una rotación de otra lista.

La función debe:

* Recibir dos listas de enteros `a` y `b`.
* Devolver `True` si `b` es una rotación de `a`.
* Devolver `False` en cualquier otro caso.
* Dos listas vacías se consideran rotaciones entre sí.
* Si las listas tienen distinta longitud, el resultado es `False`.

Una rotación consiste en desplazar los elementos circularmente cualquier número de posiciones.

## Prototipo

```python
def array_rotation_detector(a: list[int], b: list[int]) -> bool:
```

## Ejemplos

```python
array_rotation_detector([1, 2, 3, 4], [3, 4, 1, 2])
# True
```

```python
array_rotation_detector([5, 6, 7], [7, 5, 6])
# True
```

```python
array_rotation_detector([1, 2, 3], [2, 1, 3])
# False
```

```python
array_rotation_detector([], [])
# True
```

```python
array_rotation_detector([1, 2], [1, 2, 3])
# False
```

## Casos borde

* Ambas listas pueden estar vacías.
* Las listas pueden contener elementos repetidos.
* La función debe **devolver** un booleano; no debe imprimir nada.
