# -*- coding: utf-8 -*-
import sys, json
from terminaltables import AsciiTable

class Maze:
    """Will solve the maze!"""

    def __init__(self, start_node=0, json_file='', search_parameters=[]):
        self.search_parameters = search_parameters
        self.output = [['ID', 'Room', 'Object collected']]
        self.json_array = self.validate_json(json_file)
        self.search_elements(self.get_item_from_id(int(start_node)))

    def get_item_from_id(self, my_id):
        """Return internal item from a posision based on the item ID field."""
        try:
            obj_id = (obj for obj in self.json_array['rooms'] if obj["id"] == my_id).next()

            if obj_id:
                return obj_id
            else:
                print 'YOU DONT KNOW HOW TO PLAY :-)'
                return None
        except:
            print 'YOU DONT KNOW HOW TO PLAY :-)'
            return None

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
                print 'THE FILE IS NOT A JSON!'


    def search_elements(self, my_item):
        """Get the elements on the "object" node of an item list."""
        if not my_item:
            return None

        needles_found = []

        for needle in self.search_parameters:
            try:
                obj_found = (obj for obj in my_item['objects'] if obj["name"].upper() == needle.upper()).next()
                needles_found.append(obj_found['name'])
            except:
                pass

        if needles_found:
            objects_collected = ','.join(needles_found)
        else:
            objects_collected = 'None'

        self.output.append([my_item['id'], my_item['name'], objects_collected])
        self.navigate(my_item)


    def navigate(self, my_item):
        """Get the direction of the itens navigation."""
        position_of_item = [i for i, j in enumerate(self.json_array['rooms']) if j == my_item]

        if 'north' in my_item:
            new_node = my_item['north']
            self.json_array['rooms'][position_of_item[0]].pop('north')
            self.search_elements(self.get_item_from_id(new_node))

        if 'south' in my_item:
            new_node = my_item['south']
            self.json_array['rooms'][position_of_item[0]].pop('south')
            self.search_elements(self.get_item_from_id(new_node))

        if 'west' in my_item:
            new_node = my_item['west']
            self.json_array['rooms'][position_of_item[0]].pop('west')
            self.search_elements(self.get_item_from_id(new_node))

        if 'east' in my_item:
            new_node = my_item['east']
            self.json_array['rooms'][position_of_item[0]].pop('east')
            self.search_elements(self.get_item_from_id(new_node))

    def print_output(self):
        """Lets print this"""
        format = AsciiTable(self.output)
        print format.table
