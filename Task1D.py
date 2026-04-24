def inc(m:int) -> int:
    return m + 1                             # m = 3, return 4; m=4, return 5



def check(n:int) -> bool:
    return n > 2                             # n = 3, return T; n = 4, return T


answer = [inc(x) for x in range(5) if check(x)]   # answer = [4, 5]
print()