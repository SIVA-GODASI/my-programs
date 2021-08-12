a = {"bjp":3,"con":1,"aap":2}

#votes = a.values()
#print(votes)
#after this by using maximum value of given array problem used to solve the program or

winning_party = ""

maxvotes = 0

for key in a.keys():
    if maxvotes < a[key]:
        maxvotes = a[key]
        winning_party = key
print(winning_party)
