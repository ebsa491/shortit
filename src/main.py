#!/usr/bin/python
"""Stop sending long url, short it with a command in terminal."""

import sys
import api
from properties import RED_COLOR, GREEN_COLOR, NO_COLOR

def main():
    """The main function of the program."""

    args = check_args()

    if args == -1:
        print(f"[{RED_COLOR}-{NO_COLOR}] USAGE: shortit URL")
        sys.exit(1)
        return
    
    api_manager = api.UrlAPI()

    api_manager.set_url(args)
    response_stauts, result = api_manager.request_short_url()

    if response_stauts == -1:
        print(f"[{RED_COLOR}-{NO_COLOR}] Error in connecting to the API server...")
        ans = input("Do you want to know the error? [Y/n] ")
        if ans.lower() != 'n':
            print(result)

        sys.exit(1)
        return
    
    api_manager.extract_data_from_html(result)

    print("=========================")
    print(GREEN_COLOR + api_manager.get_short_url() + NO_COLOR)
    print("=========================")

    sys.exit(0)
    return

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
