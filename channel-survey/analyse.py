#!/bin/env python3

import glob
import pandas as pd
import json
import pprint

import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt

from collections import defaultdict


def add_freq(e1, e2):
    for k in e2:
            e1[k] += len(e2[k])
    return e1


def analyse(files, results):
    for f in files:
        data = json.load(open(f))
        for e in data.values():
            try:
                freqs = e['channelsurvey']['survey']
            except:
                pass
            else:
                results = add_freq(results, freqs)
    return results


def run():
    files = sorted(glob.glob('*.json'))
    results = defaultdict(int)
    return analyse(files, results)


def plot(results):
    p_res = pd.Series(results)
    with plt.xkcd():
        ax = p_res.plot(kind='bar')
        fig = ax.get_figure()
        fig.savefig('./result.pdf')


if __name__ == '__main__':
    results = run()
    with open('./results.json', 'w') as out:
        json.dump(results, out)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(results)
    plot(results)
