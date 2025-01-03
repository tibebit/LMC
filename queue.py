# Fabio Tiberio SM3201378
from lmc_exceptions import *

class Queue:
  def __init__(self):
    self.items = list()

  def fill(self, items):
    self.items = items

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    if self.isEmpty():
      raise EmptyInputQueueException("La coda di input è vuota")
    return self.items.pop(0)

  def isEmpty(self):
    return self.items == []

  def size(self):
    return len(self.items)
