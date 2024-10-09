#!/bin/bash

clear
now=$(date)

echo '###############################'
echo 'for push swap eval '
echo "$0 by @jsu "
echo $now
echo '###############################'
echo

echo '+++++++++++++++++++++++++++++++'
echo "sort $1" numbers
echo '+++++++++++++++++++++++++++++++'
arg=$(shuf -i 1-999 -n $1 | tr '\n' ' ')
echo "./push_swap $arg > quicktest.log" 
./push_swap $arg > quicktest.log
echo

echo "*** check with ./checker_linux ***"
echo "./push_swap $arg | ./checker_linux $arg"
./push_swap $arg | ./checker_linux $arg
echo

echo "*** check with python3 ./checker.py ***"
echo "./push_swap $arg | python3 ./checker.py $arg"
./push_swap $arg | python3 ./checker.py $arg

echo
echo "cat quicktest.log | wc -l"
cat quicktest.log | wc -l
