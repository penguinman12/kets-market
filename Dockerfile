FROM python:3.11.0

WORKDIR /home/

RUN echo "testing123456789"

RUN git clone https://github.com/penguinman12/kets-market.git

WORKDIR /home/kets-market/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=prag.settings.deploy && python manage.py migrate --settings=prag.settings.deploy && gunicorn prag.wsgi --env DJANGO_SETTINGS_MODULE=prag.settings.deploy --bind 0.0.0.0:8000"]
