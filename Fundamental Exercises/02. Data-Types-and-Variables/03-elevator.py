n = int(input())
p = int(input())
if n % p == 0:
    print(int(n/p))
elif not n % p == 0:
    print (int(n/p + 1))