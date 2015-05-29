def fib(n):
	recepie = bin(n)[3:]
    	v1, v2, v3 = 1, 1, 0
    	for rec in recepie:
    		calc = v2*v2
    		v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
    		if rec=='1':
    			v1, v2, v3 = v1+v2, v1, v2
    	return v2
     
n, q = map(int, raw_input().split())
while q>0:
	ans, l, r = map(int, raw_input().split())
	ser = []
	tsum = 0
	if ans==0:
		for k in range(l,r+1):
			ser.append(fib(k))
	else:
		for i in ser:
			tsum += i
	print tsum
	q-=1