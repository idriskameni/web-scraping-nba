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