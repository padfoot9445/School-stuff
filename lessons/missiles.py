import random
class Board:
    #I don't like it, but the best way is to keep a set of building coordinates
    def __init__(self):
        self.board = [['-' for e in range(8)] for i in range(8)]
        self.moves = 50
        self.buildings = set()
        self.place_buildings()
        self.uav_scan()
        self.hit_buildings = 0
    def shoot(self, x, y) -> bool:
        self.moves -= 1
        if (x,y) in self.buildings:
            self.modify(x, y, 'H')
            self.hit_buildings += 1
            return True
        else:
            self.modify(x,y,'x')
            return False
        return
    def access(self, x, y):
        return self.board[y-1][x-1]
    def modify(self, x, y, val):
        self.board[y-1][x-1] = val
    def place_buildings(self) -> None:
        building_count = 0
        while building_count != 10:
            coords = (random.randint(1,8), random.randint(1,8))
            if coords in self.buildings:
                continue
            self.buildings.add(coords)
            building_count += 1
    def uav_scan(self):
        for x, y in self.buildings:
            if not 1 < x < 8 or not 1 < y < 8:
                continue
            match random.randint(1, 5):
                case 1:
                    self.modify(x, y, 'u')
                case 2:
                    self.modify(x+1, y, 'u')
                case 3:
                    self.modify(x, y-1, 'u')
                case 4:
                    self.modify(x-1, y, 'u')
                case 5:
                    self.modify(x, y+1, 'u')
    def __str__(self) -> str:
        output = [" "+"".join(str(i) for i in range(1,9))]
        for e in range(1,9):
            output.append(f'{e}{"".join(self.access(i, e) for i in range(1,9))}')
        return '\n'.join(output)
    @property
    def has_moves(self):
        return self.moves > 0

class Game:
    @staticmethod
    def play_game():
        board = Board()
        while board.has_moves and board.hit_buildings < 10:
            if board.shoot(*Game.get_move()):
                print(f"That's a hit! You have now scored {board.hit_buildings}")
            else:
                print(f"Miss. Only {board.moves} missiles left.")
            print(str(board))
    @staticmethod
    def get_move():
        return int(input()), int(input())

Game.play_game()


