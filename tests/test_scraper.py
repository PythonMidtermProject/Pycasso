import pytest
from pycasso.scraper import get_google_images


def test_scraper_exists():
    assert get_google_images
    
#@pytest.mark.skip("Scraper can access user input")
def test_access_images():
    actual = get_google_images("dog") == True
    expected = False
    assert actual == expected
