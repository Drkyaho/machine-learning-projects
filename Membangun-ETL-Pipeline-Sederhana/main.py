from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv

def main():
    print("=== Mulai proses ETL ===")
    df = extract_data()
    print(f"Data mentah: {len(df)} baris")

    if df.empty:
        print("Data kosong! Periksa kembali struktur website.")
        return

    df_clean = transform_data(df)
    print(f"Data setelah transformasi: {len(df_clean)} baris")

    load_to_csv(df_clean)
    print("=== ETL selesai ===")

if __name__ == "__main__":
    main()
