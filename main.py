from api.WordsApi import WordsApi
from factories.PlayerFactory import PlayerFactory
from controllers.LobbyController import LobbyController
from controllers.GameController import GameController
from model.GameState import GameState
from enums.GameStepsEnum import GameStepsEnum

if __name__ == '__main__':
    words_api = WordsApi()
    wordlist = words_api.get_wordlist()
    game_state = GameState()
    game_state.set_wordlist(wordlist)

    player_factory = PlayerFactory()
    lobby_controller = LobbyController(player_factory, game_state)
    game_controller = GameController(game_state)

    controllers = {
        GameStepsEnum.PLAYERS_SET_UP: game_controller,
        GameStepsEnum.UNINITIALIZED: lobby_controller
    }

    while not game_state.get_game_step() == GameStepsEnum.QUIT:
        controller = lobby_controller
        if game_state.game_step == GameStepsEnum.STOPPED or game_state.game_step == GameStepsEnum.UNINITIALIZED:
            controller = lobby_controller
        else:
            controller = game_controller

        controller.handle()
