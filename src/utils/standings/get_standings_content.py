from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def get_standings_content(base_url):
    """

    :return:
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

    # Return the BeautifulSoup object
    return soup