chemlib
----------------

A lightweight Python library for chemistry.

Currently supports only basic lookups from the builtin periodic table.

Examples:
```
import chemlib

element = "C"
mm = chemlib.getMolarMass(element)
name = chemlib.getName(element)
an = chemlib.getAtomicNumber(element)
print "{0} has a molar mass of {1} and atomic number of {2}".format(name, mm, an)
```
```
compound = "C6H12O6" # glucose
glucose = chemlib.Compound(compound)
print compound.getMolarMass()
```

Provided under the MIT License.