from collections import Counter
from AOCD1 import LEFT, RIGHT
c = Counter(RIGHT)
print(sum(i * c.get(i, 0) for i in LEFT))