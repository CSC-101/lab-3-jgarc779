def check(n:int) -> bool:
    return n > 2 #n=0,return F; n=1, return F; n=2, return F; n=3, return T; n=4, return T
answer = [x for x in range(5) if check(x)]   #answer = [3,4]
print()