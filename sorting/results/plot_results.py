
from bokeh.plotting import *
from os.path import dirname, join

import pandas as pd
import math

results = [
    pd.read_csv(join(dirname(__file__), 'python2_results.csv')),
    pd.read_csv(join(dirname(__file__), 'python3_results.csv'))
]

output_file('results/python_results.html', title='python sorting test')
colormap = {'insertion_sort': 'red', 'merge_sort': 'green'}

for res in results:
    res['length'] = res['length'].map(lambda x: math.log(x, 2))
    res['time'] = res['time'].map(lambda x: math.log(x, 10))
    res['color'] = res['algorithm'].map(lambda x: colormap[x])

    scatter(res['length'], res['time'], color=res['color'], 
        fill_alpha=0.2, size=10)

show()
