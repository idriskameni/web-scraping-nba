import pandas as pd


def create_list_of_players_dataset(list_of_players_content):


    i = 0

    # creat an empty list called tables
    tables = []

    # Find de table inspecting the url
    html_tables = list_of_players_content.find_all('div', {'class': 'nba-stat-table__overflow'})

    # Creat team tables
    for html_table in html_tables:
        table = html_table.find('table')
        tables.append(pd.read_html(str(table))[0])

    unique_tables = [tables[x] for x, y in enumerate(tables) if tables[x].equals(tables[x - 1]) is False]

    # Creat csv file with team and players information
    for table in tables:
        table.to_csv('..\\..\\docs\\teams\\team_' + str(i) + '.csv', sep=',', index=False, encoding='utf-8-sig')

        i += 1
