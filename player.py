import math
import random

class Player:
  def __init__(self, letter):
    # letter is x or o
    self.letter = letter

  # we want players to get their next move
  def get_move(self, game):
    pass

class RandomComputerPlayer(Player):
  def __init__(self, letter): 
    super().__init__(letter) # super() accesses the parent class Player for the .__init__ method and calls it with the variable letter
  def get_move(self, game):
    square = random.choice(game.available_moves()) # get random, valid spot
    return square

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    valid_square = False
    val = None
    while not valid_square:
      square = input(self.letter + '\'s turn. Input move (0-8): ')
      # check for correct value by trying to cast it to an integer
      # if it is not an integer, we say invalid
      # if the spot is not available on the board, we say invalid
      try:
        val = int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square = True # only if the above work/pass
      except ValueError:
        print('Invalid square. Please try again.')
    
    return val
