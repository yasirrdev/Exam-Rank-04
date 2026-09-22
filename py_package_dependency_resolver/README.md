# 05 - py_package_dependency_resolver

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna

## Enunciado

Escribe una función que resuelva el orden correcto de instalación de un conjunto de paquetes con dependencias.

La función debe:

* Recibir un diccionario donde cada clave es un paquete y su valor es una lista de dependencias.
* Devolver una lista con el orden de instalación.
* Un paquete **siempre debe instalarse después de todas sus dependencias**.
* Si existe una dependencia que no aparece como clave en el diccionario, debe ignorarse.
* Si existe un ciclo de dependencias, la función debe devolver una lista vacía.

## Prototipo

```python
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
```

## Ejemplos

```python
package_dependency_resolver({
    "A": ["B"],
    "B": ["C"],
    "C": []
})
# ["C", "B", "A"]
```

```python
package_dependency_resolver({
    "app": ["core", "utils"],
    "core": [],
    "utils": []
})
# ["core", "utils", "app"]
```

```python
package_dependency_resolver({
    "A": ["B"],
    "B": ["A"]
})
# []
```

```python
package_dependency_resolver({})
# []
```

```python
package_dependency_resolver({
    "A": ["X"],
    "B": ["A"]
})
# ["A", "B"]
```

## Casos borde

* El diccionario puede estar vacío.
* Las dependencias inexistentes deben ignorarse.
* Si hay un ciclo, devolver `[]`.
* La función debe **devolver** una lista de cadenas; no debe imprimir nada.
