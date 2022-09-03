import random
from controllers.Controller import Controller
from model.GameState import GameState
from enums.GameStepsEnum import GameStepsEnum


class GameController(Controller):
    def __init__(self, game_state: GameState):
        super().__init__(game_state)

    def initialize_game(self):
        self.game_state.set_word(random.choice(self.game_state.wordlist))
        self.game_state.set_choices([])
        self.game_state.set_current_player_index(0)
        self.game_state.game_step = GameStepsEnum.STARTED

    def get_guess_word_from_choices(self):
        string = ""
        for character in self.game_state.get_word():
            if character in self.game_state.get_choices():
                string = string + character
            else:
                string = string + "_"
        return string

    def switch_next_player(self):
        if self.game_state.get_current_player_index() < len(self.game_state.get_players()) - 1:
            self.game_state.set_current_player_index(self.game_state.get_current_player_index() + 1)
        else:
            self.game_state.set_current_player_index(0)

    def remove_current_player(self):
        self.game_state.remove_player(self.game_state.get_players()[self.game_state.get_current_player_index()])

    def is_player_forced_to_guess_word(self):
        return len(self.game_state.get_choices()) == len(dict.fromkeys(self.game_state.get_word())) - 1

    def validate_game_end(self):
        return len(self.game_state.get_players()) < 2

    def validate_round_end(self):
        return len(self.game_state.get_choices()) == len(dict.fromkeys(self.game_state.get_word()))

    def choosing_letter(self):
        choice = input(">Player {Player} choose letter: ".format(
            Player=self.game_state.get_current_player().get_name())
        )

        if choice not in self.game_state.get_choices() and choice in self.game_state.get_word():
            self.game_state.get_choices().append(choice)
            self.game_state.get_current_player().add_temp_point()

            print("Good one {Player}, you get a point. In this round you have: {Temp_point} ".format(
                Player=self.game_state.get_current_player().name,
                Temp_point=self.game_state.get_current_player().get_temp_point())
            )

            return True
        else:
            print("Nope, {Player} you missed ".format(Player=self.game_state.get_current_player().get_name()))
            return False

    # is action
    def guessing_word(self):
        choice = input(">Player {Player} guess word: ".format(Player=self.game_state.get_current_player().get_name()))
        if choice == self.game_state.get_word():
            self.game_state.get_players()[self.game_state.get_current_player_index()].add_point()
            self.game_state.set_choices(list(set(self.game_state.word)))

            print("Good one {Player}! You guess the word, when your scorepoint"
                  " is increase about your temp point".format(Player=self.game_state.get_current_player().name))

            return True

        else:
            self.game_state.get_current_player().remove_lifes()
            print("Nope, {Player} loses one life".format(Player=self.game_state.get_current_player().name))
            return False

    def print_game(self):
        print("Guess: {Guess}".format(Guess=self.get_guess_word_from_choices()))
        print("Turn player: {Player} ".format(Player=self.game_state.get_current_player().name))

        [print(
            "{PlayerName} ma punktow {Points} i zyc {Lifes}".format(
                PlayerName=player.name,
                Points=player.score_point,
                Lifes=player.lifes
            )
        ) for player in self.game_state.get_players()]

    def print_game_end(self):
        print("{Player} jest winner".format(Player=self.game_state.get_current_player().name))
        print("Haslem bylo {Word}".format(Word=self.game_state.get_word()))

    def start_take(self):
        print("What do you want to do?")
        print("1. Select a letter")
        print("2. Guess the keyword")

        # actions return if they succeeded
        actions = {
            "1": self.choosing_letter,
            "2": self.guessing_word
        }

        player_action = actions["2"]

        if not self.is_player_forced_to_guess_word():
            choice = input(">> Choose: ")

            if choice in actions.keys():
                player_action = actions[choice]

        did_player_succeed = player_action()

        # action failed then switch next player
        if not did_player_succeed:
            # player failed big time
            if self.game_state.get_current_player().lifes == 0:
                print("{Player} odpada bo jest slaby".format(Player=self.game_state.get_current_player().name))
                self.remove_current_player()
                self.game_state.current_player_index -= 1

            self.switch_next_player()

    def handle(self):
        while not self.game_state.game_step == GameStepsEnum.STOPPED:
            self.initialize_game()

            while self.game_state.get_game_step() == GameStepsEnum.STARTED:
                self.print_game()

                if self.validate_game_end():
                    self.game_state.set_game_step(GameStepsEnum.STOPPED)

                if self.validate_round_end():
                    self.game_state.set_game_step(GameStepsEnum.PLAYERS_SET_UP)

                if not self.game_state.get_game_step() == GameStepsEnum.STARTED:
                    self.print_game_end()
                    break

                self.start_take()




