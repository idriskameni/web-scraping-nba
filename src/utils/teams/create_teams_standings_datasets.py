import pandas as pd

def create_teams_standings_datasets(standings_content):
    """

    :param standings_content:
    :return:
    """

    tables = []

    html_objects = standings_content.find_all('nba-stat-table')

    for object in html_objects:
        conference = object.get('data-title')
        table = object.find('table')
        df_table = pd.read_html(str(table))[0]
        df_table['Conference'] = conference
        tables.append(df_table)

    unique_tables = [tables[x] for x, y in enumerate(tables) if tables[x].equals(tables[x - 1]) is False]

    return unique_tables
