import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval
import numpy as np
import os
import os
import time
from pandas.core.frame import DataFrame
def extracted_cell(df2: DataFrame) -> DataFrame:
    """
Params:
df2: Rows: Single-level Index: Integer
     Columns: Single-level Index: ['budget: integer', 'genres: string', 'homepage: string', 'id: integer', 'keywords: string', 'original_language: string', 'original_title: string', 'overview: string', 'popularity: float', 'production_companies: string', 'production_countries: string', 'release_date: string', 'revenue: integer', 'runtime: float', 'spoken_languages: string', 'status: string', 'tagline: string', 'title: string', 'vote_average: float', 'vote_count: integer', 'tittle: string', 'cast: string', 'crew: string']

Returns:
Rows: Single-level Index: Integer
Columns: Single-level Index: ['budget: integer', 'genres: list of dict', 'homepage: string', 'id: integer', 'keywords: list of dict', 'original_language: string', 'original_title: string', 'overview: string', 'popularity: float', 'production_companies: string', 'production_countries: string', 'release_date: string', 'revenue: integer', 'runtime: float', 'spoken_languages: string', 'status: string', 'tagline: string', 'title: string', 'vote_average: float', 'vote_count: integer', 'tittle: string', 'cast: list of dict', 'crew: list of dict']
"""
    from ast import literal_eval
    features = ['cast', 'crew', 'keywords', 'genres']
    for feature in features:
        df2[feature] = df2[feature].apply(literal_eval)
    return df2