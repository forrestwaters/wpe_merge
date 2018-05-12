import csv
import requests
from account import Account

class WpeMerge(object):
    """
    Account ID, First Name, Created On, Status, Status Set On
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    
    def parse_csv(self):
        with open(self.input_file) as csv_file:
            reader = csv.DictReader(csv_file)
            accounts = []
            for row in reader:
                accounts.append(row)
            return accounts
    

test = WpeMerge('sample.csv', 'test').parse_csv()
for account in test:
    print Account(account)
    

