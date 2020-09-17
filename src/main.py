#!/usr/bin/python
"""Stop sending long url, short it with a command in terminal."""

import sys

def main():
    """The main function of the program."""

    args = check_args()

    if args == -1:
        print("USAGE: shortit URL")
        sys.exit(-1)

def check_args():
    """
    This method checks the program's arguments count.
    If arguments were correct, sets self.program_args = \" \".join(sys.argv[1:]).
    """

    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    else:
        return -1

if __name__ == '__main__':
    main()
