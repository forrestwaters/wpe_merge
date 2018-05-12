import csv
import requests
from account import Account

API_ENDPOINT = "http://interview.wpengine.io/v1/accounts/"


class WpeMerge(object):
    """
    Account ID, First Name, Created On, Status, Status Set On
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.parse_csv()
        self.merge()

    
    def parse_csv(self):
        with open(self.input_file) as csv_file:
            reader = csv.DictReader(csv_file)
            self.accounts = []
            for row in reader:
                self.accounts.append(row)
            return self.accounts
    
    def merge(self):
        self.merged_list = []
        for account in self.accounts:
            x = Account(account)
            self.merged_list.append(x.__dict__)
        return self.merged_list
    

test = WpeMerge("sample.csv", "test")
print(test.merged_list)