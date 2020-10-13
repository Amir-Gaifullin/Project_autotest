
A = input().split()
odd = 0
for i in range(len(A)):
    A[i] = int(A[i])
for i in range(len(A)):
    if ((A[i] % 2) != 0):
                odd = odd + 1
print(odd)
