import stemgraphic
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import *

def stem(_value:list, _scale:int):
    stemgraphic.stem_graphic(_value, scale=_scale)

def table(_value:list):
    pd.Series(_value).value_counts()
    return pd.Series(_value).value_counts()

def hist(_value:list, arange:int, color:str):
    bins = np.arange(arange) + 0.5
    hist, edges = np.histogram(_value, bins=bins)
    y = np.arange(1,hist.max()+1)
    x = np.arange(arange)
    X, Y = np.meshgrid(x, y)
    data = plt.scatter(X, Y, c=Y<=hist, cmap=f"{color}", )
    plt.grid()
    plt.show()
    return data
    
def freq(_data:list, _bins:list, labels:list):
    freq_table = {}
    for label in labels:
        freq_table[label] = 0

    for value in _data:
        for i in range(len(_bins)-1):
            if _bins[i] <= value < _bins[i+1]:
                freq_table[labels[i]] +=1
                break
    return freq_table

def freq_plot(_labels:list, _values:list, title:str, xlab:str, ylab:str, _line: bool = False, _line_color:str = 'red', _line_size:int = 7, _line_width:int = 5):
    x = np.arange(len(_labels))
    fig, ax1 = plt.subplots()
    ax1.plot(_labels, _values, '-s', color=f'{_line_color}', markersize=_line_size, linewidth=_line_width, alpha=0.7, label=f'{title}')
    ax1.set_xlabel(f'{xlab}')
    ax1.set_ylabel(f'{ylab}')
    ax1.tick_params(axis='both', direction='in')
    plt.bar(x, _values)
    plt.xticks(x, _labels)
    plt.show()