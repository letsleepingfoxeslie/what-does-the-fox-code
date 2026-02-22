import random

# Constants
OPERATORS = ["+", "-", "*"]
MIN_OPERAND, MAX_OPERAND = 2, 16

def generate_problem():
    left, right = random.randint(MIN_OPERAND, MAX_OPERAND), random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = f"{left} {operator} {right}"
    return expression

print(generate_problem())