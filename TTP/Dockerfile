#Build with docker build -t ttp-server .
#Run with docker run ttp-server
FROM python:3.11.0b3

ADD main.py .

RUN python -m pip install --upgrade pip

RUN pip install requests beautifulsoup4

CMD ["python", "./main.py"]