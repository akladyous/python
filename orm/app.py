# from typing import NewType

# T = NewType("T", str)
# user: T
# user = "John"


from typing import NewType
from mypy import checker

T = NewType("T", str)
user: T
user = "John"  # No error, 'user' is assigned a string value

# Uncomment the line below to see MyPy error
# user = 42  # Raises a MyPy error: "Incompatible types in assignment"

checker.check_file("<input>", globals())
