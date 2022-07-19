FROM python:latest
USER root
RUN apt-get update -y && apt-get upgrade -y && apt install libgl1-mesa-dev -y

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install opencv-python paho-mqtt

CMD [ "python3", "/root/opt/main.py" ]