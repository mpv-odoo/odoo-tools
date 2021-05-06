from __future__ import annotations
from abc import ABC, abstractmethod
from .context import Main

class State(ABC):
   def context(self) -> Main:
      return self._context

   @context.setter
   def context(self, context: Main) -> None:
      self._context = context

   @abstractmethod
   def handle1(self) -> None:
      pass

   @abstractmethod
   def handle2(self) -> None:
      pass


class ConcreteStateA(State):
   def handle1(self) -> None:
      print("ConcreteStateA handles request1.")
      print("ConcreteStateA wants to change the state of the context.")
      self.context.transition_to(ConcreteStateB())

def handle2(self) -> None:
   print("ConcreteStateA handles request2.")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())
