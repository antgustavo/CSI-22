def sum_to(n)->int:
    if(n == 0):
        return 0
    return n + sum_to(n-1)

print(sum_to(20))