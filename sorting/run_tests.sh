#!/bin/env sh

echo 'Running python2'
python2 -m tests.timed_run > results/python2_results.csv

echo 'Running python3'
python3 -m tests.timed_run > results/python3_results.csv

echo 'Plotting ...'
python results/plot_results.py
