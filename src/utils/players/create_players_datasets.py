import pandas as pd


def create_players_datasets(list_of_players_content):
    """
    This function extracts two tables located within the BeautifulSoup element 'list_of_players_content' (which
    needs to be the output of '../src/players/get_players_content.py'). It returns a tuple with two dataframes with
    information about the players of a team.
    :param list_of_players_content: BeautifulSoup element containing the website content where the tables are
    (for a single team).
    :return: Returns a tuple with two dataframes:
    1) stats of players for that specific team;
    2) list of players for that specific team.
    """

    # Create an empty list called tables
    tables = []

    # Find all elements in HTML object that are of type <div> with class 'nba-stat-table__overflow'
    html_tables = list_of_players_content.find_all('div', {'class': 'nba-stat-table__overflow'})

    # Loop through each 'div' to identify the tables and append them to 'tables'
    for html_table in html_tables:
        table = html_table.find('table')
        tables.append(pd.read_html(str(table))[0])

    # Remove duplicates from the list of tables
    unique_tables = [tables[x] for x, y in enumerate(tables) if tables[x].equals(tables[x - 1]) is False]

    # Return stats of players and list of players dataframes
    return unique_tables[0], unique_tables[1]
