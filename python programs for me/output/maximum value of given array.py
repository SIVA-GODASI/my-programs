
a = [4,5,6,1,2,3,4]

max_value = a[0]

for i in range (1,len(a)):

    if a[i] > max_value:
        max_value = a[i]

print(max_value)
