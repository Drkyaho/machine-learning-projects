import pandas as pd

def load_to_csv(df, filename='products.csv'):
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Gagal menyimpan ke CSV: {e}")
