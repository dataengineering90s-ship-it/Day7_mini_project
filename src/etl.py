# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 09:32:38 2025

@author: sirin
"""

from src.extract import extract_data
from src.transform import clean_data
from src.load import load_to_db

def run_etl():
    df = extract_data("data/sales.csv")
    df_clean = clean_data(df)
    load_to_db(df_clean)

if __name__ == "__main__":
    run_etl()
