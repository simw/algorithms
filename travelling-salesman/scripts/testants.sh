#! /bin/sh

PROG="python main.py"
DATA="data/sample.tsp"
ALGO="6"
OPTS="output=simple;graph=false;dexp=0;pexp=2;pdecay=0.99"

# echo "exponent,distance"
echo "n,distance"

for i in 1 5 10 50 100 500 1000 5000 10000;
do
    FULLOPTS="\"$OPTS;n=$i\""
    for count in {1..20};
    do
        out="$($PROG $ALGO $DATA $FULLOPTS)"
        echo "$i,$out"
    done
done

