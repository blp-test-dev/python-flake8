# Indentation error (incorrect indentation)
def indentation_error():
    x = 5
    return x

# Unused variable
unused_variable = 42

# Variable shadowing
shadowed_variable = 10
def variable_shadowing(shadowed_variable):
    return shadowed_variable + 5

# Line length violation (exceeding 80 characters)
long_line = "This is a very long line of code that exceeds the maximum line length in Flake8. This is just to trigger the check."

# Missing docstring
def missing_docstring():
    pass

# Import order issue
import os
from math import sqrt
import sys

# Whitespace issues
whitespace_error   = 42
extra_whitespace   = "   too much whitespace   "
mixed_tabs_spaces  = "mixed\ttabs  and    spaces"

# Variable naming convention violation
VariableNamingViolation = "This variable name violates PEP 8"

# Code complexity (nested logic)
def complex_code():
    if True:
        for i in range(10):
            while True:
                pass

# Line continuation style
long_line_continuation = "This is a very long line " + \
    "split into multiple lines using backslashes for continuation."

# Hardcoded value
magic_number = 42

# Inconsistent whitespace
inconsistent_whitespace = "   Inconsistent   whitespace    "
