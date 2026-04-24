def square(n:int) -> int:
    return n * n # n=1, returns 1, n=2, returns 4, n=3,returns 9, n=4, returns 16

squares = [square(x) for x in [1,2,3,4]] #squares= [1, 4, 9, 16]
print() #squares is a collection of return values in order collected