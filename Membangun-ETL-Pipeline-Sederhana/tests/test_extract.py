import sys
import os

# Tambahkan path ke Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import patch, Mock
from utils.extract import scrape_page, extract_data
import requests
from bs4 import BeautifulSoup

def test_scrape_page_success():
    # Mock HTML response
    mock_html = """
    <html>
        <div class="collection-card">
            <h3 class="product-title">Test Product</h3>
            <span class="price">$10.99</span>
            <div class="product-details">
                <p>Rating: ⭐ 4.5/5</p>
                <p>2 Colors</p>
                <p>Size: M</p>
                <p>Gender: Male</p>
            </div>
        </div>
    </html>
    """
    
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response
        
        result = scrape_page(1)
        
        assert len(result) == 1
        assert result[0]['Title'] == "Test Product"
        assert result[0]['Price'] == "$10.99"

def test_scrape_page_failure():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Error")
        
        result = scrape_page(1)
        
        assert len(result) == 0

def test_extract_data():
    with patch('utils.extract.scrape_page') as mock_scrape:
        mock_scrape.return_value = [{'Title': 'Test'}]
        
        df = extract_data()
        
        assert len(df) == 50  # Because we're scraping 50 pages