import csv
import requests

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

    
    def fetch_api(self, account_id):
        with requests.get(API_ENDPOINT + account_id) as x:
            return x.json()
    

    def merge(self):
        self.merged_list = []
        for account in self.accounts:
            api_response = self.fetch_api(account['Account ID'])
            merged_tuple = (account['Account ID'], account['First Name'], account['Created On'], api_response['status'], api_response['created_on'])
            self.merged_list.append(merged_tuple)
        return self.merged_list

    
    def write_to_new_file(self):
        for account in self.merge():
            print account
    


