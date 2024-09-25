# Quinten Reed
# U2L2
# DynamicArray

import ctypes

class DynamicArray():
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)

  def __len__(self):
    return self.__n

  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
      raise IndexError("invalid index")
    
    return self.__A[k]

  def __str__(self):
    if self.__n == 0:
      return "[]"

    out = '['
    for i, element in enumerate(self.__A):
      try:
        out += str(element) + ', '
        temp = self.__A[i+1]
      except:
        break
    return out[:-2] + ']'

  def append(self, element):
    if self.__n >= self.__capacity:
      self.__A = self.__resize()

    self.__A[self.__n] = element
    self.__n += 1

  def get_cap(self):
    return self.__capacity

  def __resize(self):
    self.__capacity *= 2

    new_list = (self.__capacity * ctypes.py_object)()

    for i in range(self.__n):
      new_list[i] = self.__A[i]

    return new_list

  def __make_array(self, c):
    """return new array with capacity c"""
    return (c * ctypes.py_object)()