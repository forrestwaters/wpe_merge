import os
import sys
import unittest
sys.path.append('/Users/forrest.waters/projects/scratch/scratch/forrestwaters/wpe_merge')
from merge import WpeMerge
from collections import OrderedDict


class TestWpeMerge(unittest.TestCase):

    mock_csv_data = [OrderedDict([('Account ID', '12345'), ('Account Name', 'lexcorp'), ('First Name', 'Lex'), ('Created On', '1/12/11')])]

    mock_api_response = {"account_id":12345,"status":"good","created_on":"2011-01-12"}

    def test_parse_csv(self):
        wpm_parse = WpeMerge('unittests/test.csv', 'unittests/new.csv').parse_csv()
        self.assertEqual(wpm_parse, self.mock_csv_data)


if __name__ == '__main__':
    unittest.main()