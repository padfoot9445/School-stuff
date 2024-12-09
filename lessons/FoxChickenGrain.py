from enum import Enum, auto
class FaliureException(Exception):
    pass
class Movable(Enum):
    Grain = auto()
    Fox = auto()
    Chicken = auto()
    predator_prey_pairs = [(Fox, Chicken), (Chicken, Grain)]
class Mover(Enum):
    Farmer = auto()
class Area:
    def __init__(self, is_destination: bool = False):
        self.destination = is_destination
        self.__movers: set[Mover] = set()
        self.__movables: set[Movable] = set()
    def move_event_handler(self):
        for pred, prey in Movable.predator_prey_pairs:
            if pred in self.__movables and prey in self.__movables and len(self.__movers) == 0:
                self.wrong_move(pred, prey)
            
    @staticmethod
    def wrong_move(pred: Movable, prey: Movable):
        print(f"The {pred.name} ate the {prey.name}")
        raise FaliureException()
    
