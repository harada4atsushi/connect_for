from board import DRAW


class PlayerHuman:
    def __init__(self,turn):
        self.name="Human"
        self.myturn=turn

    def act(self,board):
        valid = False
        while not valid:
            try:
                act = input("Where would you like to place " + str(self.myturn) + " (1-35)? ")
                act = int(act)
                #if act >= 1 and act <= 9 and board.board[act-1]==EMPTY:
                if act >= 1 and act <= 35:
                    valid=True
                    return act-1
                else:
                    print ("That is not a valid move! Please try again.")
            except Exception as e:
                    print (act +  "is not a valid move! Please try again.")
        return act

    def getGameResult(self,board):
        if board.winner is not None and board.winner!=self.myturn and board.winner!=DRAW:
            print("I lost...")