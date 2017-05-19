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


def human_vs_dumped():
    p1 = PlayerHuman(PLAYER_O)
    with open('dump/ql_vs_alpha_random_2017_05_19_17_42_46.pkl', mode='rb') as f:
        p2 = pickle.load(f)

    p2.e = 0
    game = GameOrganizer(p1, p2)
    game.progress()


def mc_vs_dumped():
    p1 = PlayerMC(PLAYER_O, 'M1')
    # with open('dump/ql_vs_alpha_random_2017_05_19_17_42_46.pkl', mode='rb') as f:
    with open('dump/ql_vs_ql_2017_05_19_18_35_32.pkl', mode='rb') as f:
        p2 = pickle.load(f)

    p2.e = 0
    game = GameOrganizer(p1, p2, 10, False)
    game.progress()


def sdate():
    return datetime.now().strftime('%Y_%m_%d_%H_%M_%S')