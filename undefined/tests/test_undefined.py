import undefined as ud
import undefined
from  undefined import Undefined as uc


def test_undefined():
    assert ud is uc



import unittest

class TestUndefined(unittest.TestCase):


  def test_bool(self):
      with self.assertRaises(NotImplementedError):
          if undefined:
              pass

  def test_str(self):
      with self.assertRaises(NotImplementedError):
          '%s' % undefined

