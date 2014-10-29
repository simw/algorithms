#! /bin/sh

PROG="python main.py"
DATA="$1"
OPTS="\"output=simple;graph=true;n=1\""

echo "algorithm,distance"

for i in {1..6};
do
    for count in {1..10};
    do
        out="$($PROG $i $DATA $OPTS)"
        echo "$i,$out"
    done
done
