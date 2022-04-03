import pandas as pd

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
        table.to_csv('..\\..\\docs\\standings\\nba_standing_conference_' + str(i) + '.csv', sep=',', index=False, encoding='utf-8-sig')
        i += 1

