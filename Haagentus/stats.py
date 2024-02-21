from math import comb
import math

def comb_test(n:int, N:int, k:int, error:int):
    p = comb(k, error) * comb(37, 4) / comb(N, n)
    return p

def std_error(n1:int, p1:float, n2:int, p2:float, mu:float):
    return math.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)

def z_score(cx:float, mu:float, sem:float):
    return (cx - mu) / sem

def sigma(n:float, p:float, alpha:float):
    return {'sigma':(n * p * (1 - p)) ** 0.5, 'mu':n * p}
