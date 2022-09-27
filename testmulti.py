import argparse
import json
from multiprocessing.dummy import freeze_support
import numpy as np
import os
import multiprocessing
import pickle
import sys
from tqdm import tqdm

def task1(x):
    return x+10

if __name__ == '__main__':
    #freeze_support()
    pool = multiprocessing.Pool(1)
    for x in tqdm(pool.imap_unordered(task1,[1,2,3,4]),total=4):
        print(x)

#from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     pool = multiprocessing.Pool(1)
#     # with Pool(5) as p:
#     #     print(p.map(f, [1, 2, 3]))
#     for x in tqdm(pool.imap_unordered(task1,[1,2,3,5,6]),total=4):
#         print(x)