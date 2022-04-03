from sys import path
path.append('../../')

from src.utils.standings.get_standings_content import get_standings_content
from src.utils.standings.create_standings_datasets import create_standings_datasets
from src.utils.teams.get_teams_links import get_teams_links
from src.utils.players.get_list_of_players_content import get_list_of_players_content
from src.utils.players.create_list_of_players_dataset import create_list_of_players_dataset


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
    final_list = []

    # Get link from each team
    for link in teams_links:

        splitted_link = link.split('/')

        url = base_url + splitted_link[1] + '/roster/' + splitted_link[2] + '/' + splitted_link[3]

        list_of_players_content = get_list_of_players_content(url)

        final_list.append(create_list_of_players_dataset(list_of_players_content))


if __name__ == "__main__":
    web_scraping_nba()