# type: ignore
# fmt: off
"""
This file contains a series of attempts to create objects that are tuples with 0, 1, or 2 members.

typing is set to ignore all of this file since some of these do not work (on purpose)
"""

# Empty attempts
a = ()
b = tuple()
c = ,
d = (,)
e = tuple(,)
# Single item attempts
f = "sauron"
g = ("gollum")
h = tuple("frodo")
i = "legolas", 
j = ("gandalf",)
k = tuple("bilbo", )
# Two item attempts
l = "pippin", "arwen"
m = ("aragorn", "gimli")
n = tuple("samwise", "sarumon")
o = "merry", "boromir",
p = ("faramir", "treebeard",)
q = tuple("elrond", "galadriel",)