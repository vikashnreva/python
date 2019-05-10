import random
class dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return (first,second)

d2=dice()
(x,y)=d2.roll()
print(f"{x},{y}")

