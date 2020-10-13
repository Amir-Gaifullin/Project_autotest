
A = input().split()
y = 0
for i in range(len(A)):
    A[i] = int(A[i])
for i in range(len(A) // 2):
    if (i % 2 == 0):
        x = A[i]
        even = 0
        while x > 0:
            if (x % 2 == 0):
                even += 1
            x = x // 10
        if (even == 0):
            y = y + 1
if (y > 0):
    print('yes')
else:
    print('no')
