# 06 - py_palindrome_partitioner

**Fichero a entregar:** `solution.py`
**Funciones permitidas:** Ninguna

## Enunciado

Escribe una función que calcule el **mínimo número de cortes** necesarios para dividir una cadena en subcadenas palíndromas.

La función debe:

* Recibir una cadena `s`.
* Devolver el número mínimo de cortes para que **cada fragmento sea un palíndromo**.
* Una cadena vacía o de un solo carácter requiere `0` cortes.

## Prototipo

```python id="ejjktj"
def palindrome_partitioner(s: str) -> int:
```

## Ejemplos

```python id="8vcddc"
palindrome_partitioner("aab")
# 1
# aa | b
```

```python id="1xkevl"
palindrome_partitioner("racecar")
# 0
```

```python id="odg30m"
palindrome_partitioner("abcbm")
# 2
# a | bcb | m
```

```python id="cdbfgv"
palindrome_partitioner("a")
# 0
```

```python id="kbvs5u"
palindrome_partitioner("")
# 0
```

## Casos borde

* La cadena puede estar vacía.
* Un palíndromo completo devuelve `0`.
* La función debe **devolver** un entero; no debe imprimir nada.
