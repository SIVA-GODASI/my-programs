
a = [1,2,1,1,1,2,3,4,5,5]

dict = {}
for i in a:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print(dict)
