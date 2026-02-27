from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"} 

# Recursive function: will run until there's a valid input
def get_date(prompt: str, allow_default: bool = False) -> datetime:
    date_as_string = input(prompt)

    # Returns today if ENTER is iht
    if allow_default and not date_as_string:
        return datetime.today().strftime(DATE_FORMAT)
    
    # Validate date
    try:
        valid_date = datetime.strptime(date_as_string, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Invalid date format! Date must be in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount() -> float:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be non-negative non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category() -> str:
    category = input("Enter category ([I]ncome or [E]xpense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category! Enter either [I]ncome or [E]xpense")
    return get_category()

def get_description() -> str:
    return input("Enter description: ")