import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='[options] <filepath1> <filepath2>')
    parser.add_argument('first_file', help=argparse.SUPPRESS)
    parser.add_argument('second_file', help=argparse.SUPPRESS)
    parser.add_argument('-V', '--version',
                        help='output the version number',
                        metavar="")
    parser.add_argument('-f', '--format',
                        help='output format (default: "stylish")',
                        metavar="",
                        default='stylish')
    return parser.parse_args()
