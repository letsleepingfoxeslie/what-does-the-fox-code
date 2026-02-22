import random

# Constants
OPERATORS = ["+", "-", "*"]
MIN_OPERAND, MAX_OPERAND = 2, 16
TOTAL_PROBLEMS = 5

def generate_problem() -> str:
    left, right = random.randint(MIN_OPERAND, MAX_OPERAND), random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = f"{left} {operator} {right}"
    answer = eval(expression)
    return expression, answer

for problem in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    while True:
        guess = input(f"Problem #{problem + 1}: {expression} = ")
        if guess == str(answer):
            break
        continue