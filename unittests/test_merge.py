import io
import os
import unittest
from collections import OrderedDict

from merge import WpeMerge


class TestWpeMerge(unittest.TestCase):
    out_file = './new.csv'
    wpm = WpeMerge('./new.csv')

    def test_parse_csv(self):
        expected_csv_data = [OrderedDict(
            [('Account ID', '12345'), ('Account Name', 'lexcorp'), ('First Name', 'Lex'), ('Created On', '1/12/11')])]

        self.assertEqual(
            self.wpm.parse_csv(io.BytesIO(b"""Account ID,Account Name,First Name,Created On
12345,lexcorp,Lex,1/12/11""")),
            expected_csv_data)

    def test_fetch_api(self):
        expected_api_response = {"account_id": 12345, "status": "good", "created_on": "2011-01-12"}

        self.assertEqual(
            self.wpm.fetch_api('12345'),
            expected_api_response
        )

    def test_merge(self):
        expected_merge = [OrderedDict(
            [('Account ID', '12345'), ('Account Name', 'lexcorp'), ('First Name', 'Lex'), ('Created On', '1/12/11'),
             ('Status', 'good'), ('Status Set On', '2011-01-12')])]

        self.assertEqual(
            self.wpm.merge(io.BytesIO(b"""Account ID,Account Name,First Name,Created On
12345,lexcorp,Lex,1/12/11""")),
            expected_merge
        )

    def test_write_new_file(self):
        expected_csv = 'Account ID,First Name,Created On,Status,Status Set On\r\n12345,Lex,1/12/11,good,2011-01-12\r\n'

        self.wpm.write_to_new_file(io.BytesIO(b"""Account ID,Account Name,First Name,Created On
12345,lexcorp,Lex,1/12/11"""))
        test_csv_file = open(self.out_file, 'r')
        content = test_csv_file.read()
        test_csv_file.close()

        self.assertEqual(
            content,
            expected_csv
        )

        os.remove('./new.csv')
