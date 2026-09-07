#F(n)=F(n−1)+F(n−2)

def fib(num):
    if num == 0: return 0
    elif num == 1: return 1
    else:
        return fib(num-1) + fib(num-2)

lis = []
for i in range(20):
    lis.append(fib(i))

print(lis)