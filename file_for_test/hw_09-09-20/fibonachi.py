
n = int(input())
n1 = 0
n2 = 1
n3 = 0
for i in range(n):
    n3 = n1 + n3
    n1 = n2
    n2 = n3
print(n3)
