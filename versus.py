import pickle

from datetime import datetime

from player_alpha_random import PlayerAlphaRandom
from player_human import PlayerHuman
from player_mc import PlayerMC
from player_ql import PlayerQL
from player_random import PlayerRandom
from board import PLAYER_X, PLAYER_O
from game_organizer import GameOrganizer
from stop_watch import stop_watch


def random_vs_random():
    p1 = PlayerRandom(PLAYER_X, 'Random1')
    p2 = PlayerRandom(PLAYER_O, 'Random2')
    game = GameOrganizer(p1, p2)
    # game = GameOrganizer(p1, p2, 1000, False, False, 100)
    game.progress()

def human_vs_random():
    p1 = PlayerHuman(PLAYER_X)
    p2 = PlayerRandom(PLAYER_O)
    game = GameOrganizer(p1, p2)
    game.progress()


def human_vs_alpha_random():
    p1 = PlayerHuman(PLAYER_X)
    p2 = PlayerAlphaRandom(PLAYER_O)
    game = GameOrganizer(p1, p2)
    game.progress()


def human_vs_mc():
    p1 = PlayerHuman(PLAYER_X)
    p2 = PlayerMC(PLAYER_O, 'M2')
    game = GameOrganizer(p1, p2)
    game.progress()


def random_vs_alpha_random():
    p1 = PlayerRandom(PLAYER_X)
    p2 = PlayerAlphaRandom(PLAYER_O)
    game = GameOrganizer(p1, p2)
    game.progress()


@stop_watch
def mc_vs_mc():
    p1 = PlayerMC(PLAYER_X, 'M1')
    p2 = PlayerMC(PLAYER_O, 'M2')
    game = GameOrganizer(p1, p2, 3, False)
    # game = GameOrganizer(p1, p2)
    game.progress()


def mc_vs_alpha_random():
    p1 = PlayerMC(PLAYER_X, 'M1')
    p2 = PlayerAlphaRandom(PLAYER_O, 'Random')
    game = GameOrganizer(p1, p2)
    game.progress()


def ql_vs_ql():
    p1 = PlayerQL(PLAYER_X, 'Q1')
    p2 = PlayerQL(PLAYER_O, 'Q2')
    game = GameOrganizer(p1, p2, 1000000, False, False, 10000)
    game.progress()

    with open('dump/ql_vs_ql_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)


def ql_vs_random():
    p1 = PlayerQL(PLAYER_X, 'Q1')
    p2 = PlayerRandom(PLAYER_O)
    game = GameOrganizer(p1, p2, 100000, False, False, 2000)
    game.progress()

    with open('dump/pQ_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)


def ql_vs_alpha_random():
    p1 = PlayerQL(PLAYER_X, 'Q1')
    p2 = PlayerAlphaRandom(PLAYER_O)
    game = GameOrganizer(p1, p2, 1000000, False, False, 10000)
    game.progress()

    with open('dump/ql_vs_alpha_random_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)

    # pQ.e = 0
    # p2 = PlayerAlphaRandom(PLAYER_X)
    # game = GameOrganizer(pQ, p2, 1000, False, False, 100)
    # game.progress()
#
#
# def mc_vs_ql():
#     pQ = PlayerQL(PLAYER_O, "QL1")
#     p2 = PlayerQL(PLAYER_X, "QL2")
#     game = TTT_GameOrganizer(pQ, p2, 100000, False, False, 10000)
#     game.progress()
#
#     pQ.e = 0
#     p2 = PlayerMC(PLAYER_X, "M1")
#     game = TTT_GameOrganizer(pQ, p2, 100, False, False, 10)
#     game.progress()
#
#

def human_vs_dumped():
    p1 = PlayerHuman(PLAYER_X)
    with open('dump/pQ.pkl', mode='rb') as f:
        p2 = pickle.load(f)

    p2.e = 0
    game = GameOrganizer(p1, p2)
    game.progress()

        # def dqn_vs_alpha_random():
#     pDQ=DQNPlayer(PLAYER_X)
#     p2=PlayerAlphaRandom(PLAYER_O)
#     game=TTT_GameOrganizer(pDQ,p2,20000,False,False,1000)
#     game.progress()
#
#
# def dqn_vs_ql():
#     pQ = PlayerQL(PLAYER_O, "QL1")
#     p2 = PlayerQL(PLAYER_X, "QL2")
#     game = TTT_GameOrganizer(pQ, p2, 100000, False, False, 10000)
#     game.progress()
#
#     pDQ = DQNPlayer(PLAYER_X)
#     p2 = PlayerAlphaRandom(PLAYER_O)
#     game = TTT_GameOrganizer(pDQ, p2, 20000, False, False, 1000)
#     game.progress()
#
#     pQ.e = 0
#     pDQ.e = 1
#
#     game = TTT_GameOrganizer(pDQ, pQ, 30000, False, False, 1000)
#     game.progress()

def sdate():
    return datetime.now().strftime('%Y_%m_%d_%H_%M_%S')