while True:
	try:
		P,Q= raw_input().split()
		P=int(P)
		Q=int(Q)
		break
	except:
		print("Invalidinput")
		break
R=1
for x in range(Q):
	R=R*P
print(R)
