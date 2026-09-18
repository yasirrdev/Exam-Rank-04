# 01 - py_constellation_mapper

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna en especial

## Enunciado

Una constelación puede representarse mediante una lista de coordenadas `(x, y)` sobre una cuadrícula.

Escribe una función que genere una representación de la constelación utilizando `*` para las estrellas y `.` para las posiciones vacías.

* El origen `(0, 0)` corresponde a la esquina **superior izquierda**.
* La cuadrícula debe tener el **tamaño mínimo** necesario para contener todas las estrellas.
* Si la lista está vacía, la función debe devolver una lista vacía.
* Puedes asumir que todas las coordenadas son enteros mayores o iguales que `0`.

## Prototipo

```python
def constellation_mapper(stars: list[tuple[int, int]]) -> list[str]:
```

## Ejemplos

```python
constellation_mapper([(0, 0)])
# ["*"]
```

```python
constellation_mapper([(0, 0), (2, 1)])
# [
#   "*..",
#   "..*"
# ]
```

```python
constellation_mapper([(1, 1), (0, 2)])
# [
#   "..",
#   ".*",
#   "*."
# ]
```

```python
constellation_mapper([(2, 0), (0, 0), (1, 0)])
# [
#   "***"
# ]
```

```python
constellation_mapper([])
# []
```

## Nota

La función debe **devolver** una lista de cadenas. No debe imprimir el resultado.
