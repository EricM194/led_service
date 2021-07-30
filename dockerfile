FROM python:3.8-slim-buster
WORKDIR /code
ADD / /
RUN pip3 install flask
RUN pip3 install python-magichue
EXPOSE 5000
COPY . .
ENV LED_IP=0.0.0.0
CMD [ "python app.py > log.txt 2>&1 &"]
