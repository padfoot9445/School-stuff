def get_acid() -> str:
    __input = "INVALID"
    while len(__input) != len([i for i in __input if i in {'A', 'C', 'G', 'T'}]):
        __input = input()
    return __input
def check_sequence(sequence):
    count = 0
    with open("dna.txt", "r") as file:
        for line in file:
            count += line.count(sequence)
    return count

acid = get_acid()
print(f"There are {check_sequence(acid)} {acid} amino acids in the DNA sequence.")
#manual search of the file returns different results than the unit tests