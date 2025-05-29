a = [3, 2, 1, 5, 6]
al = len(a)
for i in range(al - 1):
    for j in range(i + 1, al):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)
