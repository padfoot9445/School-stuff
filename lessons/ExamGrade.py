from enum import Enum
class Grade(Enum):
    U = "U"
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
GRADE_BOUNDARIES = [float("-infinity"), 2, 4, 13, 22, 31, 41, 54, 67, 80, float("infinity")]
GRADES = [Grade.U, Grade.ONE, Grade.TWO, Grade.THREE, Grade.FOUR, Grade.FIVE, Grade.SIX, Grade.SEVEN, Grade.EIGHT, Grade.NINE]
def grade(mark: int) -> Grade:
    for i in range(len(GRADES)):
        if GRADE_BOUNDARIES[i] <= mark < GRADE_BOUNDARIES[i + 1]:
            return GRADES[i]
def marks_needed(mark: int) -> int:
    g = grade(mark) #not the best, but should work
    if mark >= 80:
        return 0 #should be infinity but w/e
    delta = 0
    while grade(mark + delta) == g:
        delta += 1
    return delta

def main():
    mark: int = int(input())
    print(f"A mark of {mark} is grade {(g := grade(mark)).value}")
    print(f"You needed {marks_needed(mark)} marks to achieve the next grade.")
    
if __name__ == "__main__":
    main()