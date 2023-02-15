import pandas as pd

import file_parser

input_filename = input("Hi, please enter the filepath to the Philantro transaction file\n")
output_filename = input("Please add the output filepath (e.g. user/documents/giftaidschedule2022)\n")

def handle(input_filename):
    df = pd.read_csv(input_filename)
    file_parser.filter_giftaid_and_international_donors(df)
    df = file_parser.filter_and_format_columns(df)
    file_parser.add_required_empty_columns(df)
    print(df)
    df.to_csv(f'{output_filename}.csv')

handle(input_filename)