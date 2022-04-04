from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def get_teams_standings_content(base_url):
    """
    This functions opens a 'Chrome' browser and gets the HTML of the URL = base_url + 'standings/'. It has been built
    to be executed by passing base_url = 'https://es.global.nba.com/'.
    :param base_url: string that must be equal to 'https://es.global.nba.com/'
    :return: It returns a BeautifulSoup object with the content of 'https://es.global.nba.com/'.
    """

    # Definition of service and driver to pull 'page_source'
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # Get the content from the indicated URL
    driver.get(base_url + 'standings/')

    # Transform 'page_source' to BeautifulSoup object
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Quit the driver
    driver.quit()

    # Returns the BeautifulSoup object
    return soup
