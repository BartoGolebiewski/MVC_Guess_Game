from model.Player import Player
from enums.GameStepsEnum import GameStepsEnum

class GameState:
    def __init__(self):
        self.players = []
        self.wordlist = []

        self.word = None
        self.choices = None
        self.current_player_index = 0
        self.game_step = GameStepsEnum.UNINITIALIZED

    def set_word(self, word):
        self.word = word

    def get_word(self):
        return self.word

    def set_wordlist(self, wordlist: list):
        self.wordlist = wordlist

    def get_wordlist(self):
        return self.wordlist

    def get_players(self):
        return self.players

    def set_players(self, players):
        self.players = players

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, index):
        self.players.remove(index)

    def set_choices(self, choices):
        self.choices = choices

    def get_choices(self):
        return self.choices

    def set_current_player_index(self, current_player_index):
        self.current_player_index = current_player_index

    def get_current_player_index(self):
        return self.current_player_index

    def get_current_player(self) -> Player:
        return self.players[self.get_current_player_index()]

    def set_game_step(self, game_step):
        self.game_step = game_step

    def get_game_step(self):
        return self.game_step

