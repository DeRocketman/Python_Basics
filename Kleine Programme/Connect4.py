class Board:
    def __init__(self):
        self.stack1 = [0, 0, 0, 0, 0, 0]
        self.stack2 = [0, 0, 0, 0, 0, 0]
        self.stack3 = [0, 0, 0, 0, 0, 0]
        self.stack4 = [0, 0, 0, 0, 0, 0]
        self.stack5 = [0, 0, 0, 0, 0, 0]
        self.stack6 = [0, 0, 0, 0, 0, 0]
        self.stack7 = [0, 0, 0, 0, 0, 0]
        self.stackcount = [0, 0, 0, 0, 0, 0, 0]
        self.allstack = [self.stack1, self.stack2, self.stack3, self.stack4, self.stack5,
                         self.stack6, self.stack7]

    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

    def print_board(self):
        print(" " + "1" + " | " + "2" + " | " + "3" + " | " + "4" + " | " + "5" + " | " + "6" + " | " + "7" + " \n" +
              "---------------------------\n" +
              " " + self.sign_to_printable(self.stack1[5]) + " | " + self.sign_to_printable(
            self.stack2[5]) + " | " + self.sign_to_printable(self.stack3[5]) + " | " + self.sign_to_printable(
            self.stack4[5]) + " | " + self.sign_to_printable(self.stack5[5]) + " | " + self.sign_to_printable(
            self.stack6[5]) + " | " + self.sign_to_printable(self.stack7[5]) + " \n" +
              " " + self.sign_to_printable(self.stack1[4]) + " | " + self.sign_to_printable(
            self.stack2[4]) + " | " + self.sign_to_printable(self.stack3[4]) + " | " + self.sign_to_printable(
            self.stack4[4]) + " | " + self.sign_to_printable(self.stack5[4]) + " | " + self.sign_to_printable(
            self.stack6[4]) + " | " + self.sign_to_printable(self.stack7[4]) + " \n" +
              " " + self.sign_to_printable(self.stack1[3]) + " | " + self.sign_to_printable(
            self.stack2[3]) + " | " + self.sign_to_printable(self.stack3[3]) + " | " + self.sign_to_printable(
            self.stack4[3]) + " | " + self.sign_to_printable(self.stack5[3]) + " | " + self.sign_to_printable(
            self.stack6[3]) + " | " + self.sign_to_printable(self.stack7[3]) + " \n" +
              " " + self.sign_to_printable(self.stack1[2]) + " | " + self.sign_to_printable(
            self.stack2[2]) + " | " + self.sign_to_printable(self.stack3[2]) + " | " + self.sign_to_printable(
            self.stack4[2]) + " | " + self.sign_to_printable(self.stack5[2]) + " | " + self.sign_to_printable(
            self.stack6[2]) + " | " + self.sign_to_printable(self.stack7[2]) + " \n" +
              " " + self.sign_to_printable(self.stack1[1]) + " | " + self.sign_to_printable(
            self.stack2[1]) + " | " + self.sign_to_printable(self.stack3[1]) + " | " + self.sign_to_printable(
            self.stack4[1]) + " | " + self.sign_to_printable(self.stack5[1]) + " | " + self.sign_to_printable(
            self.stack6[1]) + " | " + self.sign_to_printable(self.stack7[1]) + " \n" +
              " " + self.sign_to_printable(self.stack1[0]) + " | " + self.sign_to_printable(
            self.stack2[0]) + " | " + self.sign_to_printable(self.stack3[0]) + " | " + self.sign_to_printable(
            self.stack4[0]) + " | " + self.sign_to_printable(self.stack5[0]) + " | " + self.sign_to_printable(
            self.stack6[0]) + " | " + self.sign_to_printable(self.stack7[0]))

    def make_turn(self, cell, player):

        if self.stackcount[cell] < 6:

            self.allstack[cell][self.stackcount[cell]] = player.symbol
            self.stackcount[cell] = self.stackcount[cell] + 1
            return True
        else:
            return False

    def check_win(self, player):
        pass

    def is_full(self):
        for i in self.stackcount:
            if i != 6:
                return False
        return True


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(-1)
    board = Board()
    active_player = player_a
    while not board.is_full():
        board.print_board()
        try:
            cell = int(input("Where do you want to place your sign? [1-7]\n"))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 6:
            print("Please enter a number between 1 and 7")
            continue
        if not board.make_turn(cell, active_player):
            print("Invalid Move")
            continue

        if board.check_win(active_player):
            print("You wonered! GW.")
            break

        if active_player == player_a:
            active_player = player_b
        else:
            active_player = player_a
    print("It's draw")
