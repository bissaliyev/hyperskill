class TicTacToe:
    def __init__(self):
        self.cells = list(" " * 9)

    def print_board(self):
        print("---------")
        print("| {} {} {} |".format(self.cells[0], self.cells[1], self.cells[2]))
        print("| {} {} {} |".format(self.cells[3], self.cells[4], self.cells[5]))
        print("| {} {} {} |".format(self.cells[6], self.cells[7], self.cells[8]))
        print("---------")


    def move(self, ch):
        while self.is_vacant():
            x, y = input("Enter the coordinates:").split()
            if not (x.isdigit() or y.isdigit()):
                print("You should enter numbers!")
            elif not(0 < int(x) < 4 and 0 < int(y) < 4):
                print("Coordinates should be from 1 to 3!")
            else:
                x, y = int(x), int(y)
                new_coord = (x - 1) + (3 * (3 - y))

                if self.cells[new_coord] == "X" or self.cells[new_coord] == "O":
                    print("This cell is occupied! Choose another one!")
                else:
                    self.cells[new_coord] = ch
                    break


    def is_winner(self, ch):
        if self.cells[0] == self.cells[1] == self.cells[2] == ch \
            or self.cells[3] == self.cells[4] == self.cells[5] == ch \
            or self.cells[6] == self.cells[7] == self.cells[8] == ch \
            or self.cells[0] == self.cells[3] == self.cells[6] == ch \
            or self.cells[1] == self.cells[4] == self.cells[7] == ch \
            or self.cells[2] == self.cells[5] == self.cells[8] == ch \
            or self.cells[0] == self.cells[4] == self.cells[8] == ch \
            or self.cells[2] == self.cells[4] == self.cells[6] == ch:

            return True
        return False


    # def is_vacant(self):
    #     empty = (" ", "_")
    #     return any(True if c in empty else False for c in self.cells)

    def is_vacant(self):
        # empty = (" ", "_")
        return any(True for c in self.cells if c == " ")


    def is_balanced(self):
        return 0 <= abs(self.cells.count("X") - self.cells.count("O")) <= 1


    def check_state(self):
        win_x = self.is_winner("X")
        win_o = self.is_winner("O")

        if win_x:
            print("X wins")
            return True
        if win_o:
            print("O wins")
            return True
        # if (win_x and win_o) or not self.is_balanced():
        #     print("Impossible")
        #     return True
        if not win_x and not win_o and not self.is_vacant():
            print("Draw")
            return True
        # if not win_x and not win_o and self.is_vacant():
        #     print("Game not finished")
        #     return True
        return False

    def play(self):
        while True:
            self.print_board()
            self.move("X")
            self.print_board()
            if self.check_state():
                break

            self.print_board()
            self.move("O")
            self.print_board()
            if self.check_state():
                break

tictactoe = TicTacToe()
tictactoe.play()
