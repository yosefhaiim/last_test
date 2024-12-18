import os
import pandas as pd
import numpy as np


DATA_PATH = os.path.join(os.path.dirname(__file__), '../data')

def load_csv(file_name):
    """
    טוען קובץ CSV ומחזיר DataFrame.
    """
    file_path = os.path.join(DATA_PATH, file_name)
    try:
        return pd.read_csv(file_path, encoding='latin1')
    except FileNotFoundError:
        print(f"Error: File {file_name} not found in {DATA_PATH}")
        return None


global_terror = load_csv("global_terror1000.csv")
rows_5000 = load_csv("5000_rows.csv")
