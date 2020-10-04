
c1 = input()
n_0 = ord('0')
n_9 = ord('9')
i = n_0
count = 0
while i <= n_9:
    if i == ord(c1):
        break
    else:
        i += 1
        count += 1
print(count + 10)
