import pandas as pd

def add_required_empty_columns(df):
    '''Adds empty columns that are in the giftaid schedule'''
    empty_col = pd.DataFrame([''] * len(df))
    df.insert(0, 'Title', empty_col)
    df.insert(5, 'Aggregated Donations', empty_col)
    df.insert(6, 'Sponsored Event', empty_col)

def filter_giftaid_and_international_donors(df):
    '''Deletes any donors that have declined adding giftaid in Philantro and international donors'''
    df.drop(df.loc[df['Gift Aid Flag'] == False].index, inplace=True)
    df.loc[df['Country'] != 'GB', 'Postcode'] = 'X'

def filter_and_format_columns(df):
    '''Filters relevant columns for gift aid schedule, ensures street line address is max 39 characters and formats postcode to include space if missing'''
    df['Street Address Line 1'] = df['Street Address Line 1'].str[:39]
    df = df[['First Name', 'Last Name', 'Street Address Line 1', 'Postcode', 'Created', 'Amount']]
    df.loc[~df['Postcode'].str.contains(' '), 'Postcode'] = df['Postcode'].str[:-3] + ' ' + df['Postcode'].str[-3:]
    return df
