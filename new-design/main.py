#!/usr/bin/env python3
import os
import subprocess
import sys
import json
from random import randrange
from .classes.context import Main
from .classes.commands import ConcreteStateA



if __name__ == "__main__":

   context = Main(ConcreteStateA)
   context.request1()
   context.request2()