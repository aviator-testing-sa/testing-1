from typing import List, Dict, Any

# 1. Function return type mismatch
def add_numbers(a: int, b: int) -> int:
    print("A")
    return str(a + b)  # This should return an int but returns a str

# 2. Argument type mismatch
def greet(name: str) -> str:
    return f"Hello, {name}!"

greet(123)  # Passing an int instead of a str

# 3. Inconsistent list element types
my_list: List[int] = [1, 2, "three"]  # Mixing int and str in a List[int]

# 4. Key type mismatch in a dictionary
my_dict: Dict[str, int] = {
    "one": 1,
    2: "two"  # Mixing key types and value types
}

# 5. Variable type mismatch
age: int = "twenty-five"  # Assigning a string to an int variable

# 6. Missing type annotations
def process_data(data):  # No type annotations for arguments or return type
    return data * 2

# 7. Improper use of Any
def do_something(data: Any) -> int:
    return data + 1  # Assuming Any is always an int-like type

# 8. Incorrect use of Optional
from typing import Optional

def find_user(user_id: Optional[int]) -> str:
    if user_id is None:
        return "Anonymous"
    return user_id  # Returning an int where a str is expected

# 9. Invalid type operations
def combine_lists(lst1: List[int], lst2: List[str]) -> List[int]:
    return lst1 + lst2  # Combining List[int] and List[str]

# 10. Type hinting not matching actual usage
def divide(a: int, b: int) -> int:
    return a / b  # Should return a float, but return type is declared as int
