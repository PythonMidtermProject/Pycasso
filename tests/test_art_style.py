import pytest
from pycasso.art_style import choice


def test_choice():
    assert choice


# @pytest.mark.skip("Scraper can access user input")
def test_van_gogh():
    actual = choice('van gogh')
    expected = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1024px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg'
    assert actual == expected
