import pandas as pd

def check_quality(file_path):
    df = pd.read_csv(file_path)
    print("--- Перевірка пропущених значень ---")
    print(df.isnull().sum())
    print("\n--- Статистика числових полів ---")
    print(df.describe())

if __name__ == "__main__":
    check_quality("tenders_sample.csv")