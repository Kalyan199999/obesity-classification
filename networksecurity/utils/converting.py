import os ,sys
import numpy as np
import pandas as pd
from typing import List
import pickle

from networksecurity.exception.exception import NetworkSecurityException

def convert_target(value):
    if( value == 'Obesity_Type_I' or  value == 'Obesity_Type_II' or value == 'Obesity_Type_III'):
        return 'yes'
    return 'no'

def convert_lower(value):
    """Convert a string to lowercase if it's a string."""
    value = value.strip()
    if isinstance(value, str):
        return value.lower()
    return value

def convert_cat_col_lower(X: pd.DataFrame, cat_cols: List[str]):
    """
    Converts all categorical column values in `cat_cols` to lowercase.

    Parameters:
        X (pd.DataFrame): Input dataframe.
        cat_cols (List[str]): List of categorical column names.

    Returns:
        pd.DataFrame: DataFrame with lowercase categorical values.
    """
    for col in cat_cols:
        X[col] = X[col].apply(convert_lower)

    return X


# save the objects
def save_object( file_path:str , obj:str  ):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)

        with open(file=file_path, mode='wb') as file:
            pickle.dump(obj, file)

    except Exception as e:
        raise NetworkSecurityException(e)
    
def load_object():
    pass