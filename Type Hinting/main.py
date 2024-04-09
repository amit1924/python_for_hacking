def num(a: int, b: int) -> int:
    print(f"sum={a+b}")


num(50, 40)


# Optional Types
from typing import Optional


def greeting(name: Optional[str]) -> str:
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")


greet1 = greeting("Alice")
greet2 = greeting(None)
