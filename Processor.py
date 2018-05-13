import csv
import requests
from merge import WpeMerge


def main():
    account_merge = WpeMerge("sample.csv", "new.csv")
    account_merge.write_to_new_file()

if __name__ == '__main__': main()
