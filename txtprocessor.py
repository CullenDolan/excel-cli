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
        df['BILL'] = df['BILL'] + ' ' + df['Unnamed: 8']
        df = df.drop(['Unnamed: 8'], axis = 1)
        df['FileDate'] = file_date
        df['InvoiceDate'] = invoice_date
        df.to_csv('output.csv', mode = 'a', index = False) # mode = a appends date to file
    except:
        print('no header')
        df['FileDate'] = file_date
        df['InvoiceDate'] = invoice_date
        df.to_csv('output.csv', mode = 'a', index = False) 

def process_coop_int(df,file_date,invoice_date):
    df['BILL'] = df['BILL'] + df['Unnamed: 3']
    df = df.drop(['Unnamed: 3'], axis = 1)
    df.to_csv('output.csv', mode = 'a', index = False) 

if invoice_type == 'starint':
    df = pd.read_fwf(input_path)
    process_star_int(df,file_date,invoice_date)

elif  invoice_type == 'coopint':
    df = pd.read_fwf(input_path)
    process_coop_int(df,file_date,invoice_date)