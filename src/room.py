import imp
from src.guest import Guest

class Room:
    def __init__(self, room_number, entry_fee):
        self.room_number = room_number
        self.entry_fee = entry_fee
        self.guest = []
        self.songs = []
        self.available_places = 1

    def songs_count(self):
        return len(self.songs)

    def add_songs(self, song):
        self.songs.append(song)
    
    def guest_count(self):
        return len(self.guest)

    def add_available_spaces(self):
        self.available_places += 1

    def remove_available_spaces(self):
        self.available_places -= 1
    
    def check_in_guest(self, guest):
        if self.guest.count(guest) < self.available_places:
            self.guest.append(guest)
            self.remove_available_spaces()     
        
    def check_out_guest(self, guest):
        self.guest.remove(guest) 
        self.add_available_spaces()
       
    def guest_paying_entry_fee(self, guest):
        if guest.cash >= self.entry_fee:
            guest.cash -= self.entry_fee

    def is_guests_favourite_song_on_playlist(self, guest):
        for song in self.songs:
            if guest.favourite_song == song.title:
                return "Whoo!"

    



        