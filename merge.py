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

    
    def parse_csv(self):
        with open(self.input_file) as csv_file:
            reader = csv.DictReader(csv_file)
            self.accounts = [row for row in reader]
            return self.accounts

    
    def fetch_api(self, account_id):
        with requests.get(API_ENDPOINT + account_id) as x:
            return x.json()
    

    def merge(self):
        self.parse_csv()
        self.merged_list = []
        for entry in self.accounts:
            api_response = self.fetch_api(entry['Account ID'])
            entry['Status'] = api_response['status']
            entry['Status Set On'] = api_response['created_on']
            self.merged_list.append(entry)
        return self.merged_list

    
    def write_to_new_file(self):
        self.merge()
        with open(self.output_file, 'w') as csvfile:
            fieldnames = "Account ID", "First Name", "Created On", "Status", "Status Set On"
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in self.merged_list:
                del entry['Account Name'] # Account name doesn't need to be written to the new csv
                writer.writerow(entry)

