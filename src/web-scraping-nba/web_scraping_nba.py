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
    This functions uses all functions available in 'src/utils' to generate 6 datasets related to the National Basketball
    League (or NBA) which are then stored in 'docs' folder. The 6 generated datasets contain data about NBA teams' standings,
    NBA players' lists and NBA players' stats. Each of these 3 categories is divided into two, one by conference ('EAST',
    'WEST'). The folders containing these datasets are: 'docs/players_list', 'docs/players_stats' and 'docs/teams_standings'.
    :return: Not applicable.
    """

    # Definition of base URL
    base_url = 'https://es.global.nba.com/'

    # Get the standings content
    standings_content = get_teams_standings_content(base_url)

    # Create standings datasets
    list_of_standings_datasets = create_teams_standings_datasets(standings_content)

    # Save standings datasets
    save_dataframe(list_of_standings_datasets, 'teams_standings\\teams_standing')

    # Get teams links by conference
    eastern_teams_links, western_teams_links = get_teams_links(standings_content)

    # Initialize players lists and stats datasets by conference
    eastern_list_of_list_of_players_datasets = []
    eastern_list_of_stats_of_players_datasets = []
    western_list_of_list_of_players_datasets = []
    western_list_of_stats_of_players_datasets = []

    # Loop through each team's link to get the list of players and stats and append it to the earlier defined lists
    for link in eastern_teams_links + western_teams_links:

        # Split the team's link to generate the URL which contains the data about team players
        splitted_link = link['team_link'].split('/')
        url = base_url + splitted_link[1] + '/roster/' + splitted_link[2] + '/' + splitted_link[3]

        # Get the players content
        list_of_players_content = get_players_content(url)

        # Create players datasets (both stats and list of players)
        stats_of_players_dataset, list_of_players_dataset = create_players_datasets(list_of_players_content)

        # Add the name of the team to the datasets
        stats_of_players_dataset['Team'] = link['team_name']
        list_of_players_dataset['Team'] = link['team_name']

        # If the 'team_link' is part of the list of teams from 'EAST', add the datasets to the 'eastern' lists
        if link['team_link'] in [link['team_link'] for link in eastern_teams_links]:

            # Add the name of the conference the team belongs to
            stats_of_players_dataset['Conference'] = 'Eastern'
            list_of_players_dataset['Conference'] = 'Eastern'

            # Append players datasets
            eastern_list_of_stats_of_players_datasets.append(stats_of_players_dataset)
            eastern_list_of_list_of_players_datasets.append(list_of_players_dataset)

        # If the 'team_link' is part of the list of teams from 'EAST', add the datasets to the 'eastern' lists
        elif link['team_link'] in [link['team_link'] for link in western_teams_links]:

            # Add the name of the conference the team belongs to
            stats_of_players_dataset['Conference'] = 'Western'
            list_of_players_dataset['Conference'] = 'Western'

            # Append players datasets
            western_list_of_stats_of_players_datasets.append(stats_of_players_dataset)
            western_list_of_list_of_players_datasets.append(list_of_players_dataset)

    # Concatenate the datasets from all teams in a unique dataset
    eastern_stats_of_players_datasets = pd.concat(eastern_list_of_stats_of_players_datasets)
    eastern_list_of_players_datasets = pd.concat(eastern_list_of_list_of_players_datasets)
    western_stats_of_players_datasets = pd.concat(western_list_of_stats_of_players_datasets)
    western_list_of_players_datasets = pd.concat(western_list_of_list_of_players_datasets)

    # Save players' stats datasets
    save_dataframe(
        [eastern_stats_of_players_datasets.drop_duplicates(), western_stats_of_players_datasets.drop_duplicates()],
        'players_stats\\players_stats'
    )

    # Save players' stats datasets
    save_dataframe(
        [eastern_list_of_players_datasets.drop_duplicates(), western_list_of_players_datasets.drop_duplicates()],
        'players_list\\players_list'
    )


if __name__ == "__main__":
    web_scraping_nba()
