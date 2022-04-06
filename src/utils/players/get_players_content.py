from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_players_content(team_link):
    """
    This functions opens a 'Chrome' browser and gets the HTML of the URL = team_link. It returns a BeautifulSoup
    element with the content of the URL mentioned before.
    :param team_link: an string with a valid link to the page of an NBA team.
    :return: It returns a BeautifulSoup object with the content of 'team_link'.
    """

    # Definition of service and driver to pull 'page_source'
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # Get the content from the indicated URL
    driver.get(team_link)

    # Wait 3 seconds to make sure that all content is properly loaded
    driver.implicitly_wait(3)

    # Transform 'page_source' to BeautifulSoup object
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Quit the driver
    driver.quit()

    # Returns the BeautifulSoup object
    return soup
