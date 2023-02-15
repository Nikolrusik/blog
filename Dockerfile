FROM python:3.10.7-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python3 -m flask db init
RUN python3 -m flask db migrate
RUN python3 -m flask db upgrade

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000

CMD ["python3",  "-m" , "flask", "run", "--host=0.0.0.0"]