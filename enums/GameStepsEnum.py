from enum import Enum


class GameStepsEnum(Enum):
    UNINITIALIZED = "uninitialized"
    STOPPED = "stopped"
    PLAYERS_SET_UP = "players_set_up"
    QUIT = "quit"
    STARTED = "started"
