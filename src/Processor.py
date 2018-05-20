import argparse
from merge import WpeMerge


def parse_args():
    parser = argparse.ArgumentParser(description='WPE Merge Project', usage ='%(prog)s source.csv new.csv')
    parser.add_argument('input', help='Source csv file with list of accounts.')
    parser.add_argument('output', help='Output file with merged account data.')
    return parser.parse_args()


def main():
    args = parse_args()
    account_merge = WpeMerge(args.input, args.output)
    account_merge.write_to_new_file()

if __name__ == '__main__': main()
