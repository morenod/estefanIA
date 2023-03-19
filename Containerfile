FROM python:3.11
MAINTAINER morenod

ADD bot.py /
ADD requirements.txt /
ADD libs /libs
RUN apt-get update && apt-get upgrade -y
RUN pip3 install --no-cache --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "-u", "/bot.py"]
