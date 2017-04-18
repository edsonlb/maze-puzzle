FROM python:2.7
COPY maze-puzzle /application
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "App.py"]