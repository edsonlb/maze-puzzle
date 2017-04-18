FROM python:2.7
ADD App.py /
ADD Maze.py /
RUN pip install terminaltables
COPY maze-puzzle /bin/maze-puzzle
ENTRYPOINT ["maze-puzzle"]