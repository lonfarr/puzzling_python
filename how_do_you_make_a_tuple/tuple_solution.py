"""
This file breaks down the puzzle into how each solution
is parsed, the result, and possible typings that would be valid
"""

# Turn formatting off because black will actually help clarify some of
# the ambiguous statements that are below (eg: `("gollum")` -> `"gollum"``)
# fmt: off

# a and b are valid Python
# Evaluate to a tuple of `()`
# Some valid types would be `tuple[()]` or `tuple[str, ...]` or `tuple[int, ...]`
a: tuple[()] = ()             # => ()
b: tuple[str, ...] = tuple()  # => ()

# c, d, and e all result in Syntax Errors
# c = ,
# d = (,)
# e = tuple(,)

# f and g are valid Python
# Evaluate to string of values "sauron" and "gollum" respectively
# WARNING: This doesn't match our intention of being a tuple with one item
# The correct type is str
f: str = "sauron"     # => "sauron"
g: str = ("gollum")   # => "gollum"

# h and k are valid Python
# Evaluate to a tuple of each character in the string with values of
# ("f", "r", "o", "d", "o") and ("b", "i", "l", "b", "o") respectively
# WARNING: This doesn't match our intention of being a tuple with one item
# The correct type is tuple[str, ...]
# WARNING: tuple[str, str, str, str, str] is not valid as the tuple size is not
#     known until runtime, so `tuple` returns the general tuple[str, ...] type
h: tuple[str, ...] = tuple("frodo")   # => ("f", "r", "o", "d", "o")
k: tuple[str, ...] = tuple("bilbo",)  # => ("b", "i", "l", "b", "o")

# i and j are valid Python
# Evaluate to a tuple with values of ("legolas", ) and ("gandalf", ) respectively
# Valid types are `tuple[str, ...]` and `tuple[str]`
# NOTE: Unlike in h and k, the length can be determined before runtime as this is
#     a parsing problem based on commas, not iterating over a string, thus
#     `tuple[str]` is a valid type
i: tuple[str, ...] = "legolas",  # => ("legolas",)
j: tuple[str] = ("gandalf",)     # => ("gandalf",)

# l, m, o, and p are valid Python
# Evaluate to a tuple with values of ("pippin", "arwen"), ("aragorn", "gimli"),
# ("merry", "boromir") and ("faramir", "treebeard") respectively
# Valid types are `tuple[str, ...]` and `tuple[str, str]`
# NOTE: Unlike in h and k, the length can be determined before runtime as this is
#     a parsing problem based on commas, not iterating over a string, thus
#     `tuple[str, str]` is a valid type
l: tuple[str, ...] = "pippin", "arwen"         # => ("pippin", "arwen")
m: tuple[str, str] = ("aragorn", "gimli")      # => ("aragorn", "gimli")
o: tuple[str, ...] = "merry", "boromir",       # => ("merry", "boromir")
p: tuple[str, str] = ("faramir","treebeard",)  # => ("faramir","treebeard")

# n and q both result in TypeError exceptions
# Since the tuple expects one iterable item, two inputs is not valid
# n = tuple("samwise", "sarumon")
# q = tuple("elrond", "galadriel",)
