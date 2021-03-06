import csv
import logging
import requests

API_ENDPOINT = "http://interview.wpengine.io/v1/accounts/"

logger = logging.getLogger()


class WpeMerge(object):
    """
    Given a csv file with the following columns:
    Account ID,Account Name,First Name,Created On

    Fetch an api that will have the following fields:
    Account ID,Status, Status Set On

    Merge this data to a new csv with the following fields:
    Account ID, First Name, Created On, Status, Status Set On
    """
    @staticmethod
    def get_api_data(account_id):
        """
        :param: pass an account_id
        :return: json (dict) response from the api
        """
        with requests.get(API_ENDPOINT + account_id) as x:
            if x.status_code == 200:
                return x.json()
            else:
                logger.warning('Invalid API response for Account ID {}.'.format(account_id))

    def merge(self, account):
        """
        hit the API and merge the data
        :param: pass account_id
        :return: merged account dictionary
        """
        if account['Account ID'] is not '':
            api_response = self.get_api_data(account['Account ID'])
            if api_response is not None:
                account['Status'] = api_response['status']
                account['Status Set On'] = api_response['created_on']
                return account

    def write_to_new_file(self, input_file, output_file):
        """
        Iterate over the csv file, calling merge() for each line
        and writing to the new file
        :param: opened source csv file in read status
        :param: opened destination file to be written to, also in write status
        """
        fieldnames = "Account ID", "First Name", "Created On", "Status", "Status Set On"
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for account in csv.DictReader(input_file):
            self.merge(account)
            if len(account) == 6:  # only write to the new file if all fields are there
                del account['Account Name']  # Account name shouldn't be written to the new csv
                writer.writerow(account)
            else:
                if account['Account ID'] == '':
                    message = 'Line with blank account ID found in file'
                else:
                    message = 'Account {} is missing values'.format(account['Account ID'])
                logger.warning('{}. Not writing to merged file.'.format(message))
