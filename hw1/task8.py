m = int(input())
n = int(input())
k = int(input())
if (k % n == 0 or k % m == 0) and k < m * n:
    print('Yes')
else:
    print('No')
