FROM ubuntu
ADD App.py /
ADD Maze.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
ENTRYPOINT /