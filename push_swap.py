'''
push swap, implemented in Python 3, by jsu

Accepts from the commandline, a list of arguments
If arguments are NOT integers or are duplicates, error & exit

Otherwise, integer arguments will be loaded into stak_A

Implement an algorithm that employs 'push swap' operations (eg. ra, sa, pa, pb etc.) such that:
-> integers are sorted in stak_A, and 
-> stak_B is empty 

Print sequence of 'push swap' operations, to stdout

An algorithm that emits fewer instructions, is preferred

eg.
python3 ./push_swap.py 4 1 2 3 
1 instruction sequence, ra, is preferred, 
vs. 
3 instruction sequence, rra, rra, rra

NOTE. both sequences will lead to 'OK' with checker
eg.
python3 ./push_swap.py 4 1 2 3 | python3 ./checker.py 4 1 2 3

OR

ARG=$(shuf -i 1-9999 -n 100 | tr '\n' ' ');
python3 ./push_swap.py $ARG | python3 ./checker.py $ARG
'''

import sys
import push_swap_ops as pso

stak_A = []
stak_B = []

n = len(sys.argv) - 1

# screen for NON integer inputs
for i in range(n):
	try:
		stak_A.append(int(sys.argv[i + 1]))
	except:
		print('Error', file=sys.stderr)
		print('at least one argument is NOT an integer', file=sys.stderr)
		exit()

# screen for duplicate values in input
checked = []
for i in range(n):
	if stak_A[i] in checked:
		print('Error', file=sys.stderr)
		print('at least one argument is a duplicate of another')
		exit()
	checked.append(stak_A[i])

def print_staks(stak_A, stak_B):
	print(stak_A)
	print(stak_B)	

def min_to_top(stak_A):
	while stak_A.index(min(stak_A)) != 0:
		if stak_A.index(min(stak_A)) == 0:
			break
		elif stak_A.index(min(stak_A)) >= len(stak_A) / 2:
			pso.rra(stak_A)
			print('rra')
		else:
			pso.ra(stak_A)
			print('ra')
		#print(stak_A)
		#print(stak_B)

def algo_v1(stak_A, stak_B):
	if stak_A == sorted(stak_A):
		#print('stak_A is already sorted')
		exit()
	while len(stak_A) > 0:
		min_to_top(stak_A)
		pso.pb(stak_A, stak_B)
		print('pb')
	while len(stak_B) > 0:
		pso.pa(stak_A, stak_B)
		print('pa')

# algo_v2 ???
# https://en.wikipedia.org/wiki/Merge-insertion_sort



def main():
	#print_staks(stak_A, stak_B)
	algo_v1(stak_A, stak_B)
	#print_staks(stak_A, stak_B)
	
if __name__ == "__main__":
	main()
