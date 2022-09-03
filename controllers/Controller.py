from enums.GameStepsEnum import GameStepsEnum
from model.GameState import GameState


class Controller:
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    # refac state machine
    def quit(self):
        self.game_state.game_step = GameStepsEnum.QUIT
        exit(1)

    def start(self):
        self.game_state.game_step = GameStepsEnum.STARTED

    def stop(self):
        self.game_state.game_step = GameStepsEnum.UNINITIALIZED

    def players_setup(self):
        self.game_state.game_step = GameStepsEnum.PLAYERS_SET_UP

    def handle(self, **user_input) -> None:
        pass