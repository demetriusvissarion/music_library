class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks_list = []

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        self.tracks_list.append(track)

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        self.matching_tracks = []
        for obj in self.tracks_list:
            if obj.matches(keyword):
                self.matching_tracks.append(obj)
        if len(self.matching_tracks) > 0:
            return self.matching_tracks
        else:
            raise Exception("Nothing found")
