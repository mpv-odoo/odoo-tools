from abc import ABC, abstractmethod
from .context import Context


class Abstract(ABC):

   @abstractmethod
   def __init__(self, name: str) -> None:
      self._name = name

   @property
   def context(self) -> Context:
      return self._context

   @property
   def name(self) -> str:
      return self._name

   @context.setter
   def context(self, context: Context) -> None:
      self._context = context

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



class Help(Abstract):

   def print_help(self)-> None:
      print('Init Help')

   def run(self) -> None:
      print('Running Init ')