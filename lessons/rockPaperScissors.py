from enum import Enum, auto
from random import randint
class Play:
    Rock = "r"
    Paper = "p"
    Scissors = "s"
    @staticmethod
    def from_str(i: str) -> "Play":
        match i:
            case Play.Rock:
                return "rock"
            case Play.Paper:
                return "paper"
            case Play.Scissors:
                return "scissors"
        raise Exception("Invalid input" + i)
def convert(rps):
    return Play.from_str(rps)
def get_cpu_choice() -> Play:
    return (Play.Rock, Play.Paper, Play.Scissors)[randint(1, 3) - 1]

def __who_won_round(player: Play, cpu: Play) -> bool | None:
    if player == cpu:
        return None
    elif (player == Play.Rock and cpu == Play.Scissors) or (player == Play.Scissors and cpu == Play.Paper) or (player == Play.Paper and cpu == Play.Rock):
        return True
    else:
        return not __who_won_round(cpu, player)
def who_won_round(player: Play, cpu: Play):
    if __who_won_round(player, cpu) is None:
        return "draw"
    else:
        return "player" if __who_won_round(player, cpu) else "cpu"
def get_player_choice() -> Play:
    iput = "q"
    while not (iput in ["r", "p", "s"]):
        iput = input().strip()
    return iput
def play_game():
    scores = [0, 0] #cc, pc
    while max(scores) < 5:
        pc = get_player_choice()
        print(pc)
        cc = get_cpu_choice()
        print(f"player score: {scores[1]}  cpu score: {scores[0]}")
        if __who_won_round(pc, cc) == True:
            print(f"{who_won_round(pc, cc)}'s {Play.from_str(pc)} beats {who_won_round(cc, pc)}'s {Play.from_str(cc)}")
            scores[__who_won_round(pc, cc)] += 1
        elif __who_won_round(pc, cc) == False:
            print(f"{who_won_round(pc, cc)}'s {Play.from_str(cc)} beats {who_won_round(cc, pc)}'s {Play.from_str(pc)}")
            scores[__who_won_round(pc, cc)] += 1
        else:
            print(f"{Play.from_str(pc)} - {Play.from_str(pc)} - it's a draw.")
    if scores[0] == 5:
        print("CPU WINS!")
    else:
        print("PLAYER WINS!")

if __name__ == "__main__":
    play_game()