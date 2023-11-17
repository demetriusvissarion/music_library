class Track:
    def __init__(self, title=None, artist=None):
        # title and artist are both strings
        if title == None or len(title) < 1 or artist == None or len(artist) < 1:
            raise Exception("Invalid entry, 'title' and 'artist' must have at least one character.")
        else:
            self.title = title
            self.artist = artist

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        if keyword in self.title or keyword in self.artist:
            return True
        else:
            return False


# Brains Flew by Westside Gunn