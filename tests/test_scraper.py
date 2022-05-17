import pytest
from pycasso.scraper import Scraper


def test_scraper_exists():
    assert Scraper
    
#@pytest.mark.skip("Scraper can access user input")
def test_access_images():
        Scraper.input = lambda: 'What can I find for you?'
        # Call the function you would like to test (which uses input)
        output = Scraper.search()  
        assert output == 'What can I find for you?'
    

# @pytest.mark.parametrize('prompt',('Enter value here:'), indirect=True)
# def test_input(take_input):
 

# @pytest.mark.skip("Scraper can access user input")
#  def test_access_input():
#         pass


# @pytest.mark.skip("Scraper should send images to bot")
# def test_send_images():
#     pass

# @pytest.mark.skip("Scraper should search based off user input")
# def test_search():
#     pass