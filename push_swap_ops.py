def sa(stak_A):
	if len(stak_A) == 0 or len(stak_A) == 1:
		return
	else:
		temp = stak_A[0]
		stak_A[0] = stak_A[1]
		stak_A[1] = temp
		
def sb(stak_B):
	if len(stak_B) == 0 or len(stak_B) == 1:
		return
	else:
		temp = stak_B[0]
		stak_B[0] = stak_B[1]
		stak_B[1] = temp
		
def ss(stak_A, stak_B):
	sa(stak_A)
	sb(stak_B)

# move 1st ele from top of stak_B to top of stak_A
def pa(stak_A, stak_B):
	if (len(stak_B) == 0):
		return
	temp = stak_B[0]
	del stak_B[0]
	stak_A.insert(0, temp)
	
# move 1st ele from top of stak_A to top of stak_B
def pb(stak_A, stak_B):
	if (len(stak_A) == 0):
		return
	temp = stak_A[0]
	del stak_A[0]
	stak_B.insert(0, temp)

# move ele from top of stak_A, to the bottom of	
def ra(stak_A):
	if len(stak_A) < 2:
		return
	temp = stak_A[0]
	del stak_A[0]
	stak_A.append(temp)
	
# move ele from top of stak_A, to the bottom of	
def rb(stak_B):
	if len(stak_B) < 2:
		return
	temp = stak_B[0]
	del stak_B[0]
	stak_B.append(temp)
	
def rr(stak_A, stak_B):
	ra(stak_A)
	rb(stak_B)

# move ele from bottom of stak_A, to the top of	
def rra(stak_A):
	if len(stak_A) < 2:
		return
	temp = stak_A.pop(-1)
	stak_A.insert(0, temp)
	
# move ele from bottom of stak_B, to the top of	
def rrb(stak_B):
	if len(stak_B) < 2:
		return
	temp = stak_B.pop(-1)
	stak_B.insert(0, temp)

def rrr(stak_A, stak_B):
	rra(stak_A)
	rrb(stak_B)
