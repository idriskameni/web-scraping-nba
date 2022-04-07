def get_teams_links(standings_content):
    """
    This function has the aim of identifying all NBA teams' links from the standings table. It needs to get as an input
    the HTML content for the standings and it returns a list with the links to each of the NBA websites of each team. The
    input needs to be the output of 'src/utils/teams/get_teams_standings_content.py'.
    :param standings_content: Beautiful soupt element with the HTML content of standings' NBA website.
    :return: two list of teams' links (one per conference).
    """

    # Create two empty lists called 'eastern_links', 'western_links' to append the links
    eastern_links = []
    western_links = []

    # Find all elements in HTML object that are of type <nba-stat-table ...>
    html_objects = standings_content.find_all('nba-stat-table')

    # Loop through each 'nba-stat-table' to identify the tables, links and append them to 'eastern_links' or 'western_links'
    for html_object in html_objects:

        # Identify the conference
        conference = str(html_object.get('data-title')).lower()

        # If conference is 'eastern', identify links and add them to 'eastern_links'
        if conference == 'eastern':

            # Identify the table within the selected class
            table = html_object.find('table')

            # Identify the element within the table containing the team link
            links_list = table.find_all('td', {'class': 'nobr player desktop'})

            # For each element in the list of elements containing the links, identify clean link and append to 'eastern_links'
            for link in links_list:
                eastern_links.append(
                    {
                        'team_name': str(link.find('a')).split('</a>')[0].split('-->')[-1],
                        'team_link': str(link.find('a')).split(' href="')[1].split('"')[0]
                    }
                )

        # If conference is 'western', identify links and add them to 'western_links'
        elif conference == 'western':

            # Identify the table within the selected class
            table = html_object.find('table')

            # Identify the element within the table containing the team link
            links_list = table.find_all('td', {'class': 'nobr player desktop'})

            # For each element in the list of elements containing the links, identify clean link and append to 'western_links'
            for link in links_list:
                western_links.append(
                    {
                        'team_name': str(link.find('a')).split('</a>')[0].split('-->')[-1],
                        'team_link': str(link.find('a')).split(' href="')[1].split('"')[0]
                    }
                )

    # Return list of dictionaries with 'team_name' and 'team_link' as attributes of each element
    return eastern_links, western_links
