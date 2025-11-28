# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 09:27:24 2025

@author: sirin
"""

def clean_data(df):
    df = df.dropna()
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    return df
