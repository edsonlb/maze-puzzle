# A-Maze-ingly Retro Route Puzzle #

[![Test Build Status](https://travis-ci.org/edsonlb/maze-puzzle.svg?branch=master)](https://travis-ci.org/edsonlb/maze-puzzle) [![Docker Build Status](https://img.shields.io/docker/build/jrottenberg/ffmpeg.svg)](https://hub.docker.com/r/edsonlb/maze-puzzle/)

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
- On the example sent to me, the output ID is wrong for the "Dining Room". The column should show the real ID of the room. And the first is "0".
![Zero on the first element](http://image.prntscr.com/image/b6e48314a69e44299450ddce3ddc8fc4.jpeg)

- The "west" coordinate of the "Sun Room" is wrong "weast".
![weast is not west](http://image.prntscr.com/image/c75f8b5419294f1ca9305ebb880c7a72.jpeg)

- The JSON file can have None, One or More "objects" in the array node in each room.
![weast is not west](http://image.prntscr.com/image/157b9bb562704c039a27147ea3fc103e.jpeg)

- This is my FIRST code with Docker (Hope to improve & learn more, I liked!): https://hub.docker.com/r/edsonlb/maze-puzzle/
```
# Internal Docker Folder: /usr/src/app/
docker run --rm -v /PATH/TO/FILE/MY_DATA.json:/usr/src/app/MY_DATA.json edsonlb/maze-puzzle /usr/src/app/MY_DATA.json INDEX "NEEDLE 1" "NEEDLE 2" "NEEDLE 3"

#EXAMPLE
docker run --rm -v /Users/edsonlb/test_json/test_data.json:/usr/src/app/test_data.json edsonlb/maze-puzzle /usr/src/app/test_data.json 2 "Knife" "Potted Plant"
```
![Docker in Action](http://image.prntscr.com/image/13fe998a1406479d8f1e0e7ff3a08f74.png)

- And the last observation: The program quits the execution when some error is found (for simplification).

### Additional Goals ### 
- TDD approach.
- Build a Docker container with runnable code inside so that we can mount a volume in it and test on different maps.
