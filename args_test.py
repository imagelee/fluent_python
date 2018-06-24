import argparse
import sys


def parse_argv():
    parser = argparse.ArgumentParser(description='test for argparse')
    parser.add_argument(dest='filenames', metavar='filenames', nargs='*')
    parser.add_argument('-p', '--pat', metavar='pattern', required=True,
                        dest='patterns', action='append',
                        help='text pattern to search for')
    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='verbose mode')
    parser.add_argument('-o', dest='outfile', action='store',
                        help='output file')
    parser.add_argument('--speed', dest='speed', action='store',
                        choices=('slow', 'fast'), default='slow',
                        help='search speed')

    args = parser.parse_args()

    print(args.filenames)
    print(args.patterns)
    print(args.verbose)
    print(args.outfile)
    print(args.speed)


if __name__ == '__main__':
    print(sys.argv)

    parse_argv()
