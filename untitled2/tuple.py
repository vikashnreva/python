n = int(input())
l = list()
integers = input().split()
for i in integers:
        l.append(int(i))
print(hash(tuple(l)))
