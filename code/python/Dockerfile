FROM python:3.8

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./code/python .

CMD python main.py