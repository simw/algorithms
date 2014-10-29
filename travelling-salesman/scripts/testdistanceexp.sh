#! /bin/sh

PROG="python main.py"
DATA="data/sample.tsp"
ALGO="5"
OPTS="output=simple;graph=false;n=1000"

# echo "exponent,distance"

for i in {12..40..4};
do
    FULLOPTS="\"$OPTS;dexp=$i;dnorm=100\""
    for count in {1..5};
    do
        out="$($PROG $ALGO $DATA $FULLOPTS)"
        echo "$i,$out"
    done
done
