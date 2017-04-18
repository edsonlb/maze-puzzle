# A-Maze-ingly Retro Route Puzzle #

[![Build Status](https://travis-ci.org/edsonlb/maze-puzzle.svg?branch=master)](https://travis-ci.org/edsonlb/maze-puzzle)

![Local Tests](http://image.prntscr.com/image/e9ca43d8ecf44c58813bc3643422f0f0.png)

Problem:
Write a program that will output a valid route one could follow to collect all specified items within a map. The map is a json description of set of rooms with allowed path and contained object.
exercize starts with an input of:
json reppresentation of map starting room
list of object to collect

```
Room type allowed fields
  id: Integer
  name: String
  north: Integer //referring to a connected room
  south: Integer //referring to a connected room
  west: Integer  //referring to a connected room
  east: Integer  //referring to a connected room
  objects: List  //of Objects
Object type allowed fields
  name: String //Object Name
```

This is an example of a map:
```
{
"rooms": [
  { "id": 1, "name": "Hallway", "north": 2, objects: [] },
  { "id": 2, "name": "Dining Room", "south": 1, "west": 3, "east": 4, objects: []
},
  { "id": 3, "name": "Kitchen","east":2, objects: [ { "name": "Knife" } ] },
  { "id": 4, "name": "Sun Room","weast":2, objects: [ { "name": "Potted Plant" } ]
}
] }
```

### Example ###
Input Start Room ID= 2
Input Objects To Collect= Knife, Potted Plant
```
python app.py data.json 2 "knife" "Potted Plant"
```
will produce the following output:

![System Output](http://image.prntscr.com/image/848f0646fe3c457eba4737d10938417f.png)

### Assumptions ###
I made the following assumptions in the development of this software:
- On the example sent to me, the output ID is whrong for the "Dining Room". The column should show the real ID of the room. And the first is "0".
![Zero on the first element](http://image.prntscr.com/image/b6e48314a69e44299450ddce3ddc8fc4.jpeg)

- The "west" coordinate of the "Sun Room" is whrong "weast".
![weast is not west](http://image.prntscr.com/image/c75f8b5419294f1ca9305ebb880c7a72.jpeg)

- The JSON file can have None, One or More "objects" in the array node in each room.
![weast is not west](http://image.prntscr.com/image/157b9bb562704c039a27147ea3fc103e.jpeg)

- This is my first code with Docker (Hope to improve more, I liked)
```
 docker run --rm -v /home/edson/test_json/test1_data.json:/test_app edsonlb/maze-puzzle /test_app/data.json 2 "Knife" "Potted Plant"
```

- The program quits the execution when some error is found.

### Additional Goals ### 
- TDD approach.
- Build a Docker container with runnable code inside so that we can mount a volume in it and test on different maps.