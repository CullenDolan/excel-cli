import pandas as pd
import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument("Path",
                        type=str,
                        help="path to csv to read")

my_parser.add_argument("InvoiceType",
                        nargs='?',
                        help='StarInterchange, COOP, CardPro')

my_parser.add_argument("InvoiceDate",
                        nargs='?',
                        help='format = YYYY-MM-DD')

my_parser.add_argument("FileDate",
                        nargs='?',
                        help='format = YYYY-MM-DD')

#file_date = '2022-6-1'
#invoice_date = '2022-5-1'

args = my_parser.parse_args()

input_path = args.Path.lower()
invoice_type = args.InvoiceType.lower()
file_date = args.FileDate
invoice_date = args.InvoiceDate

def process_star_int(df,file_date,invoice_date):
    try:
        print('header')
        df['BILL'] = df['BILL'] + ' ' + df['Unnamed: 8']
        df = df.drop(['Unnamed: 8'], axis = 1)
        df['FileDate'] = file_date
        df['InvoiceDate'] = invoice_date
        df.to_csv('output.csv', mode = 'a', index = False) # mode = a appends date to file
    except:
        print('no header')
        df['FileDate'] = file_date
        df['InvoiceDate'] = invoice_date
        df.to_csv('output.csv', mode = 'a', index = False) # mode = a appends date to file

if invoice_type == 'starinterchange':
    df = pd.read_fwf(input_path)
    process_star_int(df,file_date,invoice_date)



# if input_path[-4:] == '.csv':
#     df = pd.read_csv(input_path)
# elif input_path[-5:] == '.xlsx':
#     df = pd.read_excel(input_path)
# elif input_path[-4:] == '.txt':
#     df = pd.read_csv(input_path)
# else:
#     print('{} is not a valid file type'.format(input_path))
# print(df.head())