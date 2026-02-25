import pandas as pd

def analyze_tenders():
    df = pd.read_csv("tenders_sample.csv")
    # Приклад: аналіз за регіонами (гіпотеза №4 з нашого плану)
    if 'procuringEntity' in df.columns:
        print("Аналіз кількості тендерів за замовниками:")
        print(df['procuringEntity'].value_counts().head())

if __name__ == "__main__":
    analyze_tenders()