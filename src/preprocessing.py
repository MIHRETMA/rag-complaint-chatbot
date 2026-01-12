import pandas as pd
import numpy as np
import re
import string


def filtering_specific_products(df):
    target_products = [
    'Credit card', 
    'Personal loan', 
    'Savings account', 
    'Money transfers']

    # Filter the DataFrame
    filtered_df = df[df['Product'].isin(target_products)].copy()
    filtered_df = filtered_df[filtered_df['Consumer complaint narrative'].notnull()].copy() # filtering non-null values

    return filtered_df


def clean_narrative(text):

    if not isinstance(text, str):
        return ""
    
    # 1. Lowercasing
    text = text.lower()
        
    # 2. Special Characters & Punctuation Removal
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # 3. Remove Excessive Whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
