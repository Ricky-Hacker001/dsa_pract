array=['z','x','c','v','b','a']
array_count=len(array)

for i in range(array_count-1):
    for j in range(array_count-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]

print(array)