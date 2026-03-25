def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", sub(5, 3))
    print("Multiplication:", mul(5, 3))
    print("Division:", div(10, 2))
