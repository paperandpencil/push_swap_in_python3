'''
push swap checker, implemented in Python 3, by jsu

Accepts from the commandline, a list of arguments
If arguments are NOT integers or are duplicates, error & exit

Otherwise, integer arguments will be loaded into stak_A

Accepts from stdin a list of, zero to n, 'push swap' instructions
Execute the 'push swap' instructions

After executing the instructions:
outputs 'OK', if integers are sorted in stak_A, and stak_B is empty
outputs 'KO', otherwise

eg.
python3 ./checker.py 4 1 2 3 // ra, for 'OK'
python3 ./checker.py 4 5 6 1 2 // rra, rra, for 'OK'
'''
import sys
import push_swap_ops as pso

def pushswap(instruction):
	if instruction == 'sa':
		pso.sa(stak_A)
	elif instruction == 'sb':
		pso.sb(stak_B)
	elif instruction == 'ss':
		pso.ss(stak_A, stak_B)
	elif instruction == 'pa':
		pso.pa(stak_A, stak_B)
	elif instruction == 'pb':
		pso.pb(stak_A, stak_B)
	elif instruction == 'ra':
		pso.ra(stak_A)
	elif instruction == 'rb':
		pso.rb(stak_B)
	elif instruction == 'rr':
		pso.rr(stak_A, stak_B)
	elif instruction == 'rra':
		pso.rra(stak_A)
	elif instruction == 'rrb':
		pso.rrb(stak_B)
	elif instruction == 'rrr':
		pso.rrr(stak_A, stak_B)
	else:
		print('Error', file=sys.stderr)
		print('Invalid instruction', file=sys.stderr)
		exit()

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

if len(stak_A) == 0:
	exit()

line = []
while True:
	tmp = sys.stdin.readline()
	tmp = tmp.rstrip()
	if tmp == '':
		break
	else:
		pushswap(tmp)
		# uncomment, to see changes across staks for each instruction:
		#print(stak_A)
		#print(stak_B)

flag = 0
if stak_A == sorted(stak_A) and len(stak_B) == 0:
	flag = 1
	
if flag == 1:
	print('OK')
else:
	print('KO')
