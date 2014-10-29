#! /bin/sh

PROG="python main.py"
DATA="data/sample.tsp"
ALGO="4"
OPTS="output=detailed;graph=true;base=random"

# echo "exponent,distance"
echo "n,distance"

for i in 100;
do
    for count in {1..100};
    do
        FULLOPTS="\"$OPTS;n=$i;filemod=$count\""
        out="$($PROG $ALGO $DATA $FULLOPTS)"
        echo "$i,$out"
    done
done

