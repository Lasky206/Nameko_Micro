FROM python:3

RUN apt-get update && apt-get -y install netcat && apt-get -y install dos2unix && apt-get clean

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY config.yml ./
COPY run.sh ./
COPY Airports.py ./

RUN dos2unix run.sh
RUN chmod +x ./run.sh

CMD ["./run.sh"]
