FROM python:2.7
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "App.py"]