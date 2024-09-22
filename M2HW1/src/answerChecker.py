# CTS 285
# M2HW1
# James Reynolds
# 09/21/2024

def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2

def subtract(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2

def multiply(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2

def divide(num1: int | float, num2: int | float) -> int | float | None:
    return num1 / num2

def range(guess: int | float, ans: int | float) -> str:
    if guess > ans:
        return "Answer too high"
    elif guess < ans:
        return "Answer too low"
    else:
        return None
    

