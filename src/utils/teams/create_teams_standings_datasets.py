import pandas as pd


def create_teams_standings_datasets(standings_content):
    """
    This function extracts two tables located within the BeautifulSoup element 'standings_content' (which needs
    to be the output of '../src/players/get_teams_standings_content.py'). It returns a list with two dataframes
    with information about the standings of the 'eastern' and 'western' NBA conferences.
    :param standings_content: BeautifulSoup element containing the website content where the tables are.
    :return: Returns a list with two dataframes:
    1) standings of the 'eastern' conference;
    2) standings of the 'western' conference;
    """

    # Create an empty list called tables
    tables = []

    # Find all elements in HTML object that are of type <nba-stat-table ...>
    html_objects = standings_content.find_all('nba-stat-table')

    # Loop through each 'nba-stat-table' to identify the tables and append them to 'tables'
    for html_object in html_objects:
        conference = html_object.get('data-title')
        table = html_object.find('table')
        df_table = pd.read_html(str(table))[0]
        df_table['Conference'] = conference
        tables.append(df_table)

    # Remove duplicates from the list of tables
    unique_tables = [tables[x] for x, y in enumerate(tables) if tables[x].equals(tables[x - 1]) is False]

    # Return list of teams standings dataframes
    return unique_tables
