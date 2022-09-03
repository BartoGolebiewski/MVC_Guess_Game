
import model
from model import *


def print_menu():
   print("Welcome to the PENDANT, What you want to do?")
   print("1. Start a game")
   print("2. Exit")

def get_players_count():
   return int(input("How many players will be playing?\n"))

def enter_name():
   input(">Enter name: ")

def view_round_controller(self):
   print("Guess: {Guess}".format(Guess=self.get_guess_word_from_choices()))
   print("Turn player: {Player} ".format(Player=self.get_current_player().name))
   print("What do you want to do?")
   print("1. Select a letter")
   print("2. Guess the keyword")
   [print(
      "{PlayerName} ma punktow {Points} i zyc {Lifes}".format(PlayerName=player.name, Points=player.score_point,
                                                              Lifes=player.lifes)) for player in self.players]

def choose_letter(self):
   input(">Player {Player} choose letter: ".format(Player=self.get_current_player().name))

def guessed_letter(self):
   print("Good one {Player}, you get a point. In this round you have: {Temp_point} ".format(
      Player=self.get_current_player().name, Temp_point=self.get_current_player().temp_point))

def missed_letter(self):
   print("Nope, {Player} you missed ".format(Player=self.get_current_player().name))

def guessing_word(self):
   input(">Player {Player} guess word: ".format(Player=self.get_current_player().name))

def guessed_word(self):
   print("Good one {Player}! You guess the word, when your scorepoint is increase about your temp point".format(
      Player=self.get_current_player().name))

def missed_word(self):
   print("Nope, {Player} loses one life".format(Player=self.get_current_player().name))

def player_is_out(self):
   print("{Player} odpada bo jest slaby".format(Player=self.get_current_player().name))


def display(self):
   print("Player: ", self.name)
   print("Score point: ", self.score_point)
   print("{Player} have {Lifes}".format(Player=self.name, Lifes=self.lifes))

def choose(self):
   input(">> Choose: ")