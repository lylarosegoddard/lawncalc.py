import unittest
from app.lawn import Lawn

class TestLawn(unittest.TestCase):
  def test_area_takes_away_some_stuff(self):
      lawn = Lawn(4, 5, 1.5)
      self.assertEqual (12.93, lawn.area())


