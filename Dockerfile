FROM python:3.8.13-slim-buster 

WORKDIR /the/workdir/path

COPY ./imdb_project ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r requirements.txt /app/requirements.txt --no-cache-dir 

CMD ["python3", "manage.py", "runserver"]





