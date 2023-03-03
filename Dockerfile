FROM python:3.8
WORKDIR /Flask-App
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app ./app
CMD ["python","./app/flaskapp.py"]
