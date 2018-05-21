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

    def parse_csv(self, input_file):
        """
        Parse the csv as an OrderedDict.
        :return: list of dicts for each account.
        """
        return csv.DictReader(input_file)

    def fetch_api(self, account_id):
        """
        :param: pass an account_id
        :return: json (dict) response from the api
        """
        with requests.get(API_ENDPOINT + account_id) as x:
            if x.status_code == 200:
                return x.json()
            else:
                pass # look into logger to send msg to std.err

    def merge(self, account):
        """
        Parse the csv; for each account id, hit the API and merge the data
        :return: list of dictionaries for each account id
        """    
        api_response = self.fetch_api(account['Account ID'])
        if api_response is not None:
            account['Status'] = api_response['status']
            account['Status Set On'] = api_response['created_on']
            return account


    def write_to_new_file(self, input_file, output_file):
        """
        Call merge() and write the merged data to our output_file
        """
        with open(output_file, 'w') as csvfile:
            fieldnames = "Account ID", "First Name", "Created On", "Status", "Status Set On"
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.parse_csv(open(input_file, 'r')):
                self.merge(account)                
                del account['Account Name']  # Account name doesn't need to be written to the new csv
                writer.writerow(account)
