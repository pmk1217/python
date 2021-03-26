l = [1, 2, 3, 4, 5]
print([i ** 2 for i in l])
t=("orange","apple","banana")
print([len(i) for i in t]) 
print("updated")
t=("orange","apple","banana")
print([i for i in t if len(i)>5])
L_1 = [3, 4, 5]
L_2 = [1.5, -0.5, 4]
print([x*y for x in L_1 for y in L_2])
