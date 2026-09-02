import sys
import os

# Tambahkan path ke Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
from utils.load import load_to_csv
import os

def test_load_to_csv(tmp_path):
    test_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    test_path = tmp_path / "test.csv"
    
    load_to_csv(test_df, test_path)
    
    assert os.path.exists(test_path)
    assert pd.read_csv(test_path).shape == (2, 2)