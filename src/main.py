#!/usr/bin/python
"""Stop sending long url, short it with a command in terminal."""

import sys

class ShortIt:
    """shortit main class."""

    def __init__(self):
        """ __init__ """

        self.program_args = ""

        self.__check_args()

    def __check_args(self):
        """
        This method checks the program's arguments count.
        If arguments were correct, sets self.program_args = \" \".join(sys.argv[1:]).
        """

        if len(sys.argv) > 1:
            self.program_args = " ".join(sys.argv[1:])
        else:
            print("USAGE: shortit URL")
            sys.exit(1)

if __name__ == '__main__':
    app = ShortIt()
