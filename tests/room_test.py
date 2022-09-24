import unittest
from src.room import Room
from src.guest import Guest
from src.songs import Songs


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 5.00)
        self.songs_1 = Songs("I Will Survive", "Gloria Gaynor")
        self.songs_2 = Songs("I'll Be Back", "The Beatles")
        self.songs_3 = Songs("Walking on Sunshine", "Katrina And The Waves")
        self.guest_1 = Guest("Ellen Ripley", 10.00, "I Will Survive")
        self.guest_2 = Guest("The Terminator", 2.00, "I'll Be Back")

    def test_room_has_room_numbers(self):
        self.assertEqual(1, self.room.room_number)
   
    def test_room_has_entry_fee(self):
        self.assertEqual(5.00, self.room.entry_fee)
    
    def test_room_has_available_spaces(self):
        self.assertEqual(1, self.room.available_places)
    
    def test_room_can_add_songs(self):
        self.room.add_songs(self.songs_3)
        self.assertEqual(1, self.room.songs_count())

    def test_room_can_add_available_spaces(self):
        self.room.add_available_spaces()
        self.assertEqual(2, self.room.available_places)

    def test_room_can_remove_available_spaces(self):
        self.room.remove_available_spaces()
        self.assertEqual(0, self.room.available_places)
    
    def test_check__in_guests_to_room(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())
        self.assertEqual(0, self.room.available_places)

    def test_check__out_guests_to_room(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room.guest_count())
        self.assertEqual(1, self.room.available_places)
    
    def test__less_guests_than_available_spaces(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())
        self.assertEqual(0, self.room.available_places)

    def test__more_guests_than_available_spaces(self):
        self.room.remove_available_spaces()
        self.assertEqual(0, self.room.guest_count())
        self.assertEqual(0, self.room.available_places)

    def test__guest_has_sufficient_funds_to_pay_entry_fee(self):
        self.room.guest_paying_entry_fee(self.guest_1)
        self.assertEqual(5.00, self.guest_1.cash)
    
    def test__guest_has_insufficient_funds_to_pay_entry_fee(self):
        self.room.guest_paying_entry_fee(self.guest_2)
        self.assertEqual(2.00, self.guest_2.cash)

    def test__guests_favourite_song_is_on_the_playlist(self):
        self.room.add_songs(self.songs_1)
        self.room.check_in_guest(self.guest_1)
        result = self.room.is_guests_favourite_song_on_playlist(self.guest_1)
        self.assertEqual("Whoo!", result)

    def test__guests_favourite_song_is_not_on_the_playlist(self):
         self.room.add_songs(self.songs_3)
         self.room.check_in_guest(self.guest_2)
         result = self.room.is_guests_favourite_song_on_playlist(self.guest_2)
         self.assertEqual(None, result)
