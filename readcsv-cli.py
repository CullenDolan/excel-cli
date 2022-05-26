import pandas as pd
import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument("Path",
                        type=str,
                        help="path to csv to read")

my_parser.add_argument("Invoicetype",
                        nargs='?',
                        help='StarInterchange, Others?')

args = my_parser.parse_args()

input_path = args.Path

if args.Path[-4:] == '.csv':
    df = pd.read_csv(input_path)
    print(df.head())
elif args.Path[-5:] == '.xlsx':
    df = pd.read_excel(input_path)
    print(df.head())
elif args.Path[-4:] == '.txt':
    df = pd.read_csv(input_path)
    print(df.head())
else:
    print('{} is not a valid file type'.format(input_path))