FROM python:3.10.11

ADD main.py .

CMD ["python3", "./main.py"]
