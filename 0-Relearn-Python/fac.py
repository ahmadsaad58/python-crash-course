# factorial 

def fac(n):
	if n == 0: 
		return 1
	if n == 1:
		return 1
	if n == 2: 
		return 2
	if n == 3: 
		return 6
	
	return n * fac(n - 1)

def memo(func):
	memo = {}

	def use_memo(n):
		try:
			return memo[n]
		except:
			memo[n] = func(n)
			return memo[n]
	
	return use_memo

@memo
def fac_memo(n):
	base = {0: 1, 1: 1, 2: 2, 3: 6}
	try: 
		return base[n]
	except:
		return n * fac(n - 1)

print([fac_memo(n) for n in range(10)])