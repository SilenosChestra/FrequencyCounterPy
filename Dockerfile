FROM python:latest

COPY config/python /conf

RUN pip install --upgrade pip -r /conf/requirements.txt

COPY src /srv

WORKDIR /srv

ENTRYPOINT ["uwsgi"]

CMD ["--ini", "/srv/uwsgi.ini"]
