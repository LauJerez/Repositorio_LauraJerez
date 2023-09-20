a=[1,2,3,4]
b=['uno','dos','tres','cuatro']
x=zip(a,b)
m=list(x)
# print(m[0])

for idx, valor in enumerate(m):
    print(idx)
    print(valor)