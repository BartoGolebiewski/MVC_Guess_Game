from controllers.Controller import Controller
from factories.PlayerFactory import PlayerFactory
from model.GameState import GameState
from enums.GameStepsEnum import GameStepsEnum


class LobbyController(Controller):
    def __init__(self, player_factory: PlayerFactory, game_state: GameState):
        super().__init__(game_state)
        self.player_factory = player_factory

    def handle(self):
        print("Welcome to the PENDANT, What you want to do?")
        print("1. Start a game")
        print("2. Exit")
        choice = input("Choose: ")

        if choice != "1":
            self.quit()
        else:
            players_count = int(input("How many players will be playing?\n"))

            for i in range(0, players_count):
                name = input(">Enter name: ")
                player = self.player_factory.create(name, 0, 3, 0, 0)
                self.game_state.add_player(player)

            self.game_state.set_game_step(GameStepsEnum.PLAYERS_SET_UP)