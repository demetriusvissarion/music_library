import pytest
from unittest.mock import Mock
from lib.music_library import *

"""
Adding a track object
#add Track gets added to the library (Returns nothing)
"""
def test_mock_if_adds_track():
    music_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.title = 'Finesse'
    fake_track1.artist = 'Bruno Mars'
    music_library.add(fake_track1)
    result = music_library.tracks_list[0].title
    assert result == 'Finesse'


"""
Searching a keyword in the tracks_list objects and finding it
#search Returns a list of instances of track that match the keyword
"""
def test_mock_if_searches_keyword_and_finds_it():
    music_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.title = 'Finesse'
    fake_track1.artist = 'Bruno Mars'
    fake_track1.matches.return_value = True
    music_library.add(fake_track1)
    matching_track_titles = music_library.search('Finesse')[0].title
    assert matching_track_titles == 'Finesse'


"""
Searching a keyword in the tracks_list objects and not finding it
#search throws an error
"""
def test_mock_if_searches_keyword_and_does_not_find_it():
    music_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.title = 'Finesse'
    fake_track1.artist = 'Bruno Mars'
    fake_track1.matches.return_value = False
    music_library.add(fake_track1)
    with pytest.raises(Exception) as e: 
        music_library.search('dfgdfgdf')
    error_message = str(e.value)
    assert error_message == "Nothing found"


# Brains Flew by Westside Gunn