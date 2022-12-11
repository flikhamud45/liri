import itertools

money =  [20,20,20,10,10,10,10,10,5,5,1,1,1,1,1]
new_lst= []
for i in range(2, len(money)):
    for comb in itertools.combinations(money, i):
        if sum(comb) == 100:
            new_lst.append(comb)

print(set(new_lst))
