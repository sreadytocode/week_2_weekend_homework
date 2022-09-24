import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ellen Ripley", 200.00, "I Will Survive")

    def test_guest_has_a_name(self):
        self.assertEqual("Ellen Ripley", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(200.00, self.guest.cash)

    def test_guest_has_a_favourite_song(self):
        self.assertEqual("I Will Survive", self.guest.favourite_song)
