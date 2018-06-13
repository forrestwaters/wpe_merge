import argparse
from merge import WpeMerge


def parse_args():
    parser = argparse.ArgumentParser(description='WPE Merge Project', usage='%(prog)s input.csv output.csv')
    parser.add_argument('input', type=argparse.FileType('r'), help='Source csv file with list of accounts.')
    parser.add_argument('output', type=argparse.FileType('w'), help='Output file with merged account data.')
    return parser.parse_args()


def main():
    args = parse_args()
    account_merge = WpeMerge()
    account_merge.write_to_new_file(args.input, args.output)
    args.input.close()  # TODO: possibly use with so we don't have to close the file
    args.output.close()


if __name__ == '__main__':
    main()
