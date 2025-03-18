import random
import sys
sys.setrecursionlimit(100000)
def distribution(number):
    def _dist(num, accumulator):
        assert len(accumulator) == 11
        n = random.randint(1,6) + random.randint(1,6) - 2
        accumulator2 = accumulator[0:n] + [accumulator[n] + 1] + accumulator[n + 1:]
        if num == 1:
            return accumulator2
        else:
            return _dist(num - 1, accumulator2)
    d = _dist(number, [0 for _ in range(11)])
    print("\n".join(f"{i + 2} : {d[i]}" for i in range(11)))
def main():
    number = int(input())
    d = distribution(number)
    print("\n".join(f"{i + 2} : {d[i]}" for i in range(11)))
