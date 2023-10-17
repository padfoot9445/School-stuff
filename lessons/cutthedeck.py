import random

random.seed(10)


# The value order of the cards for reference
CARDS = [
    "6C",
    "7C",
    "8C",
    "9C",
    "10C",
    "JC",
    "QC",
    "KC",
    "AC",
    "6D",
    "7D",
    "8D",
    "9D",
    "10D",
    "JD",
    "QD",
    "KD",
    "AD",
    "6H",
    "7H",
    "8H",
    "9H",
    "10H",
    "JH",
    "QH",
    "KH",
    "AH",
]


def play_game():
    deck = CARDS
    random.shuffle(deck)
    __input = float("infinity")  # initialize value outside of range defined below
    while not (__input >= 0 and __input <= 34):
        try:
            __input = int(input())
        except ValueError:
            continue
    picked = deck.pop(__input)
    computer = deck[random.randint(0, 33)]
    if output_winner(picked, computer) == computer:
        print("CPU wins.")
    else:
        print("You win!")


def __compare_suits(s1, s2):
    suit_to_num = {"C": 0, "D": 1, "H": 2, "S": 3}
    if suit_to_num[s1] > suit_to_num[s2]:
        return 1
    elif suit_to_num[s1] == suit_to_num[s2]:
        return 2
    else:
        return 0


def output_winner(player, computer):
    def __equals(__player, __computer):
        """a wrapper around compare_suits to return the right thing"""
        if __compare_suits(__player, __computer):
            return __player
            # if the suit of the player is larger
        else:
            return __computer

    try:
        n1 = int(player[0])
    except ValueError:
        try:
            int(computer[0])
        except ValueError:
            letter_to_num = {"J": 1, "Q": 2, "K": 3, "A": 4}
            n1 = letter_to_num[player[0]]
            n2 = letter_to_num[computer[0]]
            if n1 == n2:
                return __equals(player, computer)
            elif n1 > n2:
                return player
            else:
                return computer
        else:
            return player
            # player has a letter card where computer has a number
    else:
        try:
            n2 = int(computer[0])
        except ValueError:
            return computer
            # computer is a letter card
        else:
            if n1 > n2:
                return player
            elif n2 > n1:
                return computer
            else:
                return __equals(player, computer)
