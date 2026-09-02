import sys
import os

# Tambahkan path ke Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
import numpy as np
from utils.transform import transform_data, clean_price, clean_rating

def test_clean_price():
    assert clean_price("$10.99") == 175840
    assert clean_price("Price Unavailable") is None
    assert clean_price("Invalid") is None

def test_clean_rating():
    assert clean_rating("4.5/5") == 4.5
    assert clean_rating("Invalid Rating / 5") is None
    assert clean_rating("Not Rated") is None

def test_transform_data():
    test_data = {
        'Title': ['Product 1', 'Product 1', 'Unknown Product'],
        'Price': ['$10', 'Price Unavailable', '$20'],
        'Rating': ['4/5', 'Invalid Rating / 5', '3/5'],
        'Colors': ['2 Colors', '3 Colors', '1 Colors'],
        'Size': ['Size: M', 'Size: L', 'Size: S'],
        'Gender': ['Gender: Male', 'Gender: Female', 'Gender: Unisex']
    }
    df = pd.DataFrame(test_data)
    
    transformed = transform_data(df)
    
    assert len(transformed) == 1  # After cleaning
    assert transformed['Price'].iloc[0] == 160000
    assert transformed['Rating'].iloc[0] == 4.0