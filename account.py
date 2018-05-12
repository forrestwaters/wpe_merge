import requests

API_ENDPOINT = "http://interview.wpengine.io/v1/accounts/"


class Account(object):
    """
    Takes a csv file containing a few values
    Using the account ID, hit an API to get a few more values
    Object ends up containing the following values: Account ID, First Name, Created On, Status, and Status Set On
    """

    
    def __init__(self, csv_json):
        self.account_id = csv_json['Account ID']
        self.account_name = csv_json['Account Name']
        self.first_name = csv_json['First Name']
        self.created_on = csv_json['Created On']

        x = requests.get(API_ENDPOINT + self.account_id).json()
        self.status = x['status']
        self.status_set_on = x['created_on']


