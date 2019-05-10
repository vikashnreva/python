c=int(input())
for i in range(c):
    a=tuple(map(int, input().split(" ")))
print(a)
print(hash(a))
