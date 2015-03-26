t = int(raw_input())
s = ""
while t>0:
	t-=1
	n, m = map(int, raw_input().split())
	a = map(int, raw_input().split())
	while m>0:
		m-=1
		l, r = map(int, raw_input().split())
		for i in xrange(l-1, r):
			a[i]+=1
	for x in a:
		s += str(x)+" "
	print s