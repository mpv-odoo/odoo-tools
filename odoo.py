#!/usr/bin/env python3

#import Context.context as context
from abc import ABC, abstractmethod
from typing import List
import sys

class Context:

   _state = None

   def __init__(self) -> None:
      self.num_args = 0
      self.args_list = []
      # Check args list
      if str(sys.argv > 1):
         self.args_list.append(sys.argv[1:])
      #else:
     #    self.transition_to(command.help())

   def transition_to(self, state):

      self._state = state
      self._state.context = self



class Abstract(ABC):

   @abstractmethod
   def __init__(self, name: str) -> None:
      self._name = name

   @property
   def context(self) -> Context:
      return self._context

   @context.setter
   def context(self, context: Context) -> None:
      self._context = context

   @property
   def name(self) -> str:
      return self._name



   @abstractmethod
   def print_help(self) -> None:
      pass

   @abstractmethod
   def run(self) -> None:
      pass

class Help(Abstract):

   def print_help(self) -> None:
      print('Help help')

   def run(self) -> None:
      print('Running Help ')



class Init(Abstract):

   def print_help(self)-> None:
      print('Init Help')

   def run(self) -> None:
      print('Running Init ')


if __name__ == "__main__":
   print('hello')