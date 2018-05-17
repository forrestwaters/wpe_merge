import os
import sys
import unittest
sys.path.append('/Users/forrest.waters/projects/scratch/scratch/forrestwaters/wpe_merge') #this seems bad
from merge import WpeMerge
from collections import OrderedDict


class TestWpeMerge(unittest.TestCase):

    wpm = WpeMerge('unittests/test.csv', 'unittests/new.csv')

    def test_parse_csv(self):
        expected_csv_data = [OrderedDict([('Account ID', '12345'), ('Account Name', 'lexcorp'), ('First Name', 'Lex'), ('Created On', '1/12/11')])]
        
        self.assertEqual(
            self.wpm.parse_csv(), 
            expected_csv_data)

    
    def test_fetch_api(self):
        expected_api_response = {"account_id":12345,"status":"good","created_on":"2011-01-12"}
        
        self.assertEqual(
            self.wpm.fetch_api('12345'), 
            expected_api_response
            )

    
    def test_merge(self):
        expected_merge = [OrderedDict([('Account ID', '12345'), ('Account Name', 'lexcorp'), ('First Name', 'Lex'), ('Created On', '1/12/11'), ('Status', 'good'), ('Status Set On', '2011-01-12')])]
        self.assertEqual(
            self.wpm.merge(), 
            expected_merge
        )


if __name__ == '__main__':
    unittest.main()