import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = r"004-finance-tracker/finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    def __init__(self):
        pass

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = csv.COLUMNS)
            df.to_csv(cls.CSV_FILE, index = False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = { 
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


CSV.initialize_csv()
CSV.add_entry("20-02-2026", 262.15, "Income", "Salary")