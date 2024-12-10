from enum import Enum, auto
from typing import Callable
from uuid import uuid1, UUID
class FaliureException(Exception):
    def __init__(self, pred, prey):
        self.pred = pred
        self.prey = prey
        super.__init__()
    pass
class Movable(Enum):
    Grain = auto()
    Fox = auto()
    Chicken = auto()
    predator_prey_pairs = [(Fox, Chicken), (Chicken, Grain)] #only one can exist at once
class Mover(Enum):
    Farmer = auto()
class Area:
    def __init__(self, movers: set = None, movables: set = None):
        self.movers: set[Mover] = movers if movers is not None else set()
        self.movables: set[Movable] = movables if movables is not None else set()
        self.id = uuid1()
        Move_Event.subscribe(self.move_event_handler)
    
    def move_event_handler(self, items: tuple[Mover, Movable], destination: UUID):
        self.__attempt_move(items, destination)
    def __attempt_move(self, items, destination):
        self.__move(items)
        self.__recieve_move(destination)
        self.__check_wrong_move()
    def __check_wrong_move(self):
        for pred, prey in Movable.predator_prey_pairs:
            if pred in self.movables and prey in self.movables and len(self.movers) == 0:
                self.wrong_move(pred, prey)
    def __move(self, item: tuple[Mover, Movable]):
        if item[0] in self.movers and item[1] in self.movables:
            self.movers.remove(item[0]) and self.movables.remove(item[1])
    def __recieve_move(self, destination: UUID, items: tuple[Mover, Movable]):
        if self.id == destination:
            self.movables.add(items[1])
            self.movers.add(items[0])
    @staticmethod
    def wrong_move(pred: Movable, prey: Movable):
        raise FaliureException()
    
    def __str__(self) -> str:
        return "\n".join(list(self.movables) + list(self.movers))
class Event:
    def __init__(self, handlers: list[Callable] = None):
        self.handlers = [] if handlers is None else handlers
    def __call__(self, *args, **kwargs):
        for i in self.handlers:
            i(*args, **kwargs)
    def subscribe(self, handler: Callable):
        self.handlers.append(handler)
    @classmethod
    def make_event(cls, handlers:list[Callable] = None) -> "Event":
        return cls(handlers)
Move_Event = Event()
class Game:
    def __init__(self):
        self.SRC = Area({Mover.Farmer}, {Movable.Grain, Movable.Chicken, Movable.Fox})
        self.DST = Area()
    def move(self, c: Mover, i: Movable, dst: Area):
        try:
            Move_Event((c, i), dst.id)
        except FaliureException as e:
            self.puzzle_faliure(e.pred, e.prey)
            raise e
        finally:
            self.display()
    def display(self):
        print(f"This side of the river: \n {str(self.SRC)}")
        print(f"That side of the river: \n {str(self.DST)}")     
    def try_puzzle_complete(self):
        if Movable.Grain in self.DST and Movable.Fox in self.DST and Movable.Chicken in self.DST:
            self.puzzle_complete()
    @staticmethod
    def puzzle_faliure(predator: Movable, prey: Movable):
        print(f"The {predator.name} ate the {prey.name}")
    @staticmethod
    def puzzle_complete():
        print("You solved the puzzle.")
def main():
    game = Game()
    try:
        while True:
            i = input()
            tm: Movable
            match i:
                case "chicken":
                    tm = Movable.Chicken
                case "fox":
                    tm = Movable.Fox
                case "grain":
                    tm = Movable.Grain
            game.move(Mover.Farmer, tm)
    except FaliureException:
        pass

if __name__ == "__main__":
    main()