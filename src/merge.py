import csv
import requests

API_ENDPOINT = "http://interview.wpengine.io/v1/accounts/"


class WpeMerge(object):
    """
    Given a csv file with the following columns:
    Account ID,Account Name,First Name,Created On

    Fetch an api that will have the following fields:
    Account ID,Status, Status Set On

    Merge this data to a new csv with the following fields:
    Account ID, First Name, Created On, Status, Status Set On
    """

    def __init__(self, output_file):
        """
        :param output_file: file that we will write our merged data to
        """
        self.output_file = output_file

    def parse_csv(self, csv_file):
        """
        Parse the csv as an OrderedDict.
        :return: list of dicts for each account.
        """
        reader = csv.DictReader(csv_file)
        self.accounts = [row for row in reader]
        return self.accounts

    def fetch_api(self, account_id):
        """
        :param: pass an account_id
        :return: json (dict) response from the api
        """
        with requests.get(API_ENDPOINT + account_id) as x:
            if x.status_code == 200:
                return x.json()
            else:
                pass

    def merge(self, csv_file):
        """
        Parse the csv; for each account id, hit the API and merge the data
        :return: list of dictionaries for each account id
        """
        self.parse_csv(csv_file)
        self.merged_list = []
        for entry in self.accounts:
            api_response = self.fetch_api(entry['Account ID'])
            if api_response is not None:
                entry['Status'] = api_response['status']
                entry['Status Set On'] = api_response['created_on']
                self.merged_list.append(entry)
        return self.merged_list

    def write_to_new_file(self, csv_file):
        """
        Call merge() and write the merged data to our output_file
        """
        self.merge(csv_file)
        with open(self.output_file, 'w') as csvfile:
            fieldnames = "Account ID", "First Name", "Created On", "Status", "Status Set On"
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in self.merged_list:
                del entry['Account Name']  # Account name doesn't need to be written to the new csv
                writer.writerow(entry)
