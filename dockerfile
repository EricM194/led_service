FROM python:3
WORKDIR /code
ADD / /
RUN pip install python-magichue
RUN pip install flask
EXPOSE 5000
COPY . .
CMD [ "python", "./app.py" ]
