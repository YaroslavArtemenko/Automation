import random
a = [1,2,3,4,5,'A',None]
q = [[[random.choice(a) for i in range(3)] for j in range(3)] for k in range(3)]

q.append([[1,1], [1,1,1]])
print(q)