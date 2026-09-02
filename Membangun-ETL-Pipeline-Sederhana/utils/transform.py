import pandas as pd

def clean_price(price_str):
    if not price_str or 'Price Unavailable' in price_str:
        return None
    try:
        price_float = float(price_str.replace('$', '').strip())
        # konversi ke IDR
        return int(price_float * 16000)
    except:
        return None

def clean_rating(rating_str):
    if not rating_str or rating_str in ['Invalid Rating / 5', 'Not Rated']:
        return None
    try:
        # misal "4.5 / 5"
        return float(rating_str.split('/')[0].strip())
    except:
        return None

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # 1) Hapus duplikat mentah
    df = df.drop_duplicates()

    # 2) Filter Title yang valid
    df = df[df['Title'].notna() & (df['Title'] != 'Unknown Product')]

    # 3) Bersihkan Price & Rating
    df['Price']  = df['Price'] .apply(clean_price)
    df['Rating'] = df['Rating'].apply(clean_rating)

    # 4) Buang baris tanpa Price/Rating valid
    df = df[df['Price'].notna() & df['Rating'].notna()]

    # 5) Ekstrak angka dari kolom Colors, ubah ke integer
    #    misal "3 Colors" → 3
    df['Colors'] = (
        df['Colors']
        .str.extract(r'(\d+)', expand=False)
        .astype(float)   # intermediate untuk mengizinkan NaN
        .dropna()        # buang yang gagal ekstrak angka
        .astype(int)
    )
    # setelah .dropna(), index-nya terpotong → reset index
    df = df.reset_index(drop=True)

    # 6) Bersihkan Size & Gender dengan menghapus prefix
    df['Size']   = df['Size'] .str.replace(r'^Size:\s*',   '', regex=True)
    df['Gender'] = df['Gender'].str.replace(r'^Gender:\s*', '', regex=True)

    # 7) Buang baris yang masih punya missing di kolom inti
    df = df.dropna(subset=['Size', 'Gender'])

    return df

if __name__ == "__main__":
    # contoh pemakaian:
    df_raw = pd.read_csv("products_raw.csv")  # dari extract.py
    df_clean = transform_data(df_raw)
    print(f"Data setelah transformasi: {len(df_clean)} baris")
    df_clean.to_csv("products.csv", index=False)
