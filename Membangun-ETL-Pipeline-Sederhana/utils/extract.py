import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def scrape_page(page_number):
    # Atur URL berdasarkan nomor halaman
    if page_number == 1:
        url = "https://fashion-studio.dicoding.dev/"
    else:
        url = f"https://fashion-studio.dicoding.dev/page{page_number}"

    print(f"[DEBUG] Scraping URL: {url}")

    try:
        # Panggil requests.get di dalam try agar pengecualian tertangani
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.select('.collection-card')

        data = []
        for p in products:
            title_tag   = p.select_one('h3.product-title')
            price_tag   = p.select_one('span.price')
            detail_tags = p.select('.product-details p')

            # Ambil semua elemen, jika tidak ada -> None
            title  = title_tag.text.strip() if title_tag   else None
            price  = price_tag.text.strip() if price_tag   else None
            rating = detail_tags[0].text.strip().replace("Rating: ⭐ ", "") if len(detail_tags) > 0 else None
            colors = detail_tags[1].text.strip() if len(detail_tags) > 1 else None
            size   = detail_tags[2].text.strip() if len(detail_tags) > 2 else None
            gender = detail_tags[3].text.strip() if len(detail_tags) > 3 else None

            data.append({
                'Title':     title,
                'Price':     price,
                'Rating':    rating,
                'Colors':    colors,
                'Size':      size,
                'Gender':    gender,
                'Timestamp': datetime.now().isoformat()
            })

        return data

    except requests.exceptions.RequestException as e:
        # Tangani error GET maupun status
        print(f"Gagal scraping halaman {page_number}: {e}")
        return []


def extract_data(max_pages=50):
    all_data = []
    for page in range(1, max_pages + 1):
        print(f"-- Page {page}")
        all_data.extend(scrape_page(page))
    return pd.DataFrame(all_data)


if __name__ == "__main__":
    df = extract_data()
    print(df.head())
    df.to_csv("products_raw.csv", index=False)
