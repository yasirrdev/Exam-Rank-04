# 01 - py_constellation_mapper

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna

## Enunciado

Escribe una función que proyecte una constelación de estrellas en una cuadrícula y devuelva la representación visual como una lista de cadenas.

La función debe:

* Recibir una lista de coordenadas de estrellas como tuplas **(fila, columna)**.
* Recibir el tamaño de la cuadrícula `dim`.
* Devolver una lista de cadenas de tamaño `dim`.
* Representar las estrellas con `'*'` y las posiciones vacías con `'.'`.
* Considerar `(0, 0)` como la esquina superior izquierda.
* Ignorar las coordenadas fuera de los límites de la cuadrícula.
* Manejar coordenadas duplicadas (una estrella solo aparece una vez).

## Prototipo

```python
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
```

## Ejemplos

```python
constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
# ['*..', '.*.', '..*']
```

```python
constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)
# ['.*.', '***', '.*.']
```

```python
constellation_mapper([], 2)
# ['..', '..']
```

```python
constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)
# ['*.', '.*']
```

```python
constellation_mapper([(0, 0), (5, 5)], 3)
# ['*..', '...', '...']
```

```python
constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)
# ['...', '***', '...']
```

## Casos borde

* `stars` puede estar vacío.
* Puede haber coordenadas repetidas.
* Las coordenadas fuera de la cuadrícula deben ignorarse.
* La función debe **devolver** una lista de cadenas; no debe imprimir nada.
