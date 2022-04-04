def save_dataframe(list_of_dataframes, package_location):

    i = 0

    for dataframe in list_of_dataframes:
        conference = dataframe['Conference'].unique()[0]

        dataframe.to_csv(
            '..\\..\\docs\\' + package_location + '_' + str(conference).lower() + '_conference.csv',
            sep=',',
            index=False,
            encoding='utf-8-sig'
        )

        i += 1
