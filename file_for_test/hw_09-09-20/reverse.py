
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
for i in range(- 1, - len(A) - 1, - 1):
    print(A[i], end=' ')
