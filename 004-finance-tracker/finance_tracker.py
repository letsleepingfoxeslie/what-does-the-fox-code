import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt
class CSV:
    CSV_FILE: str = r"004-finance-tracker/finance_data.csv"
    COLUMNS: list[str] = ["date", "amount", "category", "description"]
    DATE_FORMAT: str = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls) -> None:
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = csv.COLUMNS)
            df.to_csv(cls.CSV_FILE, index = False)

    @classmethod
    def add_entry(cls, date, amount, category, description) -> None:

        # Might make a class for this specifically?
        new_entry: dict = { 
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        # Context manager, avoids memory leaks
        with open(cls.CSV_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames = cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date) -> None | pd.DataFrame:
        df: pd.DataFrame = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format = CSV.DATE_FORMAT)

        # It will be a string, so we have to convert to a datetime
        start_date: datetime = datetime.strptime(start_date, CSV.DATE_FORMAT)
        end_date: datetime = datetime.strptime(end_date, CSV.DATE_FORMAT)

        # Filters between start_date and end_date
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        
        # Matches everything in out dataframe where indexes of mask match
        filtered_dataframe: pd.DataFrame = df.loc[mask]

        if filtered_dataframe.empty:
            print("No transactions found in the given data range!")
        else:
            print(f"Transactions from {start_date.strftime(CSV.DATE_FORMAT)} to {end_date.strftime(CSV.DATE_FORMAT)}: ")
            print(filtered_dataframe.to_string(index = False, formatters = { "date": lambda x: x.strftime(CSV.DATE_FORMAT)}))


        # There's a condition to check against. Syntax is messy like the future
        total_income = filtered_dataframe[filtered_dataframe["category"] == "Income"]["amount"].sum()
        total_expenses = filtered_dataframe[filtered_dataframe["category"] == "Expense"]["amount"].sum()
        print("\nSummary: ")
        print(f"Total income: +${total_income:.2f}")
        print(f"Total expenses: -${total_expenses:.2f}")
        print(f"Net savings: ${(total_income - total_expenses):.2f}")

        # TODO: for later!
        return filtered_dataframe

def prompt_entry() -> None:
    CSV.initialize_csv()
    date = get_date("Enter the date (format: dd-mm-yyyy) or press [ENTER] for today's date: ", allow_default = True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)

def plot_transactions(df: pd.DataFrame):
    df.set_index("date", inplace = True)

    # Fills in the missing days and fills them with zero
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value = 0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value = 0)

    plt.figure(figsize = (10, 5))
    plt.plot(income_df.index, income_df["amount"], label = "Income", color = "g")
    plt.plot(expense_df.index, expense_df["amount"], label = "Expense", color = "r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and expenses over time")
    plt.legend() # For labels
    plt.grid(True) 
    plt.show()

def main():
    while True:
        print("[1] Add a new transaction")
        print("[2] View transactions and summary within a date range")
        print("[3] Exit")
        choice: str = input("Enter your choice: ")

        match choice:
            case "1":
                prompt_entry()
            case "2":
                start_date: str = get_date("Enter the start date (dd-mm-yyyy): ")
                end_date: str = get_date("Enter the end date (dd-mm-yyyy) or [ENTER] for today: ", allow_default = True)
                df: pd.DataFrame = CSV.get_transactions(start_date, end_date)

                if input("Do you want to see a plot? (Y/N) ").lower() == "y":
                    plot_transactions(df)

            case "3":
                print("Exiting!")
                exit()
            case _:
                print("Invalid choice")
                continue


if __name__ == "__main__":
    main()

# CSV.get_transactions("01-01-2020", "01-01-2027")
# CSV.add_entry("20-02-2026", 262.15, "Income", "Salary")