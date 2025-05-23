array=[1,0,19,2,20,0]
array_count=len(array)

for i in range(array_count-1):
    for j in range(array_count-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]

print(array)