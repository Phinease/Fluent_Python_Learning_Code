import argparse


def process_args():
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument('-a', '--all', metavar='A', nargs='*', help='help_a')
    arg = parser.parse_args()
    return arg


def main():
    print(process_args())


if __name__ == '__main__':
    main()