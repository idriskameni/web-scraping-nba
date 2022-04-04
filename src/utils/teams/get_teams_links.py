def get_teams_links(standings_content):
    """

    :param standings_content:
    :return:
    """

    html_objects = standings_content.find_all('nba-stat-table')

    eastern_links = []
    western_links = []

    for object in html_objects:
        conference = str(object.get('data-title')).lower()
        if conference == 'eastern':
            table = object.find('table')
            links_list = table.find_all('td', {'class': 'nobr player desktop'})
            for link in links_list:
                eastern_links.append(
                    {
                        'team_name': str(link.find('a')).split('</a>')[0].split('-->')[-1],
                        'team_link': str(link.find('a')).split(' href="')[1].split('"')[0]
                    }
                )
        elif conference == 'western':
            table = object.find('table')
            links_list = table.find_all('td', {'class': 'nobr player desktop'})
            for link in links_list:
                western_links.append(
                    {
                        'team_name': str(link.find('a')).split('</a>')[0].split('-->')[-1],
                        'team_link': str(link.find('a')).split(' href="')[1].split('"')[0]
                    }
                )

    return eastern_links, western_links
