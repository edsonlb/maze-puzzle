# -*- coding: utf-8 -*-
"""Return internal item from a posision based on the item ID field."""
import sys
from pprint import pprint

def main():
    """Lets run!"""

    try:
        parameters = sys.argv
        json_file = open(parameters[1])

        start_node = parameters[2]
        if int(start_node) > 0:
            print 'STARTING AT ID: '+start_node
        else:
            print 'YOU DONT KNOW HOW TO PLAY :-)'

        search_parameters = []
        for item in parameters[3:]:
            if item:
                search_parameters.append(item)

        print len(search_parameters)
        if len(search_parameters) == 0:
            print 'YOU DONT KNOW HOW TO PLAY :-)'
            sys.exit(0)
        else:
            print 'SEARCHING:'
            pprint(search_parameters)
    except:
        print 'YOU DONT KNOW HOW TO PLAY :-)'

if __name__ == "__main__":
    main()
