import argparse
import sys
import re

import pandas as pd
from datetime import datetime
import numpy as np

if __name__ == "__main__":
    # argument-parser
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), help='log-file', default=sys.stdin)
    args = parser.parse_args()


    dates = []
    counter = []

    for line in args.infile:

        t = line.rstrip().split(' ')
        dates.append(datetime.strptime(t[0], "%Y-%m-%d_%H:%M:%S"))
        counter.append(int(t[3]))

    df = pd.DataFrame()

    df['datetime'] = pd.to_datetime(dates)
    df = df.set_index('datetime')
    df['counter'] = counter

    print(df.head())
    df['delta'] = df['counter'] - df['counter'].shift(1)
    df = df.drop(columns=['counter'])

    print(df.head())
    print(df.tail())
    print(df.sum())

    res = df.groupby(df.index.hour).max()
    print(res)
    #print(res.sum())

    #res = df.resample('15Min').max() - df.resample('15Min').min()
    #print(res)


#counter    158491


