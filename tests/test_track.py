import pytest
from lib.track import *

"""
Given a keyword after adding tracks 
#matches returns true if the keyword matches either the title or artist
"""
def test_if_matches_keyword():
    track = Track('Finesse', 'Bruno Mars')
    result = track.matches("Bruno Mars")
    assert result == True


"""
Given a keyword after adding tracks 
#matches returns false if the keyword doesn't matches either the title or artist
"""
def test_if_does_not_matches_keyword():
    track = Track('Finesse', 'Bruno Mars')
    result = track.matches("Brains Flew")
    assert result == False


"""
No track
#__init__ throws error
"""
def test_throws_error_when_no_track():
    with pytest.raises(Exception) as e: 
        Track()
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'title' and 'artist' must have at least one character."


"""
Given a track with empty title or empty artist
#__init__ throws error
"""
def test_throws_error_when_empty_artist():
    with pytest.raises(Exception) as e: 
        Track('Finesse', '')
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'title' and 'artist' must have at least one character."