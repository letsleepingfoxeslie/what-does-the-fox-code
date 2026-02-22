import random
import time

# Constants
OPERATORS = ["+", "-", "*"]
MIN_OPERAND, MAX_OPERAND = 2, 16
TOTAL_PROBLEMS = 5

def generate_problem() -> tuple[str, str]:
    left, right = random.randint(MIN_OPERAND, MAX_OPERAND), random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = f"{left} {operator} {right}"
    answer = eval(expression)
    return expression, answer


input("Press ENTER to start!")
start_time = time.time()
print("-" * 24)

for problem in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    while True:
        guess = input(f"Problem #{problem + 1}: {expression} = ")
        if guess == str(answer):
            break
        continue

end_time = time.time()
print("-" * 24)
print(f"Time taken: {end_time - start_time:.3f}s")