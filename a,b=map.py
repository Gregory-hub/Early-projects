a,b=map(int,input().split())
k=31*(a-1)+b
if a==2 and b>28 or a==4 and b>30 or a==6 and b>30 or a==9 and b>30 or a==11 and b>30 or a>12 or a<1 or b>31 or b<1 :
	print("-1")
elif a<=2:
	print(365-k)
elif a>2:
	k=k-2-int(a/2.3)
	print(365-k)
	