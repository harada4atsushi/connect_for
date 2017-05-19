import numpy as np
from more_itertools import chunked

EMPTY=0
PLAYER_X=1
PLAYER_O=-1
RED = '\033[91m'
ENDC = '\033[0m'
MARKS={PLAYER_X: RED + "X" + ENDC, PLAYER_O: "O", EMPTY: " "}
DRAW=2
COL_NUM = 5
ROW_NUM = 5
ALL_POS_COUNT = 25

class Board:

    def __init__(self,board=None):
        if board==None:
            self.board = []
            for i in range(ALL_POS_COUNT):self.board.append(EMPTY)
        else:
            self.board=board
        self.winner=None

    def get_possible_pos(self):
        pos = []
        append = pos.append

        for i in range(ALL_POS_COUNT):
            if self.board[i] == EMPTY:
                # 下のマスが埋まっている場合(重力対応)
                below_i = i + COL_NUM
                if below_i >= ALL_POS_COUNT or self.board[below_i] != EMPTY:
                    append(i)

        return pos

    def print_board(self):
        tempboard=[]
        for i in self.board:
            tempboard.append(MARKS[i])
        row = ' {} | {} | {} | {} | {} '
        hr = '\n-------------------\n'

        matrix_str = ''
        for i in range(ROW_NUM):
            matrix_str += row
            if i != ROW_NUM - 1:
                matrix_str += hr

        print(matrix_str.format(*tempboard))


    def check_winner(self, pos):
        self.check_winner_horizontal(pos)
        self.check_winner_vertical()
        self.check_winner_skew()
        return None


    def check_winner_horizontal(self, pos):
        # start_pos = pos - (pos % COL_NUM)
        # end_pos = start_pos + COL_NUM - 1
        #
        # for i in range(start_pos, end_pos):
        #     if i + COL_NUM - 1 > end_pos:
        #         break
        #     if self.board[i] == self.board[i + 1] == self.board[i + 2] == self.board[i + 3]:
        #         if self.board[i] != EMPTY:
        #             self.winner = self.board[i]
        #             return self.winner

        # ②
        # for i in range(ALL_POS_COUNT - 4):
        #     if i % COL_NUM < (i + 3) % COL_NUM:
        #         if self.board[i] == self.board[i + 1] == self.board[i + 2] == self.board[i + 3]:
        #             if self.board[i] != EMPTY:
        #                 self.winner = self.board[i]
        #                 return self.winner

        # ①
        rows = list(chunked(self.board, COL_NUM))
        self.check_connected(rows)


    def check_winner_vertical(self):
        rows = list(chunked(self.board, COL_NUM))
        cols = list(zip(*rows))
        self.check_connected(cols)


    def check_winner_skew(self):
        # indexに対応するマスに埋まっているプレイヤーの行列を作る
        for index_list in Board.__get_check_indices():
            if self.board[index_list[0]] == self.board[index_list[1]] == self.board[index_list[2]] == self.board[index_list[3]]:
               if self.board[index_list[0]] != EMPTY:
                   self.winner = self.board[index_list[0]]
                   return self.winner
        # self.check_connected(rows)


    def check_connected(self, lists):
        for list in lists:
            pre = EMPTY
            count = 0
            for player in list:
                if player == EMPTY:
                    count = 0
                elif pre == player:
                    count += 1
                    if count == 4:
                        self.winner = player
                        return self.winner
                else:
                    count = 1

                pre = player


    def check_draw(self):
        if len(self.get_possible_pos())==0 and self.winner is None:
            self.winner=DRAW
            return DRAW
        return None

    def move(self,pos,player):
        if self.board[pos]== EMPTY:
            self.board[pos]=player
        else:
            self.winner=-1*player
        self.check_winner(pos)
        self.check_draw()

    def clone(self):
        return Board(self.board.copy())

    def switch_player(self):
        if self.player_turn == self.player_x:
            self.player_turn=self.player_o
        else:
            self.player_turn=self.player_x


    @classmethod
    def __get_check_indices(cls):
        if hasattr(cls, 'check_indices'):
            return cls.check_indices

        # print('__get_check_indices')
        indices = []

        # 左上がり斜め方向のindexのリストを作る
        for i in range(ALL_POS_COUNT):
            list = []
            next_i = i
            while next_i < ALL_POS_COUNT:
                if next_i % COL_NUM >= i % COL_NUM:
                    list.append(next_i)
                next_i += COL_NUM + 1

            if len(list) >= 4:
                indices.append(list)

        # 右上がり斜め方向のindexのリストを作る
        for i in range(ALL_POS_COUNT):
            list = []
            next_i = i
            while next_i < ALL_POS_COUNT:
                if (next_i % COL_NUM < i % COL_NUM) or i == next_i:
                    list.append(next_i)
                next_i += COL_NUM - 1

            if len(list) >= 4:
                indices.append(list)

        cls.check_indices = indices
        # print(indices)
        return cls.check_indices

