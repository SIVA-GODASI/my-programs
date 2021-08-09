
def noiseven(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

print("enter the numbe")
input = int(input())
ans = noiseven(input)
print(ans)