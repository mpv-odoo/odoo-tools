from .commands import State, ConcreteStateA

class Main:

   def __init__(self, state: State) -> None:
      self.transition_to(state)

   def transition_to(self, state: State):
      self._state = state
      self._state.context = self

   def request1(self):
      self._state.handle1()

   def request2(self):
      self._state.handle2()