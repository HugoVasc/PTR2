#Build with docker build -t ttp-server .
#Run with docker run ttp-server
FROM python:3.11.0b5

ADD server.py .

RUN python -m pip install --upgrade pip

CMD ["python", "./server.py"]