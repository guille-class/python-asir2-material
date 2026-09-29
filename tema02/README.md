# Tema 2 · Conceptos básicos de la programación general

[← Volver al índice](../README.md)

## ¿Dónde programar?

Un **editor de código** (VS Code, Sublime Text, Notepad++) es ligero y admite muchos lenguajes mediante extensiones. Un **IDE** (Visual Studio, Eclipse, PyCharm) añade depurador, compilación y pruebas, a costa de consumir más recursos. En este curso usaremos **VS Code** (o Codespaces, que es VS Code en el navegador) y, más adelante, Jupyter.

## Flujo, comentarios e indentación

- **Flujo**: el orden en que se ejecutan las líneas. Por defecto es **secuencial**, de arriba abajo.
- **Comentarios**: texto que el programa ignora y que sirve para explicar el código. En Python empiezan por `#`.
- **Indentación** (sangría): organiza el código en bloques.

> **Importante en Python:** la indentación es **obligatoria**. Si está mal, el programa da error y no se ejecuta. Usa siempre 4 espacios.

## Tipos de datos

| Categoría | Tipo | En Python | Ejemplo |
|---|---|---|---|
| Numéricos | Entero | `int` | `42`, `-7`, `0` |
| Numéricos | Decimal | `float` | `3.14`, `-0.001` |
| Texto | Carácter | `str` de una letra | `'A'`, `'1'` |
| Texto | Cadena | `str` | `'Hola, mundo!'` |
| Booleanos | Verdadero / Falso | `bool` | `True`, `False` |

En Python los decimales se escriben con **punto** (`37.5`), nunca con coma.

## Constantes y variables

Ambas guardan un dato en memoria con un nombre. Una **variable** puede cambiar de valor; una **constante**, no.

```python
mi_variable = 10        # el valor puede cambiar
MI_CONSTANTE = 3.1416   # convención: constantes en MAYÚSCULAS
```

Reglas de nombrado:

- Empiezan siempre por una letra, nunca por un número.
- Constantes en `MAYÚSCULAS`; variables en minúsculas.
- Palabras separadas con `_`; sin espacios, tildes, `ñ` ni `ç`.
- Nombre único y que no sea una palabra reservada (`if`, `for`, `print`...).
- El nombre explica el valor: `precio_total` mejor que `x`.

## Operadores

| Tipo | Símbolos | Uso |
|---|---|---|
| Asignación | `=` | Guarda un valor en una variable |
| Aritméticos | `+ - * / %` | Suma, resta, multiplicación, división y **módulo** (resto de la división) |
| Relacionales | `> >= < <= == !=` | Comparan dos valores; devuelven `True` o `False` |
| Lógicos | `and`, `or`, `not` | Combinan condiciones |

Cuidado: `=` asigna y `==` compara.

## Ejemplos

- [`ejemplos/gastos.py`](ejemplos/gastos.py): calculadora de gastos mensuales (caso práctico 1 del libro).
- [`ejemplos/acceso.py`](ejemplos/acceso.py): control de acceso (caso práctico 2 del libro).

## Enlace de interés

- [Ranking de editores e IDE más populares](https://pypl.github.io/IDE.html)
