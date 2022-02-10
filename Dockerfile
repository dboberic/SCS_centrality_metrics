FROM tiangolo/uwsgi-nginx-flask:python3.8
ENV LISTEN_PORT 5000
ENV UWSGI_CHEAPER 4
ENV UWSGI_PROCESSES 64
EXPOSE 5000
COPY ./app /app
COPY uwsgi.ini /etc/uwsgi
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
