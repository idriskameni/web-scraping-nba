from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

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


def get_teams_links(standings_content):
    """

    :param standings_content:
    :return:
    """
    html_tables = standings_content.find_all('div', {'class': 'nba-stat-table__overflow'})

    links = []

    for html_table in html_tables:
        table = html_table.find('table')
        links_list = table.find_all('td', {'class': 'nobr player desktop'})

        for link in links_list:
            links.append(str(link.find('a')).split(' href="')[1].split('"')[0])

    return links


def create_standings_datasets(standings_content):
    """

    :param standings_content:
    :return:
    """

    i = 0
    tables = []

    html_tables = standings_content.find_all('div', {'class': 'nba-stat-table__overflow'})

    for html_table in html_tables:
        table = html_table.find('table')
        tables.append(pd.read_html(str(table))[0])

    unique_tables = [tables[x] for x, y in enumerate(tables) if tables[x].equals(tables[x - 1]) is False]

    for table in unique_tables:
        table.to_csv('..\\..\\docs\\standings\\standing_conference_' + str(i) + '.csv', sep=',', index=False, encoding='utf-8-sig')
        i += 1

"""
def get_list_of_players_content(list_of_teams_links):
    print('To be finished')
    return 1

def create_list_of_players_dataset(list_of_players_content):
    print('To be finished')
    
def get_players_stats_content(list_of_teams_links):
    print('To be finished')
    return 1

def create_players_stats_dataset(players_stats_content):
    print('To be finished')
"""


def web_scraping_nba():
    """

    :return:
    """

    # Definition of base URL
    base_url = 'https://es.global.nba.com/'

    # Get the standings content
    standings_content = get_standings_content(base_url)

    # Create standings datasets
    create_standings_datasets(standings_content)

    # Get teams' links
    teams_links = get_teams_links(standings_content)

    """
    # Get list of players content
    list_of_players_content = get_list_of_players_content(teams_links)
    
    # Create list of players dataset
    create_list_of_players_dataset(list_of_players_content)

    # Get players' stats content
    list_of_players_content = get_list_of_players_content(teams_links)
    
    # Create players' stats dataset
    create_list_of_players_dataset(list_of_players_content)
    """


if __name__ == "__main__":
    web_scraping_nba()