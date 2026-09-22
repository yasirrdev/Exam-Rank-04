# 07 - py_sliding_window_maximum

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna

## Enunciado

Escribe una función que devuelva el valor máximo de cada ventana deslizante de tamaño `k` sobre una lista de enteros.

La función debe:

* Recibir una lista de enteros `nums`.
* Recibir un entero `k` que representa el tamaño de la ventana.
* Desplazar la ventana una posición hacia la derecha en cada paso.
* Devolver una lista con el máximo de cada ventana.
* Si `nums` está vacía, `k <= 0` o `k` es mayor que la longitud de la lista, devolver una lista vacía.

## Prototipo

```python id="lckcpd"
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
```

## Ejemplos

```python id="lfj98l"
sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3)
# [3,3,5,5,6,7]
```

```python id="kktn5k"
sliding_window_maximum([9, 5, 2, 8], 2)
# [9,5,8]
```

```python id="lxb1lq"
sliding_window_maximum([4, 1], 1)
# [4,1]
```

```python id="w4ptqe"
sliding_window_maximum([], 3)
# []
```

```python id="f6ocie"
sliding_window_maximum([1,2,3], 5)
# []
```

## Casos borde

* `nums` puede estar vacía.
* `k` puede ser `1`.
* Si `k` es inválido, devolver `[]`.
* La función debe **devolver** una lista de enteros; no debe imprimir nada.
