import pandas as pd
from sys import path
path.append('../../')
from src.utils.teams.get_teams_standings_content import get_teams_standings_content
from src.utils.teams.create_teams_standings_datasets import create_teams_standings_datasets
from src.utils.teams.get_teams_links import get_teams_links
from src.utils.players.get_players_content import get_players_content
from src.utils.players.create_players_datasets import create_players_datasets
from src.utils.generic.save_dataframe import save_dataframe


def web_scraping_nba():
    """
    Finish documentation.
    :return:
    """

    # Definition of base URL
    base_url = 'https://es.global.nba.com/'

    # Get the standings content
    standings_content = get_teams_standings_content(base_url)

    # Create standings datasets
    list_of_standings_datasets = create_teams_standings_datasets(standings_content)

    # Save standings datasets
    save_dataframe(list_of_standings_datasets, 'teams_standings\\teams_standing')

    # Get teams links
    eastern_teams_links, western_teams_links = get_teams_links(standings_content)

    eastern_list_of_list_of_players_datasets = []
    eastern_list_of_stats_of_players_datasets = []
    western_list_of_list_of_players_datasets = []
    western_list_of_stats_of_players_datasets = []

    for link in eastern_teams_links + western_teams_links:

        splitted_link = link['team_link'].split('/')
        url = base_url + splitted_link[1] + '/roster/' + splitted_link[2] + '/' + splitted_link[3]

        list_of_players_content = get_players_content(url)
        stats_of_players_dataset, list_of_players_dataset = create_players_datasets(list_of_players_content)

        stats_of_players_dataset['Team'] = link['team_name']
        list_of_players_dataset['Team'] = link['team_name']

        if link['team_link'] in [link['team_link'] for link in eastern_teams_links]:
            stats_of_players_dataset['Conference'] = 'Eastern'
            list_of_players_dataset['Conference'] = 'Eastern'
            eastern_list_of_stats_of_players_datasets.append(stats_of_players_dataset)
            eastern_list_of_list_of_players_datasets.append(list_of_players_dataset)
        elif link['team_link'] in [link['team_link'] for link in western_teams_links]:
            stats_of_players_dataset['Conference'] = 'Western'
            list_of_players_dataset['Conference'] = 'Western'
            western_list_of_stats_of_players_datasets.append(stats_of_players_dataset)
            western_list_of_list_of_players_datasets.append(list_of_players_dataset)

    eastern_stats_of_players_datasets = pd.concat(eastern_list_of_stats_of_players_datasets)
    eastern_list_of_players_datasets = pd.concat(eastern_list_of_list_of_players_datasets)
    western_stats_of_players_datasets = pd.concat(western_list_of_stats_of_players_datasets)
    western_list_of_players_datasets = pd.concat(western_list_of_list_of_players_datasets)

    save_dataframe(
        [eastern_stats_of_players_datasets.drop_duplicates(), western_stats_of_players_datasets.drop_duplicates()],
        'players_stats\\players_stats'
    )
    save_dataframe(
        [eastern_list_of_players_datasets.drop_duplicates(), western_list_of_players_datasets.drop_duplicates()],
        'players_list\\players_list'
    )


if __name__ == "__main__":
    web_scraping_nba()
