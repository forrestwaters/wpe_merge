import csv
import requests
from merge import WpeMerge


def main():
    account_merge = WpeMerge("sample.csv", "new.csv")
    print account_merge.merged_list

if __name__ == '__main__': main()
