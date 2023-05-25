from random import randint, choice

# command line tic tac toe

class Cell:
    def __init__(self):
        self.content = "   "
        self.ticked = False
        self.current_player = None

    def tick(self, current_player):
        if current_player == "0":
            self.content = " X " # X for player 0
            self.current_player = "0"
        else:
            self.content = " O " # O for player 1
            self.current_player = "1"

        self.ticked = True


class TicTacToe:
    def __init__(self):
        self.rowOne = [Cell(), Cell(), Cell()]
        self.rowTwo = [Cell(), Cell(), Cell()]
        self.rowThree = [Cell(), Cell(), Cell()]
        self.rows = [self.rowOne, self.rowTwo, self.rowThree] # initializes rows

        self.is_ai_controlled = { # players not ai controlled by default
            "0" : False,
            "1" : False
        }

        self.column_row_indices = { # map of column and row pair keys
            1 : (2, 0),
            2 : (2, 1),
            3 : (2, 2),
            4 : (1, 0),
            5 : (1, 1),
            6 : (1, 2),
            7 : (0, 0),
            8 : (0, 1),
            9 : (0, 2)
        }

        self.init_cells()
    
    def init_cells(self):
        for row in self.rows: # set all cells to have default values
            for cell in row:
                cell.content = "   "
                cell.ticked = False
                cell.current_player = None

    def draw(self, current_player): # serializes game state (current_player needed to show who's turn it is)
        print(f"\nTurn of Player {current_player}")
        print("     1   2   3")
        print("   -------------")
        print(f" 6 |{self.rows[0][0].content}|{self.rows[0][1].content}|{self.rows[0][2].content}|")
        print("   ----+---+----")
        print(f" 3 |{self.rows[1][0].content}|{self.rows[1][1].content}|{self.rows[1][2].content}|")
        print("   ----+---+----")
        print(f" 0 |{self.rows[2][0].content}|{self.rows[2][1].content}|{self.rows[2][2].content}|")
        print("   -------------")

    def checkWin(self):
        # 1 signifies that someone won
        # 2 signifies that no one has won yet
        # 3 signifies a tie
        
        for i in range(3): # checks columns
            if self.rowOne[i] == self.rowTwo[i] == self.rowThree[i] and self.rowOne[i] is not None:
                return 1 # there is a winner

        for row in self.rows: # checks rows
            if row[0].current_player == row[1].current_player  == row[2].current_player and row[0].current_player is not None:
                return 1 # there is a winner

        if self.rows[0][0].current_player == self.rows[1][1].current_player == self.rows[2][2].current_player and self.rows[0][0].current_player is not None: # checks one diagonal
            return 1 # there is a winner

        if self.rows[2][0].current_player == self.rows[1][1].current_player == self.rows[0][2].current_player and self.rows[2][0].current_player is not None: # checks other diagonal
            return 1 # there is a winner

        for row in self.rows: # checks if all cells are ticked
            for cell in row:
                if cell.ticked == False:
                    return 2 # returns no winner if some cell unticked

        return 3 # return draw (all cells ticked and no winner)

    def play(self, set_starting_player = None):
        self.init_cells() # sets all cell values to be default

        print("Commands: restart (restarts the game), quit (quits game), changemode (switches current player to be AI controlled)") # lists commands

        current_index = randint(0, 1) # randomly chooses starting player

        if set_starting_player != None: # if starting player chosen
            current_index = set_starting_player - 1 # - 1 because it gets incremented upon setting current player
            
        starting_player = current_index # saves starting player

        while True:
            current_player = ["0", "1"][(current_index + 1) % 2] # repeatedly goes through ["0", "1"]
            current_index += 1

            self.draw(current_player)

            while True:
                try:
                    if not self.is_ai_controlled[current_player]: # if player not AI controlled
                        player_input = input("\nWhich cell to tick? (sum of row and column number): ")
                    
                        if player_input == "restart":
                            return self.play(set_starting_player=(int(starting_player) + 1) % 2) # starts new game with same starting player
                        elif player_input == "quit":
                            return # exits play
                        elif player_input == "changemode":
                            other_player = str((current_index + 1) % 2)
                            if self.is_ai_controlled[other_player]: # if other player ai controlled
                                self.is_ai_controlled[other_player] = False # set other player to not be ai controlled
                            else: # if current player ai controlled
                                self.is_ai_controlled[current_player] = True # set current player to be ai controlled

                    if self.is_ai_controlled[current_player]: # if current player AI controlled
                        unticked_cells = []
                        for row in self.rows:
                            for cell in row:
                                if not cell.ticked:
                                    unticked_cells.append(cell) # creates list of all unticked cells
                        
                        choice(unticked_cells).tick(current_player) # randomly chooses unticked cell and ticks it
                        break
                    
                    if int(player_input) not in [7, 8, 9, 4, 5, 6, 1, 2, 3]: # if input not valid column and row pair
                        print("\nInvalid coordinates, try again\n")
                        self.draw(current_player)
                        continue

                    indices = self.column_row_indices[int(player_input)] # gets column and row pair
                    if self.rows[indices[0]][indices[1]].ticked: # if cell already ticked
                        print("\nCell already ticked\n")
                        self.draw(current_player)
                        continue

                    self.rows[indices[0]][indices[1]].tick(current_player) # tick desired cell
                    break
                except ValueError: # if input not valid
                    print("\nInvalid input, try again\n")
                    self.draw(current_player)
                    continue

            checkWin = self.checkWin()
            if checkWin == 1: # if there is a winner
                self.draw(current_player)
                print(f"\n\n{current_player} has won!\n")
                return self.play(set_starting_player=None)
            if checkWin == 3: # if there is a draw
                self.draw(current_player)
                print("\n\nIt's a draw!\n")
                return self.play(set_starting_player=starting_player) # starting player set so that other player starts
            # if no win or draw keep playing


if __name__ == "__main__":
    TicTac = TicTacToe()
    TicTac.play()
