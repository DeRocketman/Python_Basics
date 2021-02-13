import random


class SteinScherePapier:
    def __init__(self):
        self.userChoice = 1
        self.aiChoice = 1
        self.userWins = 0
        self.aiWins = 0
        self.auswahl = {1: "Rock",
                        2: "Paper",
                        3: "Scissors",
                        4: "Lizard",
                        5: "Spock"}
        self.winningText = {
                            [1][3]: "Rock crushes Scissors",
                            [1][4]: "Rock crushes Lizard",
                            [2][1]: "Paper covers Rock",
                            [2][5]: "Paper disproves Spock",
                            [3][2]: "Scissors cuts Paper",
                            [3][4]: "Scissors decapitates Lizard",
                            [4][2]: "Lizard eats Paper",
                            [4][5]: "Lizard poisons Spock",
                            [5][1]: "Spock vaporizes Rock",
                            [5][3]: "Spock smashes Scissors"}

    def gewinner(self):
        wt = self.winningText
        uc = self.userChoice
        ac = self.aiChoice
        uw = "Grats u win because: "
        ul = "Oh no you Lost because: "
        if uc == 1 and ac == 3 or uc == 1 and ac == 4 or uc == 2 and ac == 1 or uc == 2 and ac == 5 or uc == 3 and ac == 2 or uc == 3 and ac == 4 or uc == 4 and ac == 2 or uc == 4 and ac == 5 or uc == 5 and ac == 1 or uc == 5 and ac == 3:
            self.userWins = self.userWins + 1
            print(uw + wt[uc][ac] + "\n", self.userWins, ":", self.aiWins)
        else:
            self.aiWins = self.aiWins + 1
            print(ul + wt[ac][uc] + "\n", self.userWins, ":", self.aiWins)

    def choice(self):
        self.userChoice = int(input("Auswahlmöglichkeiten: \n1: Rock\n2: Paper\n3: Scissors\n4: Lizard\n5: Spock\n"))
        self.aiChoice = random.randint(1, 5)
        print("U choice:" + self.auswahl[self.userChoice])
        print("AI choice:" + self.auswahl[self.aiChoice])


if __name__ == '__main__':
    repeat = True
    while repeat:
        game = SteinScherePapier()
        game.choice()
        game.gewinner()
        r = int(input("Quit? Press 0"))
        if r == 0:
            repeat = False



