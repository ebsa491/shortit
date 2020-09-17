#!/usr/bin/python
"""Stop sending long url, short it with a command in terminal."""

import sys
import api
from properties import RED_COLOR, GREEN_COLOR, NO_COLOR # Useful for coloring the outputs.

def main():
    """The main function of the program."""

    args = check_args()

    if args == -1:
        # Arguments aren't correct

        print(f"[{RED_COLOR}-{NO_COLOR}] USAGE: shortit URL")
        sys.exit(1)
        return
    
    api_manager = api.UrlAPI()

    api_manager.set_url(args)
    response_stauts, result = api_manager.request_short_url() # Sends the request to the API

    if response_stauts == -1:
        # Can't connect to the API

        print(f"[{RED_COLOR}-{NO_COLOR}] Error in connecting to the API server...")
        ans = input("Do you want to know the error? [Y/n] ") # For more information about thr error
        if ans.lower() != 'n':
            print(result)

        sys.exit(1)
        return
    
    if api_manager.extract_data_from_html(result) == -1:
        # Can't parse the html_page
        
        print(f"[{RED_COLOR}-{NO_COLOR}] Error in parsing the response...")
        sys.exit(1)
        return

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
        return " ".join(sys.argv[1:]) # Converts the arguments list to string
    else:
        return -1

if __name__ == '__main__':
    main()
