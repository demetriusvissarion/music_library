class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        pass

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        pass

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        pass

# class Tracks:
#     # User-facing properties:
#     #   name: string

#     def __init__(self, name): 
#         # Parameters:
#         #   name: string
#         # Side effects:
#         #   self.tracks_list = {}
#         self.name = name
#         self.tracks_list = {}

#     def add_tracks(self, track):
#         # Parameters:
#         #   track: string representing a single track
#         # Returns:
#         #   Nothing
#         # Side-effects
#         #   Saves the track to the self.tracks_list
#         if len(track) > 0:
#             # if key/value exists append to value, else create key/value
#             self.tracks_list.setdefault(self.name, []).append(track)
#             print("Track was added to your list")
#         else:
#             raise Exception("No track saved.")

#     def show_tracks(self):
#         # Returns:
#         #   self.tracks_list
#         if self.tracks_list.get(self.name) != None:
#             return ', '.join(self.tracks_list[self.name])
#         else:
#             raise Exception("No track saved.")