def save_dataframe(list_of_dataframes, package_location):
    """
    This function saves as CSV files each of the dataframes in the list 'list_of_dataframes' in the path
    within the 'docs' folder specified in 'package_location'. It adds the 'easter', 'western' value at the
    end of the path to differentiate between both conferences (obtained from the column 'Conference' of the
    inputed dataframe).
    :param list_of_dataframes: list of datraframes to be saved.
    :param package_location: path within 'docs' folder to place the output.
    :return: Not applicable.
    """

    # Loop through all the dataframes in the list 'list_of_dataframes'
    for dataframe in list_of_dataframes:

        # Identify the conference of the dataset and save it in the variable 'conference'
        conference = dataframe['Conference'].unique()[0]

        # Save the dataframe using the indicated path followed by the 'conference'
        dataframe.to_csv(
            '..\\..\\docs\\' + package_location + '_' + str(conference).lower() + '_conference.csv',
            sep=',',
            index=False,
            encoding='utf-8-sig'
        )
