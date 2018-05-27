import os
import csv
import unittest
from io import StringIO
from src.merge import WpeMerge
from collections import OrderedDict


class TestWpeMerge(unittest.TestCase):
    input_file = StringIO("""Account ID,Account Name,First Name,Created On
    12345,lexcorp,Lex,1/12/11""")
    out_file = './new.csv'
    wpm = WpeMerge()

    def test_parse_csv(self):
        self.assertIsInstance(self.wpm.parse_csv(self.input_file), csv.DictReader)

    def test_fetch_api(self):
        expected_api_response = {"account_id": 12345, "status": "good", "created_on": "2011-01-12"}

        self.assertEqual(self.wpm.fetch_api('12345'), expected_api_response)

    def test_merge(self):
        account = OrderedDict([('Account ID', '12345'), ('Account Name', 'lexcorp'), ('First Name', 'Lex'), ('Created On', '1/12/11')])
        expected_merge = OrderedDict([('Account ID', '12345'), ('Account Name', 'lexcorp'), ('First Name', 'Lex'), ('Created On', '1/12/11'), ('Status', 'good'), ('Status Set On', '2011-01-12')])

        self.assertEqual(self.wpm.merge(account), expected_merge)

    def test_write_new_file(self):
        expected_csv = 'Account ID,First Name,Created On,Status,Status Set On\r\n12345,Lex,1/12/11,good,2011-01-12\r\n'

        self.wpm.write_to_new_file(self.input_file, self.out_file)
        content = self.input_file

        self.assertEqual(content, expected_csv)

        os.remove('./new.csv')
