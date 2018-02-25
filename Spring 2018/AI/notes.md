# Administrivia and Py Ingredients: Numbers, Strings, and Variables #

* Python can be run interactively (REPL)
* No semicolons

## Variables ##

* `x=3`

## Numbers ##

* `+`, `-`, `*`, `/`
* Defaults to floating point division, use `//` for integer division
* Math functions
  *  `import math`
  *  `math.sqrt(9)`

## Types ##

* Dynamically types
* The following are "simple" types; Python doesn't really have a notion of
    "primitive", because **everything** is an objet. Each type also names a
    conversion function.
  * `bool`
  * `int`
  * `float`
  * `str`

## Strings ##

* Single or double quotes
  * Each obviates escaping the other
  * REPL output includes quotes, print doesn't
  * Can have `"` inside `'` and vice versa
  * Escape other characters int eh usual way `\"`
* Three single or double quotes for multi-line strings
* `wiener` + `dog`
  * `+=` can also be useful
  * Doesn't automatically convert numbers
* `*` for duplication
* `[]` for access
  * Negative index from end
  * No special char type
  * Strings are immutable
* Slicing
  * `[start:]`
  * `[:end]`
  * `[start:end:step]`
    * Any of these can be left out or negative
    * `s[::-1]` returns a reversed version of `s`
* `len(s)`
* `s.split(separator)`
  *  Result is a list
  *  Whitespace if no separator is specified
* `separator.join(list)`
    

# Py Filling: Lists, Tuples, Dictionaries, and Sets #

## Lists ##

* Created with `[]`
* `list` takes 0 or 1 arguments
* Nesting
* Element access and slicing are same as with strings
* Lists are mutable
* `s.sort()` sorts `s` in place
* `sorted(s)` returns a sorted copy of `s`
* `s.copy()`, `list(s)`, and `s[:]` all make copies

## Tuples ##

* Immutable, so safer
* Reuse can save memory
* Use `()` instead of `[]`
* Tuple unpacking and packing
* Convert using `tuple()`

## Dictionaries ##

* Associate Keys with values
  * Aka map, hashmap, has, associative array
* `{1: 'one', 2: 'two'}`
* Convert a sequence of pairs using `dict()`
* Keys must be immutable
* No duplicate keys, duplicate values okay
* New values replace old

## Sets ##

* Like dictionaries without values
* Does not maintain order
* Create with `{}`
* Convert with `set()`
* `&` intersection
* `|` union
* `-` set difference
* `^` xor
* `<=` subset
* `<` proper subset
* `>=` super set

# Turing Test #

## Alan Turing 1912-1954 ##

* Important theory of computation
  * Mathematical model of cumputer (Turing machine)
    * Any "Turing-complete" computer can simulate time and memory), so they're all equivalent
  * Some problems are unsolvable
    * Halting problem
* Durring WWII, developed machine to break German codes Knighted (OBE), 1946

# Py Crust: Code Structures #

# Rational Agents #

# Py Boxes: Modules, Packages, and Programs #

# Uniform Search #

# Heuristic Search #

# Minimax Search #

# Monte Carlo Tree Search #

# NumPy #

# Matplotlib #

