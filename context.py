import sys
from typing import List
from commands import *


class Context:

   def __init__(self, states: List[Abstract] = []) -> None:
      self.num_args = 0
      self.args_list = []

      # Check args list
      if str(sys.argv > 1):
         self.args_list.append(sys.argv[1:])
      #else:
     #    self.transition_to(command.help())

   def transition_to(self, state: Abstract):

      self._state = state
      self._state.context = self


