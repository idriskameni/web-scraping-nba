import pandas as pd


def create_players_datasets(list_of_players_content):
    """

    :param list_of_players_content:
    :return:
    """

    # Create an empty list called tables
    tables = []

    # Find de table inspecting the url
    html_tables = list_of_players_content.find_all('div', {'class': 'nba-stat-table__overflow'})

    # Create team tables
    for html_table in html_tables:
        table = html_table.find('table')
        tables.append(pd.read_html(str(table))[0])

    unique_tables = [tables[x] for x, y in enumerate(tables) if tables[x].equals(tables[x - 1]) is False]

    return unique_tables[0], unique_tables[1]