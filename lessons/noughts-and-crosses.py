import enum
class Square(enum.Enum):
    EMPTY = " "
    NOUGHT = "X"
    CROSS = "O"
class Board:
    def __init__(self):
        self.board = [[Square.EMPTY for __ in range(3)] for _ in range(3)]
        self.to_play = Square.NOUGHT #reuse square enums here
    def __check_win(self, square:tuple[int, int]) -> bool:
        side = self.to_play
        other = Square.NOUGHT if side == Square.CROSS else Square.CROSS
        COLUMN = {self.board[0][square[0]], self.board[1][square[0]], self.board[2][square[0]]}
        if (not other in self.board[square[1]] and not Square.EMPTY in self.board[square[1]]) or (not other in COLUMN and not Square.EMPTY in COLUMN ):
            return True
        elif square[0] == square[1]:
            DIAGONAL = {self.board[0][0], self.board[1][1], self.board[2][2]}
            if not other in DIAGONAL and not Square.EMPTY in DIAGONAL:
                return True
        return False
    @property
    def draw(self):
        if not Square.EMPTY in {i for e in self.board for i in e}:
            return True
        return False
    def play(self):
        while True:
            self.to_play = Square.NOUGHT if self.to_play == Square.CROSS else Square.CROSS
            while True:
                __input = input()
                x, y = int(__input[0]), int(__input[1])
                if self.board[y][x] == Square.EMPTY:
                    self.board[y][x] = self.to_play
                    break
            if self.draw:
                break
            elif self.__check_win((x,y)):
                print(f"{'X' if self.to_play == Square.CROSS else 'O'} wins.")
                break
            print(str(self))
    def __str__(self):
        output = [" 0 1 2"]
        for index, line in enumerate(self.board):
            output.append(f"{index} "+ "|".join(i.value for i in line))
        return "\n".join(output)


Board().play()

