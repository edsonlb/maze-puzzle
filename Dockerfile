FROM python:2.7
ADD App.py /
ADD Maze.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
ENTRYPOINT /