import stemgraphic
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import *
from scipy import stats

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
    
    return plt
    
def scatter(_x:list, _y:list, xlab:str=None, ylab:str=None):
    fig, ax1 = plt.subplots()
    ax1.scatter(_x, _y)
    return ax1

def pearson(_x:list, _y:list):
    val = stats.pearsonr(_x, _y)
    return val

def barplot(data1:list, data2:list, label:list, color:str, alpha:float, edgecolor:str):
    if(not (len(data1) == len(data2))):
        print("Error : 모든 데이터의 길이는 같아야 합니다.")
        return None
    if(len(label) >= 3):
        values = []
        re_values = []
        for i in range(len(data1)):
            xs = data1[i] + data2[i]
            values.append(xs)
        total = sum(data1) + sum(data2)
        for i in range(3):
            data = round((values[i] / total), 3)
            data = round((data * 100), 1)
            re_values.append(data)
        plt.rc('font', family='Malgun Gothic')
        plt.bar(label, re_values, color=f'{color}', alpha=alpha, edgecolor=f'{edgecolor}')
        plt.show()
        return plt
    else:
        thread = sum(data1), sum(data2)
        values = []
        for i in range(len(thread)):
            total = sum(thread)
            data = round((thread[i] / total), 3)
            data = round((data * 100), 1)
            values.append(data)
        plt.rc('font', family='Malgun Gothic')
        plt.bar(label, values, color=f'{color}', alpha=alpha, edgecolor=f'{edgecolor}')
        plt.show()
        return plt

    