import numpy as np
import os
import os
from glob import glob
import pandas.util
import xxhash
import pandas as pd
import os
import time
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from pandas.core.frame import DataFrame
import numpy as np
import os
import os
from glob import glob
import pandas.util
import xxhash
import pandas as pd
import os
import time
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from pandas.core.frame import DataFrame

def extracted_cell(train: DataFrame, train_text_df: DataFrame) -> DataFrame:
    """
Params:
train: pandas.DataFrame:
          Rows:   Integer
          Columns:   - id: string
                         - Typical length: 12 (avg)
                      - discourse_id: integer
                      - discourse_start: integer
                      - discourse_end: integer
                      - discourse_text: string
                         - Typical length: 240 (avg)
                      - discourse_type: string
                         - Typical length: 7 (avg)
                      - discourse_type_num: string
                         - Typical length: 9 (avg)
                      - predictionstring: string
                         - Typical length: 161 (avg)
                      - discourse_len: integer
                      - pred_len: integer
                      - discourse_nr: integer
                      - essay_len: integer
                      - essay_words: integer
                      - gap_length: float
                      - gap_end_length: float
train_text_df: pandas.DataFrame:
                  Rows:   Integer
                  Columns:   - id: string
                                 - Typical length: 12 (avg)
                              - text: string
                                 - Typical length: 2364 (avg)

Returns:
pandas.DataFrame:
   Rows:   Integer
   Columns:   - id: string
                  - Typical length: 12 (avg)
               - text: string
                  - Typical length: 2364 (avg)
               - entities: list of str
"""

    def apply_func(row, train):
        total = len(row['text'].split())
        entities = ['O'] * total
        discourse_id = row['id']
        train_df_id = train.query('id == @discourse_id').reset_index(drop=True)
        for j in range(len(train_df_id)):
            discourse = train_df_id.loc[j, 'discourse_type']
            list_ix = [int(x) for x in train_df_id.loc[j, 'predictionstring'].split(' ')]
            entities[list_ix[0]] = f'B-{discourse}'
            entities_str = f'I-{discourse}'
            for k in list_ix[1:]:
                entities[k] = entities_str
        return entities
    train_text_df['entities'] = train_text_df.apply(lambda row: apply_func(row, train), axis=1)
    return train_text_df
