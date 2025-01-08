from enum import Enum
class Movable:
    def __init__(self, name: str):
        self.position = Position.THISSIDE
        self.name = name
    def toggle(self):
        self.position = (Position.THATSIDE, Position.THISSIDE)[self.position.value]
    def __eq__(self, other: "Movable"):
        return self.name == other.name
    def __hash__(self) -> int:
        return hash(self.name)
    def __str__(self) -> str:
        return self.name[0].upper() + self.name[1:]
class Game:
    def __init__(self, farmer: Movable, players: set[Movable], pred_prey: list[tuple[Movable, Movable]]):
        self.farmer = farmer
        self.all: set["Movable"] = players
        self.pred_prey_pairs = pred_prey
    @property
    def this_side(self) -> set["Movable"]:
        return {i for i in self.all if i.position == Position.THISSIDE}
    @property
    def that_side(self) -> set["Movable"]:
        return {i for i in self.all if i.position == Position.THATSIDE}
    def __str__(self) -> str:
        this_side: str = "This side of the river:\n" + "\n".join("\t" + str(i) for i in self.all if i.position == Position.THISSIDE)
        that_side: str = "The other side of the river:\n" + "\n".join("\t" + str(i) for i in self.all if i.position == Position.THATSIDE)
        return f"{this_side}\n{that_side}"
    def move_player(self, player_name: str) -> tuple[bool, str | None]:
        for i in self.all:
            if player_name == i.name:
                
                if (not i == self.farmer) and self.farmer.position == i.position:
                    self.farmer.toggle()
                i.toggle()
                break
        else:
            raise StopIteration()
        
        chk_wrong_move: str = self.wrong_move()
        right_move = self.puzzle_solved
        if chk_wrong_move != "":
            return (False, chk_wrong_move)
        elif right_move:
            return (True, "You solved the puzzle.")
        return  (False, None)
    def wrong_move(self) -> str | None:
        return self.__wrong_move(self.this_side) + self.__wrong_move(self.that_side)
    def __wrong_move(self, player_set: set[Movable]) -> str:
        for potential_pred in player_set:
            for pot_prey in player_set:
                if (potential_pred, pot_prey) in self.pred_prey_pairs and (not self.farmer in player_set):
                    return f"The {potential_pred.name} ate the {pot_prey.name}"
        return ""
    @property
    def puzzle_solved(self) -> bool:
        return len(self.that_side) == (len(self.all))
    def play(self):
        while not self.puzzle_solved:
            print(str(self))
            try:
                solved, msg = self.move_player(input().lower().strip())
                if msg != None:
                    print(str(self))
                    print(msg)
                    exit(1)
            except StopIteration:
                print("Could not find player, exiting")
                exit(1)
        
class Position(Enum):
    THISSIDE = 0
    THATSIDE = 1
FOX = Movable("fox")
FARMER = Movable("farmer")
CHICKEN = Movable("chicken")
GRAIN = Movable("grain")
PRED_PREY = [(FOX, CHICKEN), (CHICKEN, GRAIN)]
GAME = Game(FARMER, {FOX, FARMER, CHICKEN, GRAIN}, PRED_PREY)
GAME.play()