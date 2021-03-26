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
L = [10, 25, 30]
IterL = filter(None, L)
for i in IterL:
     print("Item: {0}".format(i))
def GetBiggerThan20(i):
     return i > 20
print(list(filter(GetBiggerThan20, L)))
print(list(filter(lambda i: i>20, L)))
print(list(range(10))) # 종료값
print(list(range(5, 10))) # 시작값, 종료값
print(list(range(10, 0, -1))) # 시작값, 종료값, 증가값
print(list(range(10, 20, 2))) # 10부터 20까지 짝수
L = [1, 2, 3]
def Add10(i):
    return i+10
for i in map(Add10, L):
    print("Item: {0}".format(i))
X = [1, 2, 3]
Y = [2, 3, 4]
print(list(map(pow, X, Y))) 