import stemgraphic
import pandas as pd
from statistics import *

def stem(_value:list, _scale:int):
    stemgraphic.stem_graphic(_value, scale=_scale)

def table(_value:list):
    pd.Series(_value).value_counts()
    return pd.Series(_value).value_counts()