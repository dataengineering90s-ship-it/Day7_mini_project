# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 09:31:39 2025

@author: sirin
"""

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_db(df, table_name="sales"):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    db = os.getenv("DB_NAME")

    engine = create_engine(f"postgresql://{user}:{password}@{host}/{db}")

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print("Loaded successfully!")
