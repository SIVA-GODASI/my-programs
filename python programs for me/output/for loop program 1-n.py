
print("enter the number")

number = int(input())

for i in range (1,number+1):
    if(i%5==0 and i%3==0):
        print("fizz_fuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("fuzz")
    else:
        print(i)


    
