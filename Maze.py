# -*- coding: utf-8 -*-
import sys, json
from terminaltables import AsciiTable

class Maze:
    """Will solve the maze!"""

    def __init__(self, start_node=0, json_file='', search_parameters=[]):
        self.search_parameters = search_parameters
        self.output = [['ID', 'Room', 'Object collected']]
        self.json_array = self.validate_json(json_file)
        #self.get_item_from_id(int(start_node))

    def get_item_from_id(self, my_id):
        """Return internal item from a posision based on the item ID field."""
        array_id = (obj for obj in self.json_array['rooms'] if obj["id"] == my_id).next()

        if array_id:
            return array_id
        else:
            print 'END OF ITEMS.'
            sys.exit(0)

    def validate_json(self, my_file):
        """Because the "object" node made by "Scm Italy" was not in the JSON standards."""

        if not my_file:
            print 'YOU DONT KNOW HOW TO PLAY :-)'

        try:
            print 'VALIDATING JSON...'
            return json.loads(my_file)
        except:
            try:
                print 'VALIDATING JSON WITH OBJECT TAG CORRECTION...'
                return json.loads(my_file.read().replace('objects', '"objects"'))
            except:
                print 'YOU DONT KNOW HOW TO PLAY :-)'

    def print_output(self):
        """Lets print this"""
        format = AsciiTable(self.output)
        print format.table
